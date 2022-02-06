from django.forms import ModelForm
from .models import *

# meta data for CRUD

class BugForm(ModelForm):
    class Meta:
        model = Bug
        fields = ['bug_name','bug_project','bug_date',
                'bug_priority','bug_status','bug_description',
                'user_reporting','user_email','user_number','bug_image']

class BugTypeForm(ModelForm):
    class Meta:
        model = BugType
        fields = ['type_title',
                'type_description']

class StatusForm(ModelForm):
    class Meta:
        model = Status
        fields = ['status_title','status_description']


class DeptForm(ModelForm):
    class Meta:
        model = Department
        fields = ['department_name','department_location']

class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['project_lead_name','project_title','project_submission_date','project_duration',
                    'project_client_name','project_email','project_department']

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['user_image','user_name','role','user_mobile','user_email','user_dob']


class DepartmentForm(ModelForm):
    class Meta:
        model = Department
        fields = ['department_name','department_location']
