from django import forms
from .models import Transaction, Goal


class TransactionForm(forms.ModelForm):
    class Meta:
        model = Transaction
        fields = ['title', 'amount', 'type']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'amount': forms.NumberInput(attrs={'class': 'form-control'}),
            'type': forms.Select(attrs={'class': 'form-select'}),
        }
class GoalForm(forms.ModelForm):
    class Meta:
        model = Goal
        fields = ['goal_name', 'target_amount']
        widgets = {
            'goal_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter goal name'}),
            'target_amount': forms.NumberInput(attrs={'class': 'form-control', 'placeholder': 'Target amount'}),
        }
