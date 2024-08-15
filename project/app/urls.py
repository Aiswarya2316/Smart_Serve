from django.urls import path
from . import views
urlpatterns = [
path('login',views.login),
path('',views.register),
path('userhome',views.userhome),
path('adminhome',views.adminhome),
]