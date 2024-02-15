from django.contrib import admin
from .models import Transaction

@admin.register(Transaction)
class TransactionModel(admin.ModelAdmin):
    fields = ['name', 'type', 'date', 'amount', 'user', 'category']
    list_filter = []
    list_display = fields
    search_fields = ['name']