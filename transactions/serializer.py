from rest_framework import serializers
from .models import Transactions

class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transactions
        fields = ('event_id', 'transaction_uid', 'transaction_amount','original_amount','is_partial','currency_code','status',
        'description','merchant_reference_id','customer_token','customer_token','payment_method')

        








