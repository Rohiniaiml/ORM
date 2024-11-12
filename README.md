# Ex02 Django ORM Web Application
## Date: 

## AIM
To develop a Django application to store and retrieve data from a bank loan database using Object Relational Mapping(ORM).

## ENTITY RELATIONSHIP DIAGRAM



## DESIGN STEPS

### STEP 1:
Clone the problem from GitHub

### STEP 2:
Create a new app in Django project

### STEP 3:
Enter the code for admin.py and models.py

### STEP 4:
Execute Django admin and create details for 10 books

## PROGRAM
```
admin.py

from django.contrib import admin
from .models import bankloan,bankloanAdmin
admin.site.register(bankloan,bankloanAdmin)

models.py

from django.db import models

# Create your models here.
from django.db import models
from django.contrib import admin
class bankloan(models.Model):
        Name=models.CharField(max_length=6)
        Loan_type=models.CharField(max_length=10)
        Loan_amount=models.IntegerField(primary_key="Loan_amount")
        Rate_of_intrest=models.FloatField()
        Duration=models.CharField(max_length=10)
        EMI=models.IntegerField()
        Total_amount=models.IntegerField()
        Intrest=models.IntegerField()
class bankloanAdmin(admin.ModelAdmin):
        list_display=('Name','Loan_type','Loan_amount','Rate_of_intrest','Duration','EMI','Total_amount','Intrest')

         
```

## OUTPUT
![alt text](<Screenshot 2024-11-13 000001.png>)





## RESULT
Thus the program for creating a database using ORM hass been executed successfully
