# function/function.py
from .models import Employee

def my_function():
    employees = Employee.objects.select_related('company').all()
    result = []

    for emp in employees:
        result.append(f"Employee: {emp.name}, Company: {emp.company.name}")

    return result
