from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

def Albums (request):
    return render (request,"Tick/Albums.html")


def Tours (request):
    return render (request,"Tick/Tours.html")


def About (request):
    return render (request, "Tick/About.html")


@login_required
def Store (request):
    return render (request, "Tick/Store.html")

def Inicio(request):
    return render (request,"Tick/Inicio.html") 