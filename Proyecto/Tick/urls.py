from django.urls import path 

from Tick import views

urlpatterns = [

    path ('Albums/', views.Albums, name='Albums'),
    path ('Tours/', views.Tours, name='Tours'),
    path ('Store/', views.Store, name='Store'),
    path ('Inicio/', views.Inicio, name='Inicio'),
    path ('About/', views.About, name='About'),
    path ('', views.Inicio, name='Inicio')

]