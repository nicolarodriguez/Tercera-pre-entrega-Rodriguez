from django.contrib import admin
from App.models import Curso, Profesores, Entregable, Estudiantes

# Register your models here.
admin.site.register(Curso)
admin.site.register(Profesores)
admin.site.register(Entregable)
admin.site.register(Estudiantes)