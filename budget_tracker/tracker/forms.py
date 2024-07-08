from django import forms
from .models import *

class IncomeForm(forms.ModelForm):
    """Form definition for Income."""

    class Meta:
        """Meta definition for Incomeform."""

        model = Income
        fields = '__all__'

class ExpenseForm(forms.ModelForm):
    """Form definition for Expense."""

    class Meta:
        """Meta definition for Expenseform."""

        model = Expense
        fields = '__all__'

class ExpenseCategoryForm(forms.ModelForm):
    """Form definition for ExpenseCategory."""

    class Meta:
        """Meta definition for ExpenseCategoryform."""

        model = ExpenseCategory
        fields = "__all__"

class IncomeCategoryForm(forms.ModelForm):
    """Form definition for IncomeCategory."""

    class Meta:
        """Meta definition for IncomeCategoryform."""

        model = IncomeCategory
        fields = "__all__"

