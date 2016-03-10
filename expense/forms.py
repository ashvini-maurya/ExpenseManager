from django import forms
from expense.models import Transaction, Category



class CategoryForm(forms.ModelForm):
    name = forms.CharField()

    class Meta:
        model = Category
        fields = ('name', )


class TransactionForm(forms.ModelForm):
    amount = forms.FloatField()
    comment = forms.CharField()
    category = forms.CharField()
    user_id = forms.IntegerField()

    class Meta:
        model = Transaction
        fields = ('amount', 'comment', 'category', 'user_id')