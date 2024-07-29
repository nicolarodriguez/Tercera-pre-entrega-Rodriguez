from django.shortcuts import render
from App.models import Curso, Profesores, Estudiantes, Entregable
from App.forms import CursoFormulario, ProfeFormulario, EstudiantesFormulario, EntregableFormulario, BuscarCursoFormulario
# Create your views here.
def inicio(request):
    return render(request, "app/index.html")

def listar(request):
    cursos = Curso.objects.all()
    return render(request, "app/listar.html", {"cursos": cursos})

def cursos(request):
    return render(request,"app/form_curso.html")

def profesores(request):
    return render(request,"app/profesores.html")

def estudiantes(request):
    return render(request,"app/estudiantes.html")

def entregables(request):
    return render(request,"app/entregables.html")

def form_curso(request):
    if request.method == "POST":
        FormularioDeCurso = CursoFormulario(request.POST)
        if FormularioDeCurso.is_valid():
            informacion = FormularioDeCurso.cleaned_data
            
            curso = Curso(curso=informacion["curso"], camada=informacion["camada"])
            curso.save()
    else:
        FormularioDeCurso = CursoFormulario()
        
    return render(request, "app/form_curso.html", {"FormularioDeCurso": FormularioDeCurso})                
    
def form_profe(request):
    if request.method == "POST":
        FormularioDeProfe = ProfeFormulario(request.POST)
        if FormularioDeProfe.is_valid():
            informacion = FormularioDeProfe.cleaned_data
            
            profe = Profesores(nombre=informacion["nombre"], apellido=informacion["apellido"], email=informacion["email"], profesion=informacion["profesion"])
            profe.save()
    else:
        FormularioDeProfe = ProfeFormulario()
        
    return render(request, "app/form_profe.html", {"FormularioDeProfe": FormularioDeProfe})

def form_estudiante(request):
    if request.method == "POST":
        FormularioDeEstudiante = EstudiantesFormulario(request.POST)
        if FormularioDeEstudiante.is_valid():
            informacion = FormularioDeEstudiante.cleaned_data
            
            estudiante = Estudiantes(nombre=informacion["nombre"], apellido=informacion["apellido"], email=informacion["email"])
            estudiante.save()
    else:
        FormularioDeEstudiante = EstudiantesFormulario()
        
    return render(request, "app/form_estudiante.html", {"FormularioDeEstudiante": FormularioDeEstudiante})

def form_entregable(request):
    if request.method == "POST":
        FormularioDeEntregable = EntregableFormulario(request.POST)
        if FormularioDeEntregable.is_valid():
            informacion = FormularioDeEntregable.cleaned_data
            
            entregable = Entregable(nombre=informacion["nombre"], fechaDeEntrega=informacion["fechaDeEntrega"], entregado=informacion["entregado"])
            entregable.save()
    else:
        FormularioDeEntregable = EntregableFormulario()
        
    return render(request, "app/form_entregable.html", {"FormularioDeEntregable": FormularioDeEntregable})        

def buscar_curso(request):
    CursoFormulario = BuscarCursoFormulario(request.POST or None)
    cursos = None
    
    if request.method == "POST" and CursoFormulario.is_valid():
        camada = CursoFormulario.cleaned_data["camada"]
        cursos = Curso.objects.filter(camada=camada)
        
    return render(request, "app/resultados_busqueda.html", {"CursoFormulario": CursoFormulario, "cursos": cursos})              