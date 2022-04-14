from django.urls import path

from . import views

app_name = 'backend'

urlpatterns = [
    path('', views.TransactionListView.as_view(), name='home'),

    path('category', views.CategoryListView.as_view(), name='category-list'),
    path('category/create', views.CategoryCreateView.as_view(), name='category-create'),
    path('category/<int:pk>', views.CategoryDetailView.as_view(), name='category-details'),
    path('category/<int:pk>/update', views.CategoryUpdateView.as_view(), name='category-update'),
    path('category/<int:pk>/delete', views.CategoryDeleteView.as_view(), name='category-delete'),
    #
    path('transaction/create', views.TransactionCreateView.as_view(), name='transaction-create'),
    path('transaction/<int:pk>', views.TransactionDetailView.as_view(), name='transaction-details'),
    path('transaction/<int:pk>/update', views.TransactionUpdateView.as_view(), name='transaction-update'),
    path('transaction/<int:pk>/delete', views.TransactionDeleteView.as_view(), name='transaction-delete'),
    #
    path('account', views.AccountListView.as_view(), name='account-list'),
    path('account/create', views.AccountCreateView.as_view(), name='account-create'),
    path('account/<int:pk>', views.AccountDetailView.as_view(), name='account-details'),
    path('account/<int:pk>/update', views.AccountUpdateView.as_view(), name='account-update'),
    path('account/<int:pk>/delete', views.AccountDeleteView.as_view(), name='account-delete'),
    #
    # path('key-store', views_keystore.KSListView.as_view(), name='keystore-list'),
    # path('key-store/add', views_keystore.KSCreateView.as_view(), name='keystore-add'),
    # path('key-store/<int:pk>', views_keystore.KSDetailView.as_view(), name='keystore-detail'),
    # path('key-store/<int:pk>/update', views_keystore.KSUpdateView.as_view(), name='keystore-update'),
    # path('key-store/<int:pk>/delete', views_keystore.KSDeleteView.as_view(), name='keystore-delete'),
    #
    # path('budget', views_budget.BudgetListView.as_view(), name='budget-list'),
    # path('budget/add', views_budget.BudgetCreateView.as_view(), name='budget-add'),
    # path('budget/<int:pk>', views_budget.BudgetDetailView.as_view(), name='budget-detail'),
    # path('budget/<int:pk>/update', views_budget.BudgetUpdateView.as_view(), name='budget-update'),
    # path('budget/<int:pk>/delete', views_budget.BudgetDeleteView.as_view(), name='budget-delete'),
    #
    # path('test', views.test, name='test'),
    # path('test-download', views_account.file_download, name="test-download"),
    path('json/<str:entity>', views.json_download, name="json-download"),
    path('json-dump', views.json_dump, name="json-dump"),

]