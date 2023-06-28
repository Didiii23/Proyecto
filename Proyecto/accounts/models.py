from django.db import models

#utilizo el model User de Django
from django.contrib.auth.models import User




class Account(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='avatares', null=True, blank=True)

class Avatar(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True)
    imagen = models.ImageField(upload_to='avatares', null=True, blank = True)

    @property
    def d(self):
        return self.user.last_name

    def __str__(self):
        return f"{self.user} - {self.imagen}"