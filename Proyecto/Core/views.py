from django.shortcuts import render
from .models import Curso
from django.http import HttpResponse
from django.template import Template , Context, loader
from Core.forms import CursoFormulario, BuscaCursoForm


def inicio(request):
    return render (request,"Core/index.html")


def cursos(request):
    return render(request, "Core/cursos.html")

def profesores(request):
    return render(request, "Core/profesores.html")

def estudiantes(request):
    return render(request, "Core/estudiantes.html")

def entregables(request):
    return render(request, "Core/entregables.html")


def form_con_api(request):
    if request.method == "POST":
        miFormulario = CursoFormulario(request.POST) # Aqui me llega la informacion del html
        # print(miFormulario)
        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            curso = Curso(nombre=informacion["curso"], camada=informacion["camada"])

            curso.save()
            return render(request, "Core/index.html")
    else:
        miFormulario = CursoFormulario()

    return render (request, "Core/form_con_api.html", {"miFormulario": miFormulario})

def buscar_form_con_api(request):
    if request.method == "POST":
        miFormulario = BuscaCursoForm(request.POST) # Aqui me llega la informacion del html

        if miFormulario.is_valid():
            informacion = miFormulario.cleaned_data
            
            cursos = Curso.objects.filter(nombre__icontains=informacion["curso"])

            return render(request, "Core/resultados_buscar_form.html", {"cursos": cursos})
    else:
        miFormulario = BuscaCursoForm()

    return render(request, "Core/buscar_form_con_api.html", {"miFormulario": miFormulario})

def mostrar_cursos(request):

    cursos = Curso.objects.all() #trae todos los profesores

    contexto= {"cursos":cursos} 

    return render(request, "Core/mostrar_cursos.html",contexto)
