from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Department(models.Model):
    name = models.CharField(max_length=100)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="departments", default=1)  # assuming Company with ID 1 exists

    def __str__(self):
        return self.name

class Employee(models.Model):
    name = models.CharField(max_length=100)
    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name="employees")
    department = models.ForeignKey(Department, on_delete=models.CASCADE, related_name="employees", null=True, blank=True)

    def __str__(self):
        return self.name
