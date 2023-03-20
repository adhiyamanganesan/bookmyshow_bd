from flask import *
from flask.views import View
from flask_appbuilder import ModelView
from flask_appbuilder.models.mongoengine.interface import MongoEngineInterface
from flask_appbuilder.api import *
from flask_appbuilder.security.api import *
from .models import *
from .urls import *
from config import *

def resister_view():
    firstname = request.form["firstname"]
    lastname = request.form["lastname"]
    password = request.form["password"]
    mobile_no = request.form["mobile_no"]
    email = request.form["email"]
    data = myuser(
        firstname = firstname,
        lastname = lastname,
        password = password,
        mobile_no = mobile_no,
        email = email,
    )
    data.save()
    return {"message":"your successfully register"}

def login_view():
    email = request.form["email"]
    password = request.form["password"]
    user = myuser.objects(email=email,password=password).first()
    data={
        "user_id":user.id,
        "name": user.firstname
    }
    if user:
        return {"message":"your successfully login"}
    else:
        return {"message":"plz enter the correct data"}

def ticket_booking(user_id):
    movie_name = request.form["movie_name"]
    ticket_price = 100
    ticket_number = str(request.form["ticket_number"])
    no_of_ticket = request.form["no_of_ticket"]
    
    x = ticket_number.split(",")
    print(x)
    user = myuser.objects(id=user_id).first()
    
    data = ticket_history(
        movie_name = movie_name,
        ticket_price = ticket_price,
        ticket_number = x,
        no_of_ticket = no_of_ticket,
        total_ticket_price = int(ticket_price) * int(no_of_ticket),
        status = "Booked"
    )
    user.ticket.append(data)
    user.save()
    return {"message":"successfully booked"}

def cancel_ticket():
    movie_name = request.form["movie_name"]
    ticket_number = request.form["ticket_number"]
    ticket = ticket_history.objects(movie_name=movie_name,ticket_number=ticket_number).first()
    ticket.update(status="cancelled")
    ticket.save()
    return {"message":"your ticket succesfully cancelled"}

def history(user_id):
    user = myuser.objects(id=user_id).first()
    data_list = []
    for i in user.ticket:
        data = {
            "movie_name" : i.movie_name,
            "ticket_price" : i.ticket_price,
            "ticket_number" : i.ticket_number,
            "total_ticket" : i.total_ticket,
            "no_of_ticket" : i.no_of_ticket,
            "status" : i.status
        }
        data_list.append(data)
    return data_list

def cancel_ticket(user_id):
    user = myuser.objects(id=user_id).first()
    movie_name = request.form["movie_name"]
    ticket_number = request.form["ticket_number"]
    for i in user.ticket:
        if i.movie_name == movie_name and i.ticket_number == ticket_number:
            i.status = "cancel"
            user.save()
    return "succefully cancelled"

def seating_details():
    user=myuser.objects.all()
    print(user)
    data = []
    for i in user:
        for j in i.ticket:
            for k in j.ticket_number:
                data.append(k)
    return data

######################################## admin ###################################################

def admin_reg():
    firstname = request.form["firstname"]
    lastname = request.form["lastname"]
    password = request.form["password"]
    mobile_no = request.form["mobile_no"]
    email = request.form["email"]
    data = admin_user(
        firstname = firstname,
        lastname = lastname,
        password = password,
        mobile_no = mobile_no,
        role = "admin",
        email = email,
    )
    data.save()
    return {"message":"your successfully register"}

def theatre_details(user_id):
    json_data = request.get_json()
    admin_users = admin_user.objects(id=user_id).first()
    data = theatre_detail(
        id=ObjectId(),
        screen_name = json_data["screen_name"],
        pathway = json_data['pathway'],
        
    )
    data.seating_details.append(json_data['seating_details'])
    admin_users.theatre_details.append(data)
    admin_users.save()
    return {"message":"Theatre Details saved succefully"}

def theatre_details_show(user_id = None):
    user = admin_user.objects(id=user_id).first()
    data = []
    d = []
    for i in user.theatre_details:
        t_data = {
            "id":str(i.id),
            "screen_name":i.screen_name,
            "pathway":i.pathway,
            "seating_details":i.seating_details
        }
        d.append(t_data)
    detail = {
        "id":str(user.id),
        "firstname":user.firstname,
        "lastname":user.lastname,
        "password":user.password,
        "mobile_no":user.mobile_no,
        "email":user.email,
        "role":user.role,
        "theatre_details" : d
    }
    data.append(detail)
    return data

def edit_admin_user(user_id):
    user = admin_user.objects(id=user_id).first()
    firstname = request.form["firstname"]
    lastname = request.form["lastname"]
    password = request.form["password"]
    mobile_no = request.form["mobile_no"]
    email = request.form["email"]
    
    data = {
        "firstname" :firstname,
        "lastname" :lastname,
        "password" : password,
        "mobile_no" : mobile_no,
        "email" : email
    }
    
    for key, value in data.items():
        if value not in ["null", "undefined", None, ["null"], ""]:
            admin_user.objects(id=user_id).update(**{"set__" + key: value})
    return {"mesaage":"your data successfully update"}