from django import forms
from .models import Products, Concerts

class ProductForm(forms.Forms):
    name = forms.CharField()
    type =forms.CharField(max_length=20)
    price= forms.IntegerField()
    syze= forms.CharField(max_length=20)
    stock = forms.IntegerField()


class ConcertsForm(forms.Forms):
    date = forms.DateField()
    country = forms.CharField(max_length=20)
    city = forms.CharField(max_length=40)