from mongoengine import *


# design database
#creat collection
class Service(Document):
    name = StringField()
    yob = IntField()
    gender = IntField()
    height = IntField()
    phone = StringField()
    address = StringField()
    status = BooleanField()
