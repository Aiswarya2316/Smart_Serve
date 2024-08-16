from django.urls import path
from . import views
urlpatterns = [
path('',views.login),
path('register',views.register),
path('userhome',views.userhome),
path('adminhome',views.adminhome),
]