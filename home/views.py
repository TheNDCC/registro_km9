from django.shortcuts import render
from sales.models import Product, Sale
from expenses.models import Expense, Credit, Payment
from subsidiaries.models import Subsidiary, CashFlow
import datetime

expenses_quantity = 20
credits_quantity = 5
payments_quantity = 5

def home(request):
    products = Product.objects.all()
    if request.method == "POST":
        date = datetime.datetime.strptime(request.POST.get("date"), "%Y-%m-%d")
        subsidiary_name = request.POST.get("subsidiary")
        subsidiary = Subsidiary.objects.get(name=subsidiary_name)
        products = Product.objects.all()
        for prod in products:
            q = int(request.POST.get(f"quantity-{prod.id}"))
            a = int(request.POST.get(f"amount-{prod.id}"))
            p = int(request.POST.get(f"price-{prod.id}"))
            if q > 0 and a > 0:
                Sale.objects.create(product=prod,quantity=q,price=p,date=date)
        for item in range(expenses_quantity):
            e = request.POST.get(f"description-{item}-expenses")
            m = int(request.POST.get(f"amount-{item}-expenses"))
            if e != "" and m > 0:
                Expense.objects.create(description=e,amount=m,subsidiary=subsidiary,date=date)
        for item in range(credits_quantity):
            e = request.POST.get(f"description-{item}-credits")
            m = int(request.POST.get(f"amount-{item}-credits"))
            if e != "" and m > 0:
                Credit.objects.create(description=e,amount=m,subsidiary=subsidiary,date=date)
        for item in range(payments_quantity):
            e = request.POST.get(f"description-{item}-payments")
            m = int(request.POST.get(f"amount-{item}-payments"))
            if e != "" and m > 0:
                Payment.objects.create(description=e,amount=m,subsidiary=subsidiary,date=date)
        cash = int(request.POST.get("cash"))
        card = int(request.POST.get("card"))
        CashFlow.objects.create(date=date, cash=cash, card=card, subsidiary=subsidiary)


    context = {
        "expenses_quantity": range(expenses_quantity),
        "credits_quantity": range(credits_quantity),
        "payments_quantity": range(payments_quantity),
        "products": products,
        "subsidiaries": Subsidiary.objects.all(),
        "today": datetime.date.today(),

    }
    
    return render(request, 'home.html', context)