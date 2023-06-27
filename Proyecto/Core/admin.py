from django.contrib import admin
from .models import Profesor, Estudiante, Curso, Entregable
# Register your models here.


@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'nombre',
        'camada',
    ]

admin.site.register(Profesor)
admin.site.register(Estudiante)
admin.site.register(Entregable)