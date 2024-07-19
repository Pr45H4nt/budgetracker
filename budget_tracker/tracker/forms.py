from django import forms
from .models import *

class IncomeForm(forms.ModelForm):
    """Form definition for Income."""

    class Meta:
        """Meta definition for Incomeform."""

        model = Income
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(IncomeForm, self).__init__(*args, **kwargs)
        if self.request:
            self.fields['category'].queryset = IncomeCategory.objects.filter(user= self.request.user)
    
    

class ExpenseForm(forms.ModelForm):
    """Form definition for Expense."""

    class Meta:
        """Meta definition for Expenseform."""

        model = Expense
        fields = '__all__'

    def __init__(self, *args , **kwargs):
        self.request = kwargs.pop('request', None)
        super(ExpenseForm, self).__init__(*args , **kwargs)
        if self.request:
            self.fields['category'].queryset = ExpenseCategory.objects.filter(user = self.request.user)

class ExpenseCategoryForm(forms.ModelForm):
    """Form definition for ExpenseCategory."""

    class Meta:
        """Meta definition for ExpenseCategoryform."""

        model = ExpenseCategory
        fields = ['name']


class IncomeCategoryForm(forms.ModelForm):
    """Form definition for IncomeCategory."""

    class Meta:
        """Meta definition for IncomeCategoryform."""

        model = IncomeCategory
        fields =  ['name']


