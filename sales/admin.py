from django.contrib import admin
from .models import Product, Sale, BreakfastBarIncome, OtherIncome

# Register your models here.

admin.site.register(Product)
admin.site.register(Sale)
admin.site.register(BreakfastBarIncome)
admin.site.register(OtherIncome)

