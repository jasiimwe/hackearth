from django.urls import path
from .views import *

app_name = 'transactions'
urlpatterns = [
    path('all_transactions/', get_all_transactions),
    path('create_transactions/', create_transaction),
# <<<<<<< HEAD
    path('get_transaction_event/<str:event_uid>/', get_all_transactions_event),
# =======
    path('update_transaction/<str:uid>/', update_transaction),
    path('get_transaction/<str:uid>/', get_transaction),
    path('delete_transaction/<str:uid>/', delete_transaction),
# >>>>>>> d15af503137f15f080b313a19af07597e80eebfd
    
]
