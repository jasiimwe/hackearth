from django.urls import path
from .views import *

app_name = 'transactions'
urlpatterns = [
    path('all_transactions/', get_all_transactions),
    path('create_transactions/', create_transaction),
    
]
