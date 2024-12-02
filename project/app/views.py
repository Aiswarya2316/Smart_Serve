
from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
from django.contrib.auth.models import User,auth
import datetime
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.

def get_usr(req):
    data=Register.objects.get(Email=req.session['user'])
    return data


def get_shop(req):
    data=Product.objects.get(category=req.session['shop'])
    return data




def login(req):
    if 'user' in req.session:
        return redirect(userhome)
    if 'shop' in req.session:
        return redirect(adminhome)
    if 'deliveryss' in req.session:
        return redirect(deliverys)

    if req.method=='POST':
        email=req.POST['Email']
        password=req.POST['password']
        try:
            data=Register.objects.get(Email=email,password=password)
            req.session['user']=data.Email
            return redirect(userhome)
        except:
            shop=auth.authenticate(username=email,password=password)
            if shop is not None:
                auth.login(req,shop)
                req.session['shop']=email

                return redirect(adminhome)
         
            else:
                data=delivery.objects.get(email=email,password=password)
                req.session['deliveryss']=data.email

                return redirect(deliverys)

                messages.warning(req, "INVALID INPUT !")
    return render(req,'login.html')



def logout(req):
    if 'user' in req.session:
        # req.session.flush()
        del req.session['user']
    if 'shop' in req.session:
        del req.session['shop']
    if 'deliveryss' in req.session:
        del req.session['deliveryss']
    return redirect(login)


def register(req):

    if req.method=='POST':
        name1=req.POST['name']
        email2=req.POST['email']
        phonenumber3=req.POST['phonenumber']
        location4=req.POST['location']
        password5=req.POST['password']
        subject = 'Registration details '
        message = 'ur account uname {}  and password {}'.format(name1,password5)
        from_email = settings.EMAIL_HOST_USER
        recipient_list = [email2]
        send_mail(subject, message, from_email, recipient_list,fail_silently=False)  
        try:
            data=Register.objects.create(name=name1,Email=email2,phonenumber=phonenumber3,location=location4,password=password5)
            data.save()
            return redirect(login)
        except:
            messages.warning(req, "Email Already Exits , Try Another Email.")
    return render(req,'register.html')



def delregister(req):

    if req.method=='POST':
        name1=req.POST['name']
        email2=req.POST['email']
        phonenumber3=req.POST['phonenumber']
        location4=req.POST['rout']
        password5=req.POST['password']
    
        try:
            data=delivery.objects.create(name=name1,email=email2,phonenumber=phonenumber3,rout=location4,password=password5)
            data.save()
            return redirect(login)
        except:
            messages.warning(req, "Email Already Exits , Try Another Email.")
    return render(req,'delregister.html')
    print(delregister)


def userhome(req):
    if 'user' in req.session:
        return render(req,'userhome.html')
    else:
        return redirect(login)


def adminhome(req):
    
    return render(req,'mobileappliances/adminhome.html')


###profile
def profile(req):
    if 'user' in req.session:
        # data=Register.objects.get(Email=req.session['user'])
        return render(req,'profile.html',{'data':get_usr(req)})
    else:
        return redirect(login)
    

###profile update
def upload(req):
    if 'user' in req.session:
        data=Register.objects.get(Email=req.session['user'])
        if req.method=='POST':
            name=req.POST['name']
            phonenumber=req.POST['phonenumber']
            location=req.POST['location']
            Register.objects.filter(Email=req.session['user']).update(name=name,phonenumber=phonenumber,location=location)
            return redirect(profile)
        return render(req,'upload.html',{'data':data})

    else:
       return redirect(login)
      
  
def viewuser(req):
    return render(req,'mobileappliances/viewuser.html')


def addpro(req):
    if req.method=='POST':
        name = req.POST['name']
        discription = req.POST['discription']
        price = req.POST['price']
        category = req.POST['category']
        quantity = req.POST['quantity']
        offerprice = req.POST['offerprice']
        image = req.FILES['image']
        data=Product.objects.create(name=name,discription=discription,price=price,category=category,quantity=quantity,offerprice=offerprice,image=image)
        data.save()
        return redirect(viewpro)
    return render(req,'mobileappliances/addpro.html')


def viewpro(req):
    data=Product.objects.all()
    return render(req,'mobileappliances/viewpro.html',{'data':data})


def bookinghistry(req):
    data=buy.objects.all()
    data1=delivery.objects.all()
    return render(req,'mobileappliances/bookinghistry.html',{'data':data,'data1':data1})


def details(req,id):
    if 'shop' in req.session:
        # data=Register.objects.get(Email=req.session['user'])
        data=Product.objects.get(pk=id)
        return render(req,'mobileappliances/details.html',{'data':data})
    else:
        return redirect(login)
    

def viewproduct(req):
    data=Product.objects.all()
    return render(req,'viewproduct.html',{'data':data})


def edit(req,id):
    data=Product.objects.get(pk=id)
    if req.method=='POST':
        name1=req.POST['name']
        price=req.POST['price']
        offerprice=req.POST['offerprice']
        quantity=req.POST['quantity']
        Product.objects.filter(pk=id).update(name=name1,price=price,offerprice=offerprice,quantity=quantity,)
        return redirect(viewpro)
    return render(req,'mobileappliances/edit.html',{'data':data})

def prodetails(req,id):
    data=Product.objects.get(pk=id)
    return render(req,'prodetails.html',{'data':data})

def delete(req,id):
    data=Product.objects.get(pk=id)
    data.delete()
    return redirect(viewpro) 

def user_cart(req,id):
    if 'user' in req.session:
        product=Product.objects.get(pk=id)
        user=get_usr(req)
        qty=1
        try:
            dtls=cart.objects.get(product=product,user=user)
            dtls.quantity+=1
            dtls.save()
        except:
            data=cart.objects.create(product=product,user=user,quantity=qty)
            data.save()
        return redirect(user_view_cart)
    else:
        return redirect(login)
    
def user_view_cart(req):
    if 'user' in req.session:
        data=cart.objects.filter(user=get_usr(req))
        return render(req,'cart.html',{'data':data})

def qty_incri(req,id):
    data=cart.objects.get(pk=id)
    data.quantity+=1
    data.save()
    return redirect(user_view_cart)

def qty_decri(req,id):
    data=cart.objects.get(pk=id)
    if data.quantity>1:
        data.quantity-=1
        data.save()
    return redirect(user_view_cart)
  
def deletes(req,id):
    data=cart.objects.get(pk=id)
    data.delete()
    return redirect(user_view_cart) 

def buys(req,id):
     if 'user' in req.session:
        cart_product=cart.objects.get(pk=id)
        user=get_usr(req)
        quantity=cart_product.quantity
        date=datetime.datetime.now().strftime("%x")
        price=cart_product.product.price
        order=buy.objects.create(product=cart_product.product,user=user,quantity=quantity,date_of_buying=date,price=price)
        order.save()
        return redirect(user_view_cart)
     
def order_details(req):
    data=buy.objects.filter(user=get_usr(req))
    return render(req,'orderdetails.html',{'data':data})
    
def deliverys(req):
    # data=buy.objects.filter(deliveryss=get_usr(req))
    # data1=Product.objects.filter(user=get_usr(req))
    return render(req,'delivery.html')

def assigndel(req,id):
    if req.method=='POST':
        data1=buy.objects.get(pk=id)
        data1.del_boy=True
        data1.save()
        data=req.POST['delselect'] 
        data2=delivery.objects.get(pk=id)
        delivry=delpro.objects.create(delivery=data2,buy=data1) 
        delivry.save()

        return redirect(bookinghistry)  