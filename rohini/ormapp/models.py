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

         
