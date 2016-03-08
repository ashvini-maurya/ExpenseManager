from django import forms
from expense.models import Transaction

class TransactionForm(forms.ModelForm):
    amount = forms.IntegerField
    comment = forms.CharField
    category = forms.CharField

    class Meta:
        model = Transaction
        fields = ('category',)