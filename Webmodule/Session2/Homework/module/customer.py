from mongoengine import *


# design database
#creat collection
class Customers(Document):
    name = StringField()
    gender = IntField()
    email = StringField()
    phone_number = StringField()
    job = StringField()
    company = StringField()
    contacted = BooleanField()
