from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
from django.contrib.auth.models import User,auth

# Create your views here.

def login(req):
    if 'user' in req.session:
        return redirect(userhome)

    if req.method=='POST':
        email1 = req.POST['Email']
        password = req.POST['password']
        try:
            data=Register.objects.get(Email=email1 ,password=password)
            req.session['user']=data.Email
            return redirect(userhome) 
        except:
            shop=auth.authenticate(username=email1 , password=password)
            if shop is not None:
                auth.login(req,shop)
                req.session['shop']=email1
                return redirect(adminhome)
            messages.warning(req, "details not available.")
    return render(req,'login.html')

def logout(req):
    if 'user' in req.session:
        del req.session['user']
    if 'shop' in req.session:
        del req.session
        auth.logout()
    return redirect(login)    

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
    if 'user' in req.session:
        data=Register.objects.get(Email=req.session['user'])
        return render(req,'profile.html',{'data':data})
    else:
        return redirect(login)

def upload(req):
    if 'user' in req.session:
        data=Register.objects.get(Email=req.session['user'])
        if req.method=='POST':
            name=req.POST['name']
            phonenumber=req.POST['phonenumber']
            location=req.POST['location']
            Register.objects.filter(Email=req.session['user']).update(name=name ,phonenumber=phonenumber ,location=location)
            return redirect(profile)
        return render(req,'upload.html',{'data':data})
    else:
        return redirect(login)