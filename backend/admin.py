# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import Category, Account, Transaction


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
    search_fields = ('name',)


@admin.register(Account)
class AccountAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'typ')
    search_fields = ('name',)


@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'created_at',
        'updated_at',
        'account',
        'amount',
        'category',
        'date',
        'tran_type',
        'name',
    )
    list_filter = ('created_at', 'updated_at', 'account', 'category', 'date')
    search_fields = ('name',)
    date_hierarchy = 'created_at'