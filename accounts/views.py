from django.contrib.auth import login,logout
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.conf import settings
from django.db.models import Q
from django.core.files.storage import FileSystemStorage
from django.contrib import messages
from django.db import connection
import re

from django.conf import settings
from django.contrib.auth.decorators import login_required


from accounts import forms
# Create your views here.


@login_required
def dashboard(request):
    return render(request, 'accounts/templates/accounts/dashboard.html', )



class LogSuccess(CreateView):
    success_url = reverse_lazy("accounts:login")
    template_name = 'accounts/signup.html'
