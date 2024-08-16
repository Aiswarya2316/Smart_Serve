from django.db import models

# Create your models here.

class Register(models.Model):
    Email = models.EmailField(unique=True)
    name = models.TextField()
    phonenumber = models.IntegerField()
    password = models.IntegerField()
    location= models.TextField()

    def __str__(self):
        return self.name
    
class Product(models.Model):
    name = models.TextField()
    discription = models.TextField()
    price = models.IntegerField()
    category = models.TextField()
    quantity = models.IntegerField()
    offerprice = models.IntegerField()
    image = models.ImageField((""), upload_to=None, height_field=None, width_field=None, max_length=None)

    def __str__(self):
        return self.name
    
class cart(models.Model):
    user = models.TextField()
    product = models.TextField()
    quantity = models.IntegerField()

    def __str__(self):
        return self.name
    
class buy(models.Model):
    product = models.TextField()
    user = models.TextField()
    date_of_buying = models.IntegerField()
    payment_status = models.TextField()
    order_status = models.IntegerField()
    quantity = models.IntegerField()

    def __str__(self):
        return self.name


    
