from mongoengine import *


# design database
#creat collection
class Video(Document):
    title = StringField()
    thumbnail = StringField()
    view = IntField()
    youtube_id = StringField()
    link = StringField()
