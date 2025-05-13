from django.urls import path
from .views import run_function, employee_list_with_related, company_list_with_employees

urlpatterns = [
    path('run-function/', run_function, name='run_function'),
    path('employees/', employee_list_with_related, name='employee_list_with_related'),
    path('companies/', company_list_with_employees, name='company_list_with_employees'),
]
