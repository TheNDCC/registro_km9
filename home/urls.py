from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('employee/', views.employee_dashboard, name='employee'),
    path('employee/report/', views.employee_report, name='employee_report'),
    path('employee/report/<int:employees_id>/<str:date_from>/<str:date_to>', views.employee_report, name='employee_report'),
    path('credit/report/', views.credit_report, name='credit_report'),
    path('credit/report/<str:desc>/<str:date_from>/<str:date_to>', views.credit_report, name='credit_report'),
]