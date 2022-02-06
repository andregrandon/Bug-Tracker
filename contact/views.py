from django.shortcuts import render, redirect
from .forms import *
from django.http import HttpResponse


from .models import Contact
# Create your views here.

def contact(request):

    form = ContactForm()
    if request.method =='POST':
        # print('printing POST', request.POST)
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/contact/contact')

    context = {'contact':form}
    return render(request, 'contact/contact.html', context)
