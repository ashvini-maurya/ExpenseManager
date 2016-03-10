from django.shortcuts import render
from expense.models import Transaction
from expense.forms import TransactionForm, CategoryForm
from django.http import HttpResponse

def index(request):
    transaction_list = Transaction.objects.all()
    context_dict = {'categories': transaction_list}
    user_id = request.user.id
    print user_id

    return render(request, 'expense/index.html', context_dict)


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

        print type(request.POST['category'])           # check the type category form

        form = TransactionForm(request.POST)


        form.fields["category"].queryset = Transaction.objects.filter(category)




        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            return HttpResponse("Please enter all entries")

    else:
        form = TransactionForm()

    return render(request, 'expense/add_transaction.html', {'form': form})