from django.conf.urls import url
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('loginpage/', views.login_page, name='loginpage'),
    path('logoutpage/', views.logout_page, name='logoutpage'),
    path('addproduct/', views.add_product, name='addproduct'),
    path('viewproduct/', views.view_product, name='viewproduct'),
    path('editproduct/<int:pk>', views.edit_product, name='editproduct'),
    path('deleteprodcut/<int:pk>', views.delete_product, name='deleteproduct'),
    path('addcustomer/', views.add_customer, name='addcustomer'),
    path('frontpage/', views.front_page, name='frontpage'),
    path('addorder/<int:pk>', views.view_customer, name='viewcustomer'),
    path('deleteorder/<int:a>/<int:b>', views.delete_order, name='deleteorder')
]