from django.db import models


class Contact(models.Model):
    id_number = models.AutoField(primary_key=True)
    Name= models.CharField(max_length=255, default = '',)
    email = models.CharField(max_length=255, default = '',)
    phone = models.CharField(max_length=255, default = '')
    message = models.TextField(max_length=255, default = '')
    def __str__(self):
        return self.Name
