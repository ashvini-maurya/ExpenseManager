from django import forms
from expense.models import Transaction, Category, Budget

class TransactionForm(forms.ModelForm):
    amount = forms.IntegerField(label='amount',
                                widget=forms.TextInput(attrs={'placeholder': 'Amount'}))

    comment = forms.CharField(label='comment',
                                widget=forms.TextInput(attrs={'placeholder': 'Comment'}))

    category = forms.ModelChoiceField(queryset=Category.objects.all())


    class Meta:
        model = Transaction
        exclude = ('user',)

class CategoryForm(forms.ModelForm):
    name = forms.CharField(required=True)

    class Meta:
        model = Category
        fields = ('name', )

class MonthlyBudgetForm(forms.ModelForm):
    budget_amount = forms.FloatField(required=True)

    class Meta:
        model = Budget
        exclude = ('user',)
