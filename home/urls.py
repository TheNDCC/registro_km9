from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('employee/', views.employee_dashboard, name='employee_dashboard'),
    path('employee/report/', views.employee_report, name='employee_report'),
    path('employee/report/<int:employees_id>/<str:date_from>/<str:date_to>', views.employee_report, name='employee_report'),
]