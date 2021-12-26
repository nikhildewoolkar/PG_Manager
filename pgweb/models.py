from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import *
from django.db.models.signals import post_save
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import *
from django.db.models.signals import post_save

class UserProfile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    usernames=models.CharField(max_length=200)
    phoneno=models.CharField(max_length=150)
    pemail=models.EmailField(max_length=254)
    address=models.CharField(max_length=500)
    city=models.CharField(max_length=500)
    taluka=models.CharField(max_length=500)
    district=models.CharField(max_length=500)
    state=models.CharField(max_length=500)
    pincode=models.CharField(max_length=500)
    dob=models.CharField(max_length=500)
    desc=models.CharField(max_length=1000)
    password=models.CharField(max_length=1000)
    def __str__(self):  # __str__
        return (self.user.username)

class Newsletter(models.Model):
    email=models.CharField(max_length=200)

class Contact(models.Model):
    name=models.CharField(max_length=150)
    email=models.EmailField(max_length=254)
    type=models.CharField(max_length=500)
    sub=models.CharField(max_length=500)
    msg=models.CharField(max_length=1000)
    
class Blog(models.Model):
    bid=models.CharField(max_length=150)
    sub=models.CharField(max_length=150)
    text=models.CharField(max_length=500)
    username=models.CharField(max_length=500)
    datetime=models.CharField(max_length=1000)

class Advertisement(models.Model):
    aid=models.CharField(max_length=150)
    sub=models.CharField(max_length=150)
    text=models.CharField(max_length=500)
    username=models.CharField(max_length=500)
    datetime=models.CharField(max_length=1000)
    link=models.CharField(max_length=1000)

class Pgdata(models.Model):
    owner=models.CharField(max_length=150)
    phoneno=models.CharField(max_length=150)
    pemail=models.EmailField(max_length=254)
    address=models.CharField(max_length=500)
    uid=models.CharField(max_length=150)
    city=models.CharField(max_length=500)
    taluka=models.CharField(max_length=500)
    district=models.CharField(max_length=500)
    state=models.CharField(max_length=500)
    pincode=models.CharField(max_length=500)
    desc=models.CharField(max_length=150)
    link=models.CharField(max_length=500)
    bhk=models.CharField(max_length=500)
    nopeople=models.CharField(max_length=500)
    vacancies=models.CharField(max_length=500)
    furnished=models.CharField(max_length=150)
    accomodation=models.CharField(max_length=500)
    bachelor=models.CharField(max_length=500)
    ac=models.CharField(max_length=500)
    geyser=models.CharField(max_length=500)
    smoking=models.CharField(max_length=500)
    drink=models.CharField(max_length=500)
    vegnonveg=models.CharField(max_length=500)
    washingmachine=models.CharField(max_length=500)