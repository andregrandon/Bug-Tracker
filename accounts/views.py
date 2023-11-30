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
from .forms import SignUpForm

from django.conf import settings
from django.contrib.auth.decorators import login_required


from accounts import forms


@login_required
def dashboard(request):
    return render(request, 'accounts/templates/accounts/dashboard.html', )



class LogSuccess(CreateView):
    success_url = reverse_lazy("accounts:login")
    template_name = 'accounts/signup.html'

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('accounts:login')  # Redirect to the home page after successful signup
    else:
        form = SignUpForm()

    return render(request, 'accounts/signup.html', {'form': form})