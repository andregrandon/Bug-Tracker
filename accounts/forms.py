# forms.py
from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import UserProfile

class SignUpForm(UserCreationForm):
    # You can add more fields here if needed

    class Meta:
        model = UserProfile
        fields = ('username', 'email', 'password1', 'password2')
