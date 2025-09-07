from django.shortcuts import render
from .models import Expense
from subsidiaries.models import Subsidiary

# Create your views here.
def expense_register(request):
    if request.method == 'POST':
        # Process the form data here
        date = request.POST.get('date')
        subsidiary_id = request.POST.get('subsidiary')
        subsidiary = Subsidiary.objects.get(id=subsidiary_id)
        total_items = int(request.POST.get('total_items', 0))
        for i in range(total_items):
            description = request.POST.get(f'description-{i}')
            amount = request.POST.get(f'amount-{i}')
            if description and amount:
                new_expense = Expense.objects.create(date=date, description=description, amount=amount , subsidiary=subsidiary  )
                new_expense.save()
    context={
        'subsidiaries': Subsidiary.objects.all()
    }
    return render(request, 'expense_register.html',context)