from django.shortcuts import render
from expense.models import Transaction
from expense.forms import TransactionForm

def index(request):
    transaction_list = Transaction.objects.all()
    context_dict = {'categories': transaction_list}
    user_id = request.user.id
    print user_id

    return render(request, 'expense/index.html', context_dict)


def add_transaction(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)

        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            return form.errors

    else:
        form = TransactionForm()

    return render(request, 'expense/add_transaction.html', {'form': form})