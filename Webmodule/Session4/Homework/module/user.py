from mongoengine import *

class User(Document):
    name = StringField()
    email = StringField()
    idsignin = StringField()
    password = StringField()
