from django import forms
from .models import *

class IncomeForm(forms.ModelForm):
    """Form definition for Income."""

    class Meta:
        """Meta definition for Incomeform."""

        model = Income
        fields = '__all__'
