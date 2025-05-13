from django.shortcuts import render
from django.http import JsonResponse
from .models import Employee, Company
from .function import my_function

# Your custom function
def run_function(request):
    result = my_function()
    return render(request, 'function/result.html', {'result_list': result})


# 🔍 Uses select_related to optimize FK lookups (Employee → Company, Department)
def employee_list_with_related(request):
    employees = Employee.objects.select_related('company', 'department').all()
    data = []
    for emp in employees:
        data.append({
            'employee_name': emp.name,
            'company_name': emp.company.name,
            'department_name': emp.department.name if emp.department else None
        })
    return JsonResponse(data, safe=False)


# 🔄 Uses prefetch_related to optimize reverse FK lookups (Company → Employees)
def company_list_with_employees(request):
    companies = Company.objects.prefetch_related('employees').all()
    data = []
    for company in companies:
        data.append({
            'company_name': company.name,
            'employees': [{'id': emp.id, 'name': emp.name} for emp in company.employees.all()]
        })
    return JsonResponse(data, safe=False)
