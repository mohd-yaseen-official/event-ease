from django.urls import include, path

from .views import *


app_name = 'authentication'

urlpatterns = [

    path('login/', login, name='login'),
    path('logout/', logout, name='logout'),

    path('signup/user', create_user, name='create_user'),
    path('signup/customer', create_customer, name='create_customer'),

]