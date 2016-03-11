from django import forms
from expense.models import Transaction, Category

class TransactionForm(forms.ModelForm):
    amount = forms.IntegerField()
    comment = forms.CharField()
    category = forms.ModelChoiceField(queryset=Category.objects.all())
    user_id = forms.IntegerField()

    class Meta:
        model = Transaction
        fields = ('category',)


class CategoryForm(forms.ModelForm):
    name = forms.CharField()

    class Meta:
        model = Category
        exclude = ('name', )
