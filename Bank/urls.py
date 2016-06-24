"""Bank URL Configuration

from django.conf.urls import url
from django.contrib import admin
from Bank.views import *

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^bank/', BankViewSet.as_view({'get': 'list'}), name='bank'),
    url(r'^totalbalance/', BankViewSet.as_view({'get': 'total_balance'}), name='totalbalance'),
    url(r'averagebalance/', BankViewSet.as_view({'get': 'average_balance'}), name='averagebalance'),
]
