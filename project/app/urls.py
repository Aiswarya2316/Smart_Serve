from django.urls import path
from . import views
urlpatterns = [
path('',views.login),
path('logout',views.logout),
path('register',views.register),
path('userhome',views.userhome),
path('adminhome',views.adminhome),
path('profile',views.profile),
path('upload',views.upload),
path('viewuser',views.viewuser),
path('addpro',views.addpro),
path('viewpro',views.viewpro),
path('bookinghistry',views.bookinghistry),
]