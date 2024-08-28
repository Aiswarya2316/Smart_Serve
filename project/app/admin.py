from django.contrib import admin
from .models import *

# Register your models here.
admin.site.register(Product)
admin.site.register(cart)
admin.site.register(delivery)
admin.site.register(buy)
