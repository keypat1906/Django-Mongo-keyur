#from Bank.serializers import *
from rest_framework import viewsets
from rest_framework.response import Response
from models import *
import mongoengine
#Establish a connection with mongo instance.

#user = authenticate(username=username, password=password)
#assert isinstance(user, mongoengine.django.auth.User)


class BankViewSet(viewsets.ViewSet):
    """
    A simple ViewSet for listing or retrieving users.
    """
    def list(self, request):
        list = []
        bank = bank_data.objects(first_name__contains="JOHN")
        for object in bank:
            list.append(object.last_name)
     
        return Response(data=list)

    def retrieve(self, request, pk=None):
        queryset = Bank.objects.all()
        #user = get_object_or_404(queryset, pk=pk)
        serializer = BankSerializer(queryset)
        return Response(serializer.data)


    def total_balance(self, request, pk=None):
        bank = bank_data.objects.all()
        total = 0
        for object in bank:
            if object.accounts:
               for balance in object.accounts:
                   if balance.account_balance:
                      total = total + balance.account_balance
        return Response(data=total)   
# Create your views here.

def index(request):
    customer  = Bank.objects.all()
