from django.shortcuts import render,redirect
from django.contrib import messages
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash
from django.core.exceptions import ObjectDoesNotExist
import datetime
import os
from django.conf import settings
from django.core.mail import send_mail 
import numpy as np
from django.contrib import messages
from subprocess import check_output, CalledProcessError,STDOUT
from django.contrib.auth.models import User, auth
from django.http import HttpResponse, request
# from .models import 
from .models import UserProfile,Newsletter,Contact,Blog,Advertisement,Pgdata

def home(request):
    return render(request,"home.html")
def rentpg(request):
    return render(request,"rentpg.html")
def search(request):
    if request.method=="POST":
        id=request.POST.get("id")
        key=request.POST.get("key")
        if(id=="city"):
            n=Pgdata.objects.filter(city=key)
            return render(request,"search.html",{'n':n})
        elif(id=="taluka"):
            n=Pgdata.objects.filter(taluka=key)
            return render(request,"search.html",{'n':n})
        elif(id=="district"):
            n=Pgdata.objects.filter(district=key)
            return render(request,"search.html",{'n':n})
        elif(id=="state"):
            n=Pgdata.objects.filter(state=key)
            return render(request,"search.html",{'n':n})
        elif(id=="pincode"):
            n=Pgdata.objects.filter(pincode=key)
            return render(request,"search.html",{'n':n})
        else:
            n=reversed(Pgdata.objects.all())
            return render(request,"search.html",{'n':n})
    n=reversed(Pgdata.objects.all())
    return render(request,"search.html",{'n':n})

def advsearch(request):
    if request.method=="POST":
        d1=request.POST.get("bhk")
        d2=request.POST.get("furnished")
        d3=request.POST.get("accomodation")
        d4=request.POST.get("bachelor")
        d5=request.POST.get("ac")
        d6=request.POST.get("geyser")
        d7=request.POST.get("smoking")
        d8=request.POST.get("drink")
        d9=request.POST.get("vegnonveg")
        d10=request.POST.get("washingmachine")
        n=Pgdata.objects.filter(bhk=d1,furnished=d2,accomodation=d3,bachelor=d4,ac=d5,geyser=d6,smoking=d7,drink=d8,vegnonveg=d9,washingmachine=d10)
        return render(request,"advsearch.html",{'n':n})
    n=reversed(Pgdata.objects.all())
    return render(request,"advsearch.html",{'n':n})
def listpg(request):
    return render(request,"listpg.html")
def crudpg(request):
    p1=request.user
    id=0
    if request.method=="POST":
        n = Pgdata.objects.filter(owner=p1.username)    
        id=int(request.POST.get("id"))
        return render(request,"crudpg.html",{"id":id,'n':n})
    return render(request,"crudpg.html",{"id":id})
def addpg(request):
    id=2
    p1=request.user
    if request.method=="POST":
        uid=request.POST.get("uid")
        #owner,phoneno,pemail,address,city,taluka,district,state,pincode,desc,link,bhk,nopeople,vacancies,furnished,accomodation,bachelor,ac,geyser,smoking,drink,vegnonveg,washingmachine
        owner=request.POST.get("owner")
        phoneno=request.POST.get("phoneno")
        pemail=request.POST.get("pemail")
        address=request.POST.get("address")
        city=request.POST.get("city")
        taluka=request.POST.get("taluka")
        district=request.POST.get("district")
        state=request.POST.get("state")
        pincode=request.POST.get("pincode")
        desc=request.POST.get("desc")
        link=request.POST.get("link")
        bhk=request.POST.get("bhk")
        nopeople=request.POST.get("nopeople")
        vacancies=request.POST.get("vacancies")
        furnished=request.POST.get("furnished")
        accomodation=request.POST.get("accomodation")
        bachelor=request.POST.get("bachelor")
        ac=request.POST.get("ac")
        geyser=request.POST.get("geyser")
        smoking=request.POST.get("smoking")
        drink=request.POST.get("drink")
        vegnonveg=request.POST.get("vegnonveg")
        washingmachine=request.POST.get("washingmachine")
        if Pgdata.objects.filter(uid=uid).exists():
            return render(request,"crudpg.html",{"id":id})
        else:
            t=Pgdata(uid=uid,owner=owner,phoneno=phoneno,pemail=pemail,address=address,city=city,taluka=taluka,district=district,state=state,pincode=pincode,desc=desc,link=link,bhk=bhk,nopeople=nopeople,vacancies=vacancies,furnished=furnished,accomodation=accomodation,bachelor=bachelor,ac=ac,geyser=geyser,smoking=smoking,drink=drink,vegnonveg=vegnonveg,washingmachine=washingmachine)
            t.save()
            messages.info(request,'PG added')
            return render(request,"crudpg.html",{"id":id})
    return render(request,"crudpg.html",{"id":id})
def delpg(request):
    p1=request.user
    n=Pgdata.objects.filter(owner=p1.username)
    id=4
    if request.method == "POST":
        uid=request.POST.get("id")
        Pgdata.objects.filter(uid=uid).delete()
        messages.info(request,'PG Deleted')
        return render(request,"crudpg.html",{"id":id,'n':n,})
    return render(request,"crudpg.html",{"id":id,'n':n,})
def uppg(request):
    id=3
    p1=request.user
    n=Pgdata.objects.filter(owner=p1.username)
    if request.method=="POST":
        uid=request.POST.get("uid")
        owner=request.POST.get("owner")
        phoneno=request.POST.get("phoneno")
        pemail=request.POST.get("pemail")
        address=request.POST.get("address")
        city=request.POST.get("city")
        taluka=request.POST.get("taluka")
        district=request.POST.get("district")
        state=request.POST.get("state")
        pincode=request.POST.get("pincode")
        desc=request.POST.get("desc")
        link=request.POST.get("link")
        bhk=request.POST.get("bhk")
        nopeople=request.POST.get("nopeople")
        vacancies=request.POST.get("vacancies")
        furnished=request.POST.get("furnished")
        accomodation=request.POST.get("accomodation")
        bachelor=request.POST.get("bachelor")
        ac=request.POST.get("ac")
        geyser=request.POST.get("geyser")
        smoking=request.POST.get("smoking")
        drink=request.POST.get("drink")
        vegnonveg=request.POST.get("vegnonveg")
        washingmachine=request.POST.get("washingmachine")
        Pgdata.objects.filter(uid=uid).update(uid=uid,owner=owner,phoneno=phoneno,pemail=pemail,address=address,city=city,taluka=taluka,district=district,state=state,pincode=pincode,desc=desc,link=link,bhk=bhk,nopeople=nopeople,vacancies=vacancies,furnished=furnished,accomodation=accomodation,bachelor=bachelor,ac=ac,geyser=geyser,smoking=smoking,drink=drink,vegnonveg=vegnonveg,washingmachine=washingmachine)
        messages.info(request,'PG Updated')
        return render(request,"crudpg.html",{"id":id,'n':n})
    return render(request,"crudpg.html",{"id":id,'n':n})
def about(request):
    return render(request,"about.html")
def contact(request):
    if request.method=='POST':
        g=0
        name=request.POST.get("name")
        email=request.POST.get("email")
        subject=request.POST.get("subject")
        message=request.POST.get("message")
        c=Contact(name=name,email=email,sub=subject,msg=message)
        c.save()
        try:
            subject = 'Query/Suggestion Received'  
            message = f'Hi{name}--{email},Your response is received by PGmanager app.We will reply as soon as possible.'
            email_from = settings.EMAIL_HOST_USER 
            recipient_list = [email] 
            send_mail( subject, message, email_from, recipient_list ,fail_silently=False)
            messages.info(request,'Query/Feedback Submitted.we will reply you soon.')
        except:
            messages.info(request,'Query/Feedback Submitted.we will reply you soon.')
        return render(request,"contact.html",{"g":g}) 
    return render(request,"contact.html")
def signup(request):
    if request.method=='POST':
        first_name=request.POST.get("fname")
        last_name=request.POST.get("lname")
        email=request.POST.get("email")
        username=email
        pemail=request.POST.get("pemail")
        mobno=request.POST.get("phoneno")
        add=request.POST.get("add")
        city=request.POST.get("city")
        taluka=request.POST.get("taluka")
        district=request.POST.get("district")
        state=request.POST.get("state")
        pin=request.POST.get("pin")
        dob=request.POST.get("dob")
        desc=request.POST.get("desc")
        password=request.POST.get("pass")
        password1=request.POST.get("pass1")
        def password_check(password):
            SpecialSym =['$', '@', '#', '%'] 
            val = True
            if len(password) < 8:
                print('length should be at least 6') 
                val = False
            if len(password) > 20: 
                print('length should be not be greater than 8') 
                val = False
            if not any(char.isdigit() for char in password): 
                print('Password should have at least one numeral') 
                val = False
            if not any(char.isupper() for char in password): 
                print('Password should have at least one uppercase letter') 
                val = False
            if not any(char.islower() for char in password): 
                print('Password should have at least one lowercase letter') 
                val = False
            if not any(char in SpecialSym for char in password): 
                print('Password should have at least one of the symbols $@#') 
                val = False
            if val == False: 
                val=True
                return val
        if (password_check(password)): 
            print("y")
        else: 
            print("x")                 
        if password==password1:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username taken')
                return redirect('signup')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'email taken')
                return redirect('signup')
            elif (password_check(password)):
                messages.info(request,'password is not valid(must be combination of (A-Z,a-z,@,1-9))')
                return redirect('signup')
            else:
                user=User.objects.create_user(username=username,password=password,email=email,first_name=first_name,last_name=last_name)
                user.save()
                messages.info(request,"user created succesfully")
                user=auth.authenticate(username=username,password=password)
                if user is not None:
                   auth.login(request,user)
                u = User.objects.get(username=username)
                reg=UserProfile(user=u,usernames=username,pemail=pemail,phoneno=mobno,address=add,dob=dob,pincode=pin,taluka=taluka,state=state,district=district,desc=desc,password=password,city=city)
                reg.save()
                auth.logout(request)
        else:
            messages.info(request,"password not matching")
            return redirect('signup')
        return redirect('login')
    return render(request,"signup.html")
def login(request):
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get("pwd")
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            p1=request.user
            return redirect('/')
        else:
            messages.info(request,"Invalid Credentials")
            return redirect('login')
    return render(request,"login.html")
def logout(request):
    auth.logout(request)
    return render(request,"login.html")


def profile(request):
    if request.method=="POST":
        id=int(request.POST.get("id"))    
        return render(request,"profile.html",{"id":id})
    else:
        id=0
        return render(request,"profile.html",{"id":id})

def editprofile(request):
    id=2
    if request.method=="POST":
        u=request.user
        fname=request.POST.get("fname")
        lname=request.POST.get("lname")
        email=request.POST.get("email")
        username=email
        pemail=request.POST.get("pemail")
        mobno=request.POST.get("phoneno")
        add=request.POST.get("add")
        city=request.POST.get("city")
        taluka=request.POST.get("taluka")
        district=request.POST.get("district")
        state=request.POST.get("state")
        pin=request.POST.get("pin")
        dob=request.POST.get("dob")
        desc=request.POST.get("desc")
        password=request.POST.get("pass")
        password1=request.POST.get("pass1")
        User.objects.filter(username=username).update(first_name=fname,last_name=lname)
        UserProfile.objects.filter(usernames=username).update(user=u,usernames=username,pemail=pemail,phoneno=mobno,address=add,dob=dob,pincode=pin,taluka=taluka,state=state,district=district,desc=desc,city=city)
        messages.info(request,"Profile Updated Properly")
        return render(request,"profile.html",{"id":id})
    return render(request,"profile.html",{"id":id})

def changepassword(request):
    id=3
    if request.method == 'POST':
        old=request.POST.get("old")
        new1=request.POST.get("new1")
        new2=request.POST.get("new2")
        def passwordcheck(password):
            SpecialSym =['$', '@', '#', '%'] 
            val = True
            if len(password) < 8:
                print('length should be at least 8') 
                val = False
            if len(password) > 20: 
                print('length should be not be greater than 20') 
                val = False
            if not any(char.isdigit() for char in password): 
                print('Password should have at least one numeral') 
                val = False
            if not any(char.isupper() for char in password): 
                print('Password should have at least one uppercase letter') 
                val = False
            if not any(char.islower() for char in password): 
                print('Password should have at least one lowercase letter') 
                val = False
            if not any(char in SpecialSym for char in password): 
                print('Password should have at least one of the symbols $@#') 
                val = False
            return val
        p=request.user
        u1 = UserProfile.objects.get(usernames=p.username)
        if(u1.password==old):
            if(new1==new2):
                password=new1
                if(passwordcheck(password)==True):
                    u = User.objects.get(username=p.username)
                    u.set_password(new1)
                    u.save()
                    UserProfile.objects.filter(usernames=p.username).update(password=new1)
                    messages.info(request,"password Changed succesfully.Login using new Password.")
                    return redirect('logout')
                else:
                    messages.info(request,"Password should contain(0-9,a-z,A-Z,@)")
                    id=3
                    return render(request,"profile.html",{"id":id})    
            else:
                messages.info(request,"Password Don't Match")
                id=3
                return render(request,"profile.html",{"id":id})
        else:
            messages.info(request,"Old Password is not Correct or error occured.")
            id=3
            return render(request,"profile.html",{"id":id})
    id=3
    return render(request,"profile.html",{"id":id})

def resendpass(request):
    if request.method == 'POST':
        fname=request.POST.get("fname")
        lname=request.POST.get("lname")
        username=request.POST.get("email")
        phoneno=request.POST.get("phoneno")
        u=1
        try:
            p=User.objects.get(username=username)
            pa=UserProfile.objects.get(usernames=username)
        except:
            u=0
        if(u==1):
            password=pa.password
            if(fname == p.first_name and lname == p.last_name and phoneno ==pa.phoneno):
                print(0)
                try:
                    print(2)
                    subject = 'Forget Password(Resend)'   
                    message = f'Hi {p.username},your password for the PGmanagaer app {password}. try logging in once again and change the password.'
                    email_from = settings.EMAIL_HOST_USER 
                    recipient_list = [p.email] 
                    send_mail( subject, message, email_from, recipient_list ,fail_silently=False)
                    messages.info(request,"password has been sent to your registered email address,kindly check.")
                except:
                    print(1)
                    messages.info(request,"sorry for inconvenience.email sending fail. kindly send query on conact page with proper subject and text.we will contact you soon..")
            else:
                messages.info(request,"Entered incorrect information.Try using correct credentials.")
            return render(request,"resendpass.html")
        else:
            messages.info(request,"User is not registered.kindly go to signup page and register.")
            return render(request,"login.html")
        return render(request,"login.html")
    return render(request,"resendpass.html")

def blogadv(request):
    d2=reversed(Advertisement.objects.all())
    d1=reversed(Blog.objects.all())
    return render(request,"blogadv.html",{'d1':d1,'d2':d2})
def newsletter(request):
    if request.method=="POST":
        g=1
        email=request.POST.get("email")
        d=Newsletter.objects.all()
        for d in d:
            if(email == d.email):
                messages.info(request,"Email already present in Newsletter database.")
                break
        else:
            wo=Newsletter(email=email)
            wo.save()
            try:
                subject = 'Newsletter Activated'   
                message = f'Hi {email},Newsletter Activated for your entered email address.Now you will get all the updates from PGmanager app.'
                email_from = settings.EMAIL_HOST_USER 
                recipient_list = [email] 
                send_mail( subject, message, email_from, recipient_list ,fail_silently=False)
                messages.info(request,"Newsletter Activated.")
            except:
                messages.info(request,"Newsletter Activated.")
        return render(request,"contact.html",{"g":g})   
    return render(request,"contact.html")

def crudadv(request):
    p1=request.user
    x = datetime.datetime.now()
    now=x.strftime("%Y")+"-"+x.strftime("%m")+"-"+x.strftime("%d")
    if request.method=="POST":
        u = User.objects.get(username=p1.username)
        n = Advertisement.objects.filter(username=p1.username)
        id=int(request.POST.get("id"))
        return render(request,"crudadv.html",{"id":id,"now":now,'n':n})
    else:
        id=0
        if(p1.username==""):
            return render(request,"crudadv.html")
        else:    
            u = User.objects.get(username=p1.username)
            return render(request,"crudadv.html",{"now":now})

def createadv(request):
    p1=request.user
    x = datetime.datetime.now()
    u = User.objects.get(username=p1.username)
    id=1
    now=x.strftime("%Y")+"-"+x.strftime("%m")+"-"+x.strftime("%d")
    if request.method=="POST":
        username=request.POST.get("username")
        aid=request.POST.get("aid")
        sub=request.POST.get("sub")
        text=request.POST.get("text")
        link=request.POST.get("link")
        createdate=request.POST.get("date")
        u1 = User.objects.get(username=p1.username)
        if(Advertisement.objects.filter(username=username,aid=aid).exists()):
            print("nick1")
            messages.info(request,'Header Exists')
            return render(request,"crudadv.html",{"id":id,"now":now})
        else:
            print("nick2")
            t=Advertisement(username=username,aid=aid,sub=sub,text=text,link=link,datetime=createdate)
            t.save()
            messages.info(request,'Blog Added')
            id=1
            return render(request,"crudadv.html",{"id":id,"now":now})
    return render(request,"crudadv.html",{"id":id,"now":now})

def deleteadv(request):
    p1=request.user
    x = datetime.datetime.now()
    n = Advertisement.objects.filter(username=p1.username)
    id=2
    now=x.strftime("%Y")+"-"+x.strftime("%m")+"-"+x.strftime("%d")
    if request.method=="POST":
        aid=request.POST.get("id")
        Advertisement.objects.filter(username=p1.username,aid=aid).delete()
        messages.info(request,'Advertisement Deleted')
        return render(request,"crudadv.html",{"id":id,"now":now,'n':n})   
    return render(request,"crudadv.html",{"id":id,"now":now,'n':n})

def crudblog(request):
    p1=request.user
    x = datetime.datetime.now()
    now=x.strftime("%Y")+"-"+x.strftime("%m")+"-"+x.strftime("%d")
    if request.method=="POST":
        u = User.objects.get(username=p1.username)
        n = Blog.objects.filter(username=p1.username)
        id=int(request.POST.get("id"))
        return render(request,"crudblog.html",{"id":id,"now":now,'n':n})
    else:
        id=0
        if(p1.username==""):
            return render(request,"crudblog.html")
        else:    
            u = User.objects.get(username=p1.username)
            return render(request,"crudblog.html",{"now":now})

def createblog(request):
    p1=request.user
    x = datetime.datetime.now()
    u = User.objects.get(username=p1.username)
    id=1
    now=x.strftime("%Y")+"-"+x.strftime("%m")+"-"+x.strftime("%d")
    if request.method=="POST":
        username=request.POST.get("username")
        bid=request.POST.get("bid")
        sub=request.POST.get("sub")
        text=request.POST.get("text")
        createdate=request.POST.get("date")
        u1 = User.objects.get(username=p1.username)
        if(Blog.objects.filter(username=username,bid=bid).exists()):
            print("nick1")
            messages.info(request,'Header Exists')
            return render(request,"crudblog.html",{"id":id,"now":now})
        else:
            print("nick2")
            t=Blog(username=username,bid=bid,sub=sub,text=text,datetime=createdate)
            t.save()
            messages.info(request,'Blog Added')
            id=1
            return render(request,"crudblog.html",{"id":id,"now":now})
    return render(request,"crudblog.html",{"id":id,"now":now})

def deleteblog(request):
    p1=request.user
    x = datetime.datetime.now()
    n = Blog.objects.filter(username=p1.username)
    id=2
    now=x.strftime("%Y")+"-"+x.strftime("%m")+"-"+x.strftime("%d")
    if request.method=="POST":
        bid=request.POST.get("id")
        Blog.objects.filter(username=p1.username,bid=bid).delete()
        messages.info(request,'Blog Deleted')
        return render(request,"crudblog.html",{"id":id,"now":now,'n':n})   
    return render(request,"crudblog.html",{"id":id,"now":now,'n':n})