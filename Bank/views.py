from rest_framework import viewsets
from rest_framework.response import Response
from models import *
import mongoengine

class BankViewSet(viewsets.ViewSet):


    def list(self, request):
        """
        A simple ViewSet for listing or retrieving users.
        """
        list = []
        bank = bank_data.objects(first_name__contains="JOHN")
        for object in bank:
            list.append(object.last_name)
     
        return Response(data=list)

    def total_balance(self, request, pk=None):
        """
        A simple ViewSet for calculating total balance of all the \
                                                  account holders.
        """
        pipe = {"$unwind": "$accounts"}, 
               {"$group": {"_id": "null", 
                "sum": {"$sum": "$accounts.account_balance"}}}
        total_balance = bank_data._get_collection().aggregate(pipe)\
                        ["result"][0]["sum"]
        return Response(data=total_balance)

    def average_balance(self, request, pk=None):
        """
        A simple ViewSet for calculating average balance of all \
                                           the account holders.
        """
        pipe = {"$unwind": "$accounts"},
               {"$group": {"_id": "null",
                "avg": {"$avg": "$accounts.account_balance"}}}
        average_balance = bank_data._get_collection().aggregate(pipe)\
                          ["result"][0]["avg"]
        return Response(data=average_balance)
