from django.urls import path
from .views import create_transaction

app_name = 'transactions'
urlpatterns = [
    path('all_transactions/', get_all_transactions),
    path('create_transaction', create_transaction),
    
]
