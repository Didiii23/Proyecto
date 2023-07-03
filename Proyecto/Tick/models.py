from django.db import models

# Create your models here.

#Creating a Class Products for the Store Inventory
class Products(models.Model):
    name = models.CharField(max_length=40)
    type =models.CharField(max_length=20)
    price= models.IntegerField()
    syze=models.CharField(max_length=20)
    stock = models.IntegerField()



#Creating a Class Concert for the Tour 
class Concerts(models.Model):
    date = models.DateField()
    country = models.CharField(max_length=20)
    city = models.CharField(max_length=40)



