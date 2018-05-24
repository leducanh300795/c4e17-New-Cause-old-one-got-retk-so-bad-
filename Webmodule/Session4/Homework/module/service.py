from mongoengine import * #StringField, IntField, BooleanField, Document

# Design database
    # Create collection
class Service(Document):
    image = StringField()
    name = StringField()
    yob = IntField()
    gender = IntField()
    email = StringField()
    height = IntField()
    measurements = ListField()
    phone = StringField()
    description = ListField()
    address = StringField()
    job = StringField()
    company = StringField()
    status = BooleanField()
