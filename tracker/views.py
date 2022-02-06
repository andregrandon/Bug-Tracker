from django.views.generic import TemplateView



class HomePage(TemplateView):
    template_name='index.html'

class AboutPage(TemplateView):
    template_name='about.html'

class ContactPage(TemplateView):
    template_name='contact.html'


class UserAccount(TemplateView):
    template_name='user.html'

class ChangePassword(TemplateView):
    template_name='changepassword.html'
