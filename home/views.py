from django.shortcuts import render
from sales.models import Product
from subsidiaries.models import Subsidiary
import datetime

# Create your views here.

def home(request):
    products = Product.objects.all()
    
    context = {
        "expenses_quantity": range(10),
        "credits_quantity": range(10),
        "payments_quantity": range(10),
        "products": products,
        "subsidiaries": Subsidiary.objects.all(),
        "today": datetime.date.today(),

    }
    
    return render(request, 'home.html', context)