from django.db import models

# Create  models here.
class Company(models.Model):
    name = models.CharField(max_length=50)
    company_id = models.AutoField(primary_key=True)
    location = models.CharField(max_length=100)      
    about = models.TextField()
    type = models.CharField(max_length=100, choices=(('IT', 'IT'), 
                                                    ('NON-IT', 'NON-IT'),
                                                    )
                            )
    phone_number = models.CharField(max_length=10)
    email = models.EmailField()
    added_date = models.DateTimeField(auto_now_add=True)


    
# employee model
class Employee(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=10)
    email = models.EmailField()
    about = models.TextField()
    position=models.CharField(max_length=50, choices=(
                                ('Manager', 'Manager'),
                                ('Developer', 'Developer'),
                                ('HR', 'HR')
                ))
    
    company=models.ForeignKey(Company, on_delete=models.CASCADE)