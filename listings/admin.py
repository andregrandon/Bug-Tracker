from django.contrib import admin
from .models import Bug,Status,BugType,Department,Project,User
# Register your models here.

admin.site.register(Bug)
admin.site.register(Status)
admin.site.register(BugType)
admin.site.register(Department)
admin.site.register(Project)
admin.site.register(User)
