from rest_framework import serializers

class BankSerializer(serializers.Serializer):
    id  = serializers.IntegerField()
    first_name  = serializers.CharField(max_length=200)
    last_name  = serializers.CharField(max_length=200)
    account = serializers.ListField()

class AccountSerializer(serializers.Serializer):
    account_type  = serializers.CharField(max_length=200)
    account_balance  = serializers.IntegerField()
    currency  = serializers.CharField(max_length=200)
