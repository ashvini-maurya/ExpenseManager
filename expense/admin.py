from django.contrib import admin
from expense.models import Transaction, Category, User

admin.site.register(Transaction)
admin.site.register(Category)
admin.site.register(User)