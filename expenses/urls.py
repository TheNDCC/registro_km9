from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.expense_register, name='expense_register'),
    path('credit/register/', views.credit_register, name='credit_register'),
]