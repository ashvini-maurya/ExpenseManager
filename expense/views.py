from django.shortcuts import render
from expense.models import Transaction

def index(request):
    transaction_list = Transaction.objects.all()
    context_dict = {'categories': transaction_list}
    return render(request, 'expense/index.html', context_dict)