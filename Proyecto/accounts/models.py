from django.db import models

#utilizo el model User de Django
from django.contrib.auth.models import User

class Account(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatares', null=True, black=True)
    
