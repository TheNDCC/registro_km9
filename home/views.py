from django.shortcuts import render
from sales.models import Product, Sale
from expenses.models import Expense, Credit, Payment
from subsidiaries.models import Subsidiary, CashFlow
from employees.models import Employee, Commission
import datetime
from django.db import models

expenses_quantity = 10
credits_quantity = 5
payments_quantity = 5
employees_days = 7
commission_rate = 3
minimum_sales_for_commission = 100
products_commission= ["Pollo Asado", "Pollo Rostizado"]

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
        diff = int(request.POST.get("diff"))
        CashFlow.objects.create(date=date, cash=cash, card=card, diff=diff, subsidiary=subsidiary)


    context = {
        "expenses_quantity": range(expenses_quantity),
        "credits_quantity": range(credits_quantity),
        "payments_quantity": range(payments_quantity),
        "products": products,
        "subsidiaries": Subsidiary.objects.all(),
        "today": datetime.date.today(),

    }
    
    return render(request, 'home.html', context)

def employee_dashboard(request):
    employees = Employee.objects.all()
    if request.method == "POST":
        
        for i in range(employees_days):
            date = datetime.datetime.strptime(request.POST.get(f"date-{i}"), "%Y-%m-%d")
            sales = Sale.objects.filter(date=date, product__name__in=products_commission)
            sale_quantity = sales.aggregate(total=models.Sum('quantity'))['total']
            
            if sale_quantity is None:
                sale_quantity=0
            for employee in employees:
                subsidiary = request.POST.get(f"subsidiary-{employee.id}-{i}")
                if subsidiary != "0":
                    subsidiary = Subsidiary.objects.get(name=subsidiary)
                    Commission.objects.create(employee=employee, date=date,  subsidiary=subsidiary, commission_rate=commission_rate, sale_quantity=sale_quantity)
    context = {
        "employees": employees,
        "date": datetime.date.today(),
        "days": range(employees_days),
        "subsidiaries": Subsidiary.objects.all(),
    }
    
    return render(request, 'employee_dashboard.html', context)