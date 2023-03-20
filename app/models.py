from mongoengine import *
from flask_appbuilder.security.mongoengine.models import *
from bson.objectid import ObjectId
from mongoengine import document
from mongoengine.fields import *
from mongoengine.document import *
from app import db

class ticket_history(EmbeddedDocument):
    movie_name = StringField()
    ticket_price = IntField()
    ticket_number = ListField()
    total_ticket_price = IntField()
    status = StringField()
    no_of_ticket = StringField()

class myuser(Document):
    firstname = StringField()
    lastname = StringField()
    password = StringField()
    mobile_no = StringField()
    email = StringField()
    ticket = ListField(EmbeddedDocumentField(ticket_history))

class theatre_detail(EmbeddedDocument):
    id = ObjectIdField()
    screen_name=StringField()
    pathway = StringField()
    seating_details = ListField()

class admin_user(Document):
    firstname = StringField()
    lastname = StringField()
    password = StringField()
    mobile_no = StringField()
    email = StringField()
    role = StringField()
    theatre_details = ListField(EmbeddedDocumentField(theatre_detail))