from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.expense_register, name='expense_register'),
]