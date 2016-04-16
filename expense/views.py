from django.shortcuts import render
from expense.models import Transaction, Category
from expense.forms import TransactionForm, CategoryForm, MonthlyBudgetForm
from django.http import HttpResponse, HttpResponseRedirect
from expense.models import Budget
from datetime import date
import datetime

def index(request):
    user = request.user.id
    today = date.today()
    transaction_list = Transaction.objects.filter(user=user, created_at__month=today.month).order_by('-created_at')

    transactions = Transaction.objects.filter(user=user)
    category_dict = {}
    for transaction in transactions:
        if str(transaction.category) in category_dict:
            category_dict[str(transaction.category)] += transaction.amount
        else:
            category_dict[str(transaction.category)] = transaction.amount

    top_five_cat = sorted(category_dict.items(), key=lambda x: x[1], reverse=True)[:5]
    return render(request, 'expense/index.html', {'categories': transaction_list, 'top_five_cat': top_five_cat})




def transactions(request):
    user = request.user
    transactions = Transaction.objects.filter(user=user).order_by('created_at')[::-1]
    transactions_dict = {'transactions': transactions}
    return render(request, 'expense/all_transactions.html', transactions_dict)




def transactions_per_category(request):
    if request.method == "GET":
        user = request.user
        transactions = Transaction.objects.filter(user=user)
        category_dict = {}
        for transaction in transactions:
            if str(transaction.category) in category_dict:
                category_dict[str(transaction.category)] += transaction.amount
            else:
                category_dict[str(transaction.category)] = transaction.amount

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




def display_monthly_budget(request):
    user = request.user
    try:
        budget_amount = Budget.objects.get(user=user)
    except Budget.DoesNotExist:
        budget_amount = None
    if budget_amount:
        remainingamount = remaining_budget_balance(request)
    else:
        return HttpResponse("You have not set your BUDGET yet...")
    return render(request, 'expense/display_monthly_budget.html', {'budget_amount': budget_amount,'remainingamount':remainingamount})




def remaining_budget_balance(request):
    user = request.user
    today = date.today()
    of_user = Transaction.objects.filter(user=user, created_at__month=today.month)
    budget_amount = Budget.objects.get(user=user)
    #expense_budget = Transaction.objects.filter(user=user).aggregate(Sum('amount'))
    #remaining_amount = budget_amount.budget_amount - int(expense_budget['amount__sum'])

    amount_list = []
    for amount in of_user:
        amount_list.append(amount.amount)
    sum_of_all_transactions = sum(amount_list)

    if float(sum_of_all_transactions) > float(str(budget_amount)):
        return HttpResponse("You have spend more than your budget amount....",  str(sum_of_all_transactions) +  " / " + str(budget_amount))
    else:
        pass

    for date_month in of_user:
        transaction_date = date_month.created_at.date().month, date_month.created_at.date().year
        #print transaction_date
        # if current_date == transaction_date:
        #     print "yyyyyyyyyyyy"

        return (str(sum_of_all_transactions) +  " / " + str(budget_amount))






def month_year_transactions(request):
    user = request.user
    form = TransactionForm(request.GET)
    if request.method == 'GET':
        try:
            requested_month_year = Transaction.objects.filter(user=request.user)
            # print requested_month_year
            # month_and_years = {}
            # for month_year in requested_month_year:
            #print requested_month_year
            print "aaaaaa"
            requested_month_year.created_at = request.GET['arrVal']                #datetime.datetime.now().strftime("%Y-%m")
            print "bbbbbbbbbbb"
            print requested_month_year

        except:
            print "xxxxxxx"
            pass

        for transaction_month_year in requested_month_year:
            transaction = Transaction.objects.filter(user=user).order_by('-created_at')
            return render(request, 'expense/month_year_transactions.html', {'transaction': transaction})

            print transaction_month_year.created_at.strftime("%Y-%m"), transaction_month_year.amount


        for transaction_month_year in transactions:
            if present_month_year == transaction_month_year.created_at.strftime("%Y-%m"):
                #print "YES"
                return render(request, 'expense/month_year_transactions.html', {})

    else:
        form = TransactionForm()

    return render(request, 'expense/month_year_transactions.html', {'form': form})