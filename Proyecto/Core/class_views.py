#Nuevo archivo de vistas para utilizar clases
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Curso


#Mostrar Cursos
class CursoListView(ListView):
    model = Curso
    template_name = "Core/class_list.html"


#Detalles del curso (Trae un solo registro y muestra los datos)
class CursoDetailView(DetailView):
    model = Curso
    template_name= "Core/class_detail.html"


#Crear Curso
class CursoCreateView(CreateView):
    model = Curso
    # Si se crea el usuario se redirige al siguiente URL
    success_url = "Core/curso/list" 
    fields = ['nombre', 'camada']


#Update View
class CursoUpdateView(UpdateView):
    model = Curso
    success_url = "/Core/curso/list"
    fields = ['nombre', 'camada']


#Delete View
class CursoDeleteView(DeleteView):
    model = Curso
    success_url= "Core/curso/list"