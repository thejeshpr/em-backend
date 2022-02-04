import datetime

from django import forms
from django.forms import ModelForm
from django.utils import timezone

from .models import Category, Transaction, Account


class CategoryForm(ModelForm):
    class Meta:
        model = Category
        fields = [
            'name',
        ]


class TransactionForm(ModelForm):
    class Meta:
        model = Transaction
        fields = [
            'name',
            'amount',
            'account',
            'date',
            'category',
            'tran_type',
        ]

    date = forms.DateField(
        # input_formats=['%d/%m/%Y'],
        initial=datetime.date.today
    )


class AccountForm(ModelForm):
    class Meta:
        model = Account
        fields = [
            'name',
            'typ',
        ]
