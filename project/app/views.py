from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages

# Create your views here.

def login(req):
    if req.method=='POST':
        email1 = req.POST['Email']
        password = req.POST['password']
        try:
            data=Register.objects.get(Email=email1 ,password=password)
            return redirect(userhome) 
        except:
            messages.warning(req, "details not available.")
    return render(req,'login.html')

def register(req):
    if req.method=='POST':
        email1=req.POST['Email']
        name2=req.POST['name']
        phonenumber3=req.POST['phonenumber']
        location4=req.POST['location']
        password5=req.POST['password']
        try:
            data=Register.objects.create(Email=email1 , name=name2 , phonenumber=phonenumber3 ,location=location4 , password=password5 )
            data.save()
            return redirect(login)
        except:
            messages.warning(req, "Your account expires in three days.")
    return render(req,'register.html')

def userhome(req):
    return render(req,'userhome.html')

def adminhome(req):
    return render(req,'adminhome.html')

def profile(req):
    return render(req,'profile.html')

def upload(req):
    return render(req,'upload.html')