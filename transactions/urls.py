from django.urls import path
from .views import *

app_name = 'transactions'
urlpatterns = [
    path('all_transactions/', get_all_transactions),
    path('create_transactions/', create_transaction),
    path('update_transaction/<str:uid>/', update_transaction),
    path('get_transaction/<str:uid>/', get_transaction),
    path('delete_transaction/<str:uid>/', delete_transaction),
    
]
