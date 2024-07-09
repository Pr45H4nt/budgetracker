from django.urls import path
from . import views
from . import forms
from . import models

urlpatterns = [
    path("", views.indexview, name = "home"),
    path("add/income", views.addview, {'formtype':forms.IncomeForm}, name = "addincome"),
    path("add/incomecategory", views.addview, {'formtype': forms.IncomeCategoryForm}, name = "addincomecategory"),
    path("add/expense", views.addview, {'formtype': forms.ExpenseForm}, name = "addexpense"),
    path("add/expensecategory", views.addview, {'formtype': forms.ExpenseCategoryForm}, name = "addexpensecategory"),
    path('show/income', views.showdb , {'database' : models.Income , 'datacategory': models.IncomeCategory}, name= 'showincome' ),
    path('show/expense', views.showdb , {'database' : models.Expense , 'datacategory': models.ExpenseCategory}, name= 'showexpense' ),
]