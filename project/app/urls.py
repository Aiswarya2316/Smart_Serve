from django.urls import path
from . import views
urlpatterns = [
path('',views.login),
path('logout',views.logout),
path('register',views.register),
path('delregister',views.delregister),
path('userhome',views.userhome),
path('adminhome',views.adminhome),
path('profile',views.profile),
path('upload',views.upload),
path('viewuser',views.viewuser),
path('addpro',views.addpro),
path('viewpro',views.viewpro),
path('bookinghistry',views.bookinghistry),
path('details/<int:id>',views.details),
path('viewproduct',views.viewproduct),
path('edit/<int:id>',views.edit),
path('prodetails/<int:id>',views.prodetails),
path('delete/<int:id>',views.delete),
path('cart/<int:id>',views.user_cart),
path('user_view_cart',views.user_view_cart),
path('qty_incri/<int:id>',views.qty_incri),
path('qty_decri/<int:id>',views.qty_decri),
path('deletes/<int:id>',views.deletes),
path('buys/<int:id>',views.buys),
path('order_details',views.order_details),
path('delivery',views.deliverys),
path('assigndel/<int:id>',views.assigndel),


]