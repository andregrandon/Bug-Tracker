from django.db import models
from django.contrib.auth.models import User


class Contact(models.Model):
    id_number =status_id = models.AutoField(primary_key=True)
    Name= models.CharField(max_length=255, default = '',)
    email = models.CharField(max_length=255, default = '',)
    phone = models.CharField(max_length=255, default = '')
    message = models.CharField(max_length=255, default = '')
    def __str__(self):
        return self.id_number
