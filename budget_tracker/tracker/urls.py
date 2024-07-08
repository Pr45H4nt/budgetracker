from django.urls import path
from . import views
from . import forms

urlpatterns = [
    path("", views.indexview, name = "home"),
    path("add/income", views.addview, {'formtype':forms.IncomeForm}, name = "addincome"),
    path("add/incomecategory", views.addview, {'formtype': forms.IncomeCategoryForm}, name = "addincomecategory"),
    path("add/expense", views.addview, {'formtype': forms.ExpenseForm}, name = "addexpense"),
    path("add/incomecategory", views.addview, {'formtype': forms.ExpenseCategoryForm}, name = "addexpensecategory"),
]