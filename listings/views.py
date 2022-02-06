from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import TemplateView
from django.db import connection
from .forms import *

from .models import Status,BugType,Department,Project,User,Bug

def home(request):
    context = locals()
    template = 'home.html'
    return render(request,template,context)

#
# listing functions

def departments(request):
        departments = Department.objects.all()
        print("------------------------------------------")
        for i in departments:
            print(i.department_id)
        print("------------------------------------------")
        return render(request,'listings/departmentdetails.html', {'departments':departments})


def buglist(request):
    buglist = Bug.objects.all()
    print("------------------------------------------")
    for i in buglist:
        print(i.bug_id)
    print("------------------------------------------")
    return render(request,'listings/buglisting.html',{'buglist':buglist})


def statuslist(request):
    statuslist = Status.objects.all()
    print("------------------------------------------")
    for i in statuslist:
        print(i.status_id)
    print("------------------------------------------")
    return render(request,'listings/statusdetails.html',{'statuslist':statuslist})


def typelist(request):
    typelist = BugType.objects.all()
    print("------------------------------------------")
    for i in typelist:
        print(i.type_id)
    print("------------------------------------------")
    return render(request,'listings/typedetails.html',{'typelist':typelist})


def projectlist(request):
    projectlist = Project.objects.all()
    print("------------------------------------------")
    for i in projectlist:
        print(i.project_id)
    print("------------------------------------------")
    return render(request,'listings/projectdetails.html',{'projectlist':projectlist})


def userlist(request):
    userlist = User.objects.all()
    print("------------------------------------------")
    for i in userlist:
        print(i.user_id)
    print("------------------------------------------")
    return render(request,'listings/userdetails.html',{'userlist':userlist})


# create functions

def addBug(request):

    form = BugForm()
    if request.method =='POST':
        # print('printing POST', request.POST)
        form = BugForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/listings/buglisting')

    context = {'addbug':form}
    return render(request, 'listings/add_bug.html', context)

def addType(request):

    form = BugTypeForm()
    if request.method == 'POST':
        # print('printing POST', request.POST)
        form = BugTypeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/listings/typelisting')

    context = {'addtype':form}
    return render(request, 'listings/add_type.html', context)


def addStatus(request):

    form = StatusForm()
    if request.method == "POST":
        # print('printing POST', request.POST)
        form = StatusForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/listings/statuslisting')

    context = {'addstatus':form}
    return render(request, 'listings/add_status.html', context)

def addDept(request):
    form = DeptForm()
    if request.method == "POST":
        form = DeptForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/listings/deptlisting')

    context = {'adddept':form}
    return render (request, 'listings/add_dept.html', context)

def addProject(request):
    form = ProjectForm()
    if request.method == "POST":
        form = ProjectForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/listings/projectlisting')

    context = {'addproject':form}
    return render (request, 'listings/add_project.html', context)

def addUser(request):
    form = UserForm()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/listings/userlisting')

    context = {'adduser':form}
    return render (request, 'listings/add_user.html', context)

#update functions

def updateBug(request, pk):

    updatebug = Bug.objects.get(bug_name=pk)
    form = BugForm(instance=updatebug)

    if request.method == 'POST':
        form = BugForm(request.POST, instance=updatebug)
        if form.is_valid():
            form.save()
        return redirect('/listings/buglisting')


    context = {'addbug':form}
    return render(request,'listings/add_bug.html/',context)

def updateType(request, pk):

    updatetype = BugType.objects.get(type_id=pk)
    form = BugTypeForm(instance=updatetype)

    if request.method == 'POST':
        form = BugTypeForm(request.POST, instance=updatetype)
        if form.is_valid():
            form.save()
        return redirect('/listings/typelisting')

    context = {'addtype':form}
    return render(request,'listings/add_type.html/', context)

def updateStatus(request, pk):

    updatestatus = Status.objects.get(status_id=pk)
    form = StatusForm(instance=updatestatus)

    if request.method == "POST":
        form = StatusForm(request.POST, instance = updatestatus)
        if form.is_valid():
            form.save()
        return redirect('/listings/statuslisting')

    context = {'addstatus':form}
    return render (request, 'listings/add_status.html/', context)

def updateProject(request, pk):

    updateproject = Project.objects.get(project_id=pk)
    form = ProjectForm(instance = updateproject)

    if request.method == "POST":
        form = ProjectForm(request.POST, instance = updateproject)
        if form.is_valid():
            form.save()
        return redirect('/listings/projectlisting')

    context = {'addproject':form}
    return render (request, 'listings/add_project.html/', context)

def updateUser(request, pk):

    updateuser = User.objects.get(user_id=pk)
    form = UserForm(instance = updateuser)

    if request.method == "POST":
        form = UserForm(request.POST,instance=updateuser)
        if form.is_valid():
            form.save()
        return redirect('/listings/userlisting')

    context = {'adduser': form}
    return render (request, 'listings/add_user.html/', context)

def updateDept(request, pk):

    updatedept = Department.objects.get(department_id=pk)
    form = DepartmentForm(instance = updatedept)

    if request.method == "POST":
        form = DepartmentForm(request.POST,instance=updatedept)
        if form.is_valid():
            form.save()
        return redirect('/listings/deptlisting')

    context = {'adddept': form}
    return render (request, 'listings/add_dept.html/', context)


#delete methods

def deleteBug(request, pk):
    deletebug = Bug.objects.get(bug_name=pk)
    if request.method == "POST":
        deletebug.delete()
        return redirect ('/listings/buglisting')


    context = {'deletebug':deletebug}
    return render(request, 'templates/delete/deletebug.html', context)

def deleteType(request, pk):
    deletetype = BugType.objects.get(type_title=pk)
    if request.method == "POST":
        deletetype.delete()
        return redirect ('/listings/typelisting')

    context = {'deletetype':deletetype}
    return render(request, 'templates/delete/deletetype.html', context)

def deleteStatus(request, pk):
    deletestatus = Status.objects.get(status_id=pk)
    if request.method == "POST":
        deletestatus.delete()
        return redirect ('/listings/statuslisting')

    context = {'deletestatus':deletestatus}
    return render (request, 'templates/delete/deletestatus.html', context)

def deleteProject(request, pk):
    deleteproject = Project.objects.get(project_id=pk)
    if request.method == "POST":
        deleteproject.delete()
        return redirect ('/listings/projectlisting')

    context = {'deleteproject':deleteproject}
    return render (request, 'templates/delete/deleteproject.html', context)

def deleteUser(request, pk):
    deleteuser = User.objects.get(user_id=pk)
    if request.method == "POST":
        deleteuser.delete()
        return redirect ('/listings/userlisting')

    context = {'deleteuser':deleteuser}
    return render (request, 'templates/delete/deleteuser.html', context)

def deleteDept(request, pk):
    deletedept = Department.objects.get(department_id=pk)
    if request.method == "POST":
        deletedept.delete()
        return redirect ('/listings/deptlisting')

    context = {'deletedept':deletedept}
    return render (request, 'templates/delete/deletedept.html', context)
