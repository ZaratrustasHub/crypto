from django.contrib import admin
from bank.models import customer, TransactionHistory

admin.site.register(customer)
admin.site.register(TransactionHistory)
