from django.contrib import admin
from .models import Expense, Credit, Payment

# Register your models here.
admin.site.register(Expense)
admin.site.register(Credit)
admin.site.register(Payment)