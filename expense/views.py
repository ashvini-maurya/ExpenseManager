from django.shortcuts import render
from expense.models import Transaction, Category
from expense.forms import TransactionForm, CategoryForm, MonthlyBudgetForm
from django.http import HttpResponse, HttpResponseRedirect
from expense.models import Budget
#import datetime
#import time
from django.shortcuts import get_object_or_404
from django.http import Http404



def index(request):
    transaction_list = Transaction.objects.all()
    context_dict = {'categories': transaction_list}
    return render(request, 'expense/index.html', context_dict)


def transactions(request):
    user = request.user
    transactions = Transaction.objects.filter(user=user)
    transactions_dict = {'transactions': transactions}

    return render(request, 'expense/all_transactions.html', transactions_dict)



def transactions_per_category(request):
    if request.method == "GET":
        user = request.user
        transactions = Transaction.objects.filter(user=user)
        category_dict = {}
        for transaction in transactions:
            if transaction.category in category_dict:
                category_dict[str(transaction.category)] += transaction.amount
            else:
                category_dict[str(transaction.category)] = transaction.amount
        #print category_dict

        return render(request, 'expense/transactions_per_category.html', {'category': category_dict, 'transactions': transactions})



def add_category(request):

    if request.method == 'POST':
        try:
            cat = Category.objects.filter(name=request.POST['name'])
            if(cat):
                return HttpResponse("category already exists")
        except :
           pass
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
    form = MonthlyBudgetForm()
    if request.method == 'POST':
        try:
            getbudget=Budget.objects.get(user=request.user)
            getbudget.budget_amount=request.POST['budget_amount']
            if float(getbudget.budget_amount) > 0:
                getbudget.save()
            else:
                return HttpResponse("Please set your budget amount greater than ZERO!")
            return HttpResponseRedirect('/expense/')
        except:
            form = MonthlyBudgetForm(request.POST)
            user = request.user
            if form.is_valid():
                budget = form.save(commit=False)
                budget.user = user
                budget.save()
                return index(request)
            else:
                return HttpResponse("Please enter Monthly Budget!")
    else:
        form = MonthlyBudgetForm()
    return render(request, 'expense/add_monthly_budget.html', {'form': form})















#
# def get_obj_or_404(transaction, *args, **kwargs):
#     try:
#         return transaction.objects.get(*args, **kwargs)
#     except transaction.DoesNotExist:
#         raise Http404



def display_monthly_budget(request):
    user = request.user
    try:
        budget_amount = Budget.objects.get(user=user)
        #print budget_amount
    except Budget.DoesNotExist:
        budget_amount = None

    #budget_amount = get_object_or_404(Budget, user=user)

    remainingamount = remaining_budget_balance(request)
    #remainingamount = get_obj_or_404(remaining_budget_balance, user=user)
    #print remainingamount

    return render(request, 'expense/display_monthly_budget.html', {'budget_amount': budget_amount,'remainingamount':remainingamount})



def remaining_budget_balance(request):
    user = request.user
    #current_date = datetime.datetime.now().date().month, datetime.datetime.now().date().year
    #print current_date

    #print current_date_month
    of_user = Transaction.objects.filter(user=user)

    budget_amount = Budget.objects.get(user=user)
    #expense_budget = Transaction.objects.filter(user=user).aggregate(Sum('amount'))
    #remaining_amount = budget_amount.budget_amount - int(expense_budget['amount__sum'])

    amount_list = []
    for amount in of_user:
        amount_list.append(amount.amount)
    sum_of_all_transactions = sum(amount_list)

    for date_month in of_user:
        #transaction_date = date_month.created_at.date().month, date_month.created_at.date().year
        # print transaction_date
        #if current_date == transaction_date:
            #print "yyyyyyyyyyyy"

        return (str(sum_of_all_transactions) +  " / " + str(budget_amount))

















    # try:
    #     budget_amount = Budget.objects.get(user=user)
    #     #print(budget_amount)
    #     #expense_budget=Transaction.objects.filter(user=user).aggregate(Sum('amount'))
    #
    #
    #
    #     # print transaction
    #
    #     #print(expense_budget)
    #
    #     expense_budget = Transaction.objects.filter(user=user).aggregate(Sum('amount'))
    #
    #     remaining_amount = budget_amount.budget_amount - int(expense_budget['amount__sum'])
    #
    #
    #
    #
    #     # if remaining_amount > budget_amount:
    #     #     print "Your expenses are more than your budget amount."
    #
    #
    #
    #     #print remaining_amount
    #
    #     return remaining_amount
    # except Exception as d:
    #     print(d)