from django.shortcuts import render
from expense.models import Transaction
from expense.forms import TransactionForm, CategoryForm, MonthlyBudgetForm
from django.http import HttpResponse
from expense.models import Budget


def index(request):
    transaction_list = Transaction.objects.all()
    context_dict = {'categories': transaction_list}
    print context_dict

    return render(request, 'expense/index.html', context_dict)


def transactions(request):
    transactions = Transaction.objects.all()
    transactions_dict = {'transactions': transactions}
    return render(request, 'expense/all_transactions.html', transactions_dict)


def add_category(request):
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            return HttpResponse("Please enter a category")
    else:
        form = CategoryForm()

    return render(request, 'expense/add_category.html', {'form': form})



def add_transaction(request):
    if request.method == 'POST':
        form = TransactionForm(request.POST)
        user = request.user

        if form.is_valid():
            transaction = form.save(commit=False)
            transaction.user = user
            transaction.save()
            return index(request)
        else:
            return HttpResponse("Please enter all entries")

    else:
        form = TransactionForm()

    return render(request, 'expense/add_transaction.html', {'form': form})


def add_monthly_budget(request):
    if request.method == 'POST':
        form = MonthlyBudgetForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            return HttpResponse("Please enter Monthly Budget!")
    else:
        form = MonthlyBudgetForm()

    return render(request, 'expense/add_monthly_budget.html', {'form': form})

