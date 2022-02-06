from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Status(models.Model):
    status_id = models.AutoField(primary_key=True)
    status_title = models.CharField(max_length=255, default = '',)
    status_description = models.CharField(max_length=255, default = '',blank=True)
    def __str__(self):
        return self.status_title

class BugType(models.Model):
    type_id = models.AutoField(primary_key=True)
    type_title = models.CharField(max_length=255,default = '')
    type_description = models.CharField(max_length=255, default = '',blank=True)
    def __str__(self):
        return self.type_title

class Department(models.Model):
    department_id = models.AutoField(primary_key=True)
    department_name = models.CharField(max_length=255,default = '')
    department_location = models.CharField(max_length=255,default = '')
    def __str__(self):
        return self.department_name

class Project(models.Model):
    project_id = models.AutoField(primary_key=True)
    project_lead_name = models.CharField(max_length=255, default = '')
    project_title = models.CharField(max_length=255, default = '',)
    project_submission_date = models.CharField(max_length=255, default = '')
    project_duration = models.CharField(max_length=255, default = '')
    project_email = models.CharField(max_length=255, default = '')
    project_department = models.CharField(max_length=255, default = '',)
    project_client_name = models.CharField(max_length=255, default = '',blank=True)
    def __str__(self):
        return self.project_title

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    user_name = models.CharField(max_length=255, default = '')
    role = models.CharField(max_length=255, default = '',)
    user_mobile = models.CharField(max_length=255, default = '')
    user_email = models.CharField(max_length=255, default = '')
    user_dob = models.CharField(max_length=255, default = '')
    user_image = models.CharField(max_length=255, default = '',blank=True)
    def __str__(self):
        return self.user_name

class Bug(models.Model):
    bug_id = models.AutoField(primary_key=True)
    user_reporting = models.CharField(max_length=255, default = '')
    user_number = models.CharField(max_length=255, default = "")
    user_email = models.CharField(max_length=255, default = '')
    bug_name = models.CharField(max_length=255, default = "", null=True)
    bug_project = models.ForeignKey(Project, null=True, on_delete=models.SET_NULL)
    bug_date = models.CharField(max_length=255, default = '')
    bug_level = models.CharField(max_length=255, default = '')
    bug_priority = models.ForeignKey(BugType, null=True, on_delete=models.SET_NULL)
    bug_status = models.ForeignKey(Status, null=True, on_delete=models.SET_NULL)
    bug_description = models.TextField(default = "")
    bug_cost = models.CharField(max_length=255, default = "",blank=True)
    bug_image = models.CharField(max_length=255, default="",blank=True)
    bug_specifications = models.CharField(max_length=255, default = "",blank=True)
    def __str__(self):
        return self.bug_name
