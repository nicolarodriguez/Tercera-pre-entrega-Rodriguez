from django.urls import path
from App import views

urlpatterns = [
    path('', views.buscar_curso, name="BuscarCursos"),
    path("listar/", views.listar, name="ListarCursos"),
    path("cursos/", views.form_curso, name="Cursos"),
    path("profesores/", views.form_profe, name="Profesores"),
    path("estudiantes/", views.form_estudiante, name="Estudiantes"),
    path("entregables/", views.form_entregable, name="Entregables")
]