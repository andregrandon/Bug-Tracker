#from django.conf.urls import url
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.contrib import admin

app_name='contact'
urlpatterns = [

    path('contact',views.contact,name='contact'),

]
