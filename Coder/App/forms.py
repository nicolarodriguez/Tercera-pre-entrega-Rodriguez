from django import forms

class CursoFormulario(forms.Form):
    curso = forms.CharField(max_length=50)
    camada = forms.IntegerField()
    
class ProfeFormulario(forms.Form):
    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)    
    email = forms.EmailField()
    profesion = forms.CharField(max_length=50)
    
class EstudiantesFormulario(forms.Form):
    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    email = forms.EmailField()
    
class EntregableFormulario(forms.Form):
    nombre = forms.CharField(max_length=50)
    fechaDeEntrega = forms.DateField()
    entregado = forms.BooleanField()     
    
class BuscarCursoFormulario(forms.Form):
    camada = forms.IntegerField(label="Camada")       