from django.contrib import admin
from .models import Company, Department, Employee

# Register your models here.
admin.site.register(Company)  # Company model ko register kar rahe hain
admin.site.register(Department)
admin.site.register(Employee)
