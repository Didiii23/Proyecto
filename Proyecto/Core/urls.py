from django.urls import path
from Core import views
from Core import class_views

urlpatterns = [
    path('', views.inicio, name="Inicio"),
    path('profesores/', views.profesores, name="Profesores"),
    path('estudiantes/', views.estudiantes, name="Estudiantes"),
    path('cursos/', views.cursos, name="Cursos"),
    path('entregables/', views.entregables, name="Entregables"),
    path('form-con-api/', views.form_con_api, name="Busca-Form-Api"),
    path('buscar-form-con-api/', views.buscar_form_con_api, name="Buscar-Form-Con-Api"),
    path('mostrar-cursos/', views.mostrar_cursos, name="Mostrar_Cursos")

   
]



#URL's basadas en clases

urlpatterns +=[
    path ('class-list/', class_views.CursoListView.as_view(), name="List"),
    path ('class-detail/<pk>/',class_views.CursoDetailView.as_view(), name="Detail"),
    path ('class-create', class_views.CursoCreateView.as_view(), name="Create"),
    path ('class-update/<int:id>/', class_views.CursoUpdateView.as_view(), name="Update"),
    path ('class-delete/<int:id>/', class_views.CursoDeleteView.as_view(), name="Delete"),

]