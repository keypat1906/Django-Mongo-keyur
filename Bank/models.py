from mongoengine import *

# Create your models here.

class account(EmbeddedDocument):
    account_type = StringField(max_length=50)
    account_balance = IntField(default=0)
    currency = StringField(max_length=50)

class bank_data(Document):
    id  =StringField(max_length=50)
    first_name = StringField(max_length=50)
    last_name = StringField(max_length=50)
    accounts = ListField(EmbeddedDocumentField(account))

    meta = {
        'indexes': [
            'last_name', 
            ('first_name', '+last_name')
        ]
    }

