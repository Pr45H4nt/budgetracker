from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class ExpenseCategory(models.Model):
    name = models.CharField(max_length=300)
    user = models.ForeignKey(User , on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name
    
class IncomeCategory(models.Model):
    name = models.CharField(max_length=300)
    user = models.ForeignKey(User , on_delete=models.CASCADE)

    def __str__(self) -> str:
        return self.name
    
    
class Income(models.Model):
    category = models.ForeignKey(IncomeCategory, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10 , decimal_places=2)
    description = models.CharField(null=True)
    date = models.DateField()

    def __str__(self) -> str:
        return f"{self.category} -- {self.amount}"
    
class Expense(models.Model):
    category = models.ForeignKey(ExpenseCategory, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10 , decimal_places=2)
    description = models.CharField(max_length=300 , blank=True)
    date = models.DateField()

    def __str__(self) -> str:
        return f"{self.category} -- {self.amount}"

