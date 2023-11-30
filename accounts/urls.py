#from django.conf.urls import url
from django.urls import path
from django.contrib.auth import views as auth_views
from accounts import views
from .views import signup, dashboard
app_name = 'accounts'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('dashboard/', dashboard, name='dashboard'),


    path('login',auth_views.LoginView.as_view(template_name='accounts/login.html'),name='login'),
    path('logout',auth_views.LogoutView.as_view(),name='logout'),
    #path('signup/', signup, name='signup'),

    ]
