#from django.conf.urls import url
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.contrib import admin

app_name='listings'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
#display of info urls
    path('deptlisting',views.departments,name='deptlisting'),
    path('buglisting',views.buglist,name='buglisting'),
    path('statuslisting',views.statuslist,name='statuslisting'),
    path('typelisting',views.typelist,name='typelisting'),
    path('projectlisting',views.projectlist,name='projectlisting'),
    path('userlisting',views.userlist,name='userlisting'),
#create urls
    path('add_bug/',views.addBug,name='add_bug'),
    path('add_type/',views.addType,name='add_type'),
    path('add_status/',views.addStatus,name='add_status'),
    path('add_dept/',views.addDept,name='add_dept'),
    path('add_project/',views.addProject,name='add_project'),
    path('add_user/',views.addUser,name='add_user'),
#update urls
    path('update_bug/<str:pk>/',views.updateBug,name='update_bug'),
    path('update_type/<str:pk>/',views.updateType,name='update_type'),
    path('update_status/<str:pk>/',views.updateStatus,name='update_status'),
    path('update_project/<str:pk>/',views.updateProject,name='update_project'),
    path('update_user/<str:pk>/',views.updateUser,name='update_user'),
    path('update_dept/<str:pk>/',views.updateDept,name='update_dept'),
#delete urls
    path('delete_bug/<str:pk>/',views.deleteBug,name='delete_bug'),
    path('delete_type/<str:pk>/',views.deleteType,name='delete_type'),
    path('delete_status/<str:pk>/',views.deleteStatus,name='delete_status'),
    path('delete_project/<str:pk>/',views.deleteProject,name='delete_project'),
    path('delete_user/<str:pk>/',views.deleteUser,name='delete_user'),
    path('delete_dept/<str:pk>/',views.deleteDept,name='delete_dept'),

    ]
