from django.views import generic
from django.views.generic import edit
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.core import serializers
from django.http import JsonResponse, HttpResponse, HttpResponseBadRequest

from .models import (
    Account,
    Category,
    Transaction
)

from .forms import CategoryForm, TransactionForm, AccountForm


@method_decorator(login_required(login_url='/login/'), name='dispatch')
class CategoryCreateView(edit.CreateView):
    model = Category
    form_class = CategoryForm
    template_name = 'backend/category/create.html'


@method_decorator(login_required(login_url='/login/'), name='dispatch')
class CategoryUpdateView(edit.UpdateView):
    model = Category
    form_class = CategoryForm
    template_name = 'backend/category/update.html'


@method_decorator(login_required(login_url='/login/'), name='dispatch')
class CategoryDeleteView(edit.DeleteView):
    model = Category
    template_name = 'backend/delete-confirm.html'
    success_url ="/"


@method_decorator(login_required(login_url='/login/'), name='dispatch')
class CategoryDetailView(generic.DetailView):
    model = Category
    context_object_name = 'category'
    template_name = 'backend/category/details.html'


@method_decorator(login_required(login_url='/login/'), name='dispatch')
class CategoryListView(generic.ListView):
    model = Category
    context_object_name = "categories"
    template_name = 'backend/category/list.html'


@method_decorator(login_required(login_url='/login/'), name='dispatch')
class AccountCreateView(edit.CreateView):
    model = Account
    form_class = AccountForm
    template_name = 'backend/account/create.html'


@method_decorator(login_required(login_url='/login/'), name='dispatch')
class AccountListView(generic.ListView):
    model = Account
    context_object_name = "accounts"
    template_name = 'backend/account/list.html'


@method_decorator(login_required(login_url='/login/'), name='dispatch')
class AccountDetailView(generic.DetailView):
    model = Account
    context_object_name = 'account'
    template_name = 'backend/account/details.html'


@method_decorator(login_required(login_url='/login/'), name='dispatch')
class AccountUpdateView(edit.UpdateView):
    model = Account
    form_class = AccountForm
    template_name = 'backend/account/update.html'


@method_decorator(login_required(login_url='/login/'), name='dispatch')
class AccountDeleteView(edit.DeleteView):
    model = Account
    template_name = 'backend/delete-confirm.html'
    success_url ="/"


# @method_decorator(login_required(login_url='/login/'), name='dispatch')
class TransactionCreateView(edit.CreateView):
    model = Transaction
    form_class = TransactionForm
    template_name = 'backend/transaction/create.html'


@method_decorator(login_required(login_url='/login/'), name='dispatch')
class TransactionUpdateView(edit.UpdateView):
    model = Transaction
    form_class = TransactionForm
    template_name = 'backend/transaction/update.html'


@method_decorator(login_required(login_url='/login/'), name='dispatch')
class TransactionDetailView(generic.DetailView):
    model = Transaction
    context_object_name = 'transaction'
    template_name = 'backend/transaction/details.html'


@method_decorator(login_required(login_url='/login/'), name='dispatch')
class TransactionListView(generic.ListView):
    model = Transaction
    paginate_by = 100
    context_object_name = "transactions"
    template_name = 'backend/transaction/list.html'

    def get_queryset(self):
        return Transaction.objects.order_by('-date', '-pk')


@method_decorator(login_required(login_url='/login/'), name='dispatch')
class TransactionDeleteView(edit.DeleteView):
    model = Transaction
    template_name = 'backend/delete-confirm.html'
    success_url ="/"


# @login_required(login_url='/login/')
def json_download(request, entity):
    valid_entities = {
            'transaction': Transaction,
            'category': Category,
            'account': Account
        }
    if entity in valid_entities.keys():
        objects = valid_entities[entity].objects.all().order_by('-pk')
        objects = serializers.serialize('json', objects)        
        return HttpResponse(objects, content_type="text/json")
    else:
        return HttpResponseBadRequest()


def json_dump(request):
    transactions = []
    categories = {}
    accounts = {}

    objects = Transaction.objects.all().order_by('-date', '-pk')
    for obj in objects:
        transaction = {
            "id": obj.pk,
            "name": obj.name,
            "amount": obj.amount,
            "date": obj.date        
        }
        if obj.category.pk not in categories:
            categories[obj.category.pk] = obj.category.name

        if obj.account.pk not in accounts:
            accounts[obj.account.pk] = {
                "name": obj.account.name,
                "type": obj.account.typ
            }

        transaction["category"] = categories[obj.category.pk]
        transaction["account"] = accounts[obj.account.pk].get("name")
        transaction["account_type"] = accounts[obj.account.pk].get("type")            

        transactions.append(transaction)
    return HttpResponse({"transactions": transactions}, content_type="text/json")
