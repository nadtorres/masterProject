from django  import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Alumno, Profesor, UserProfile

class RegistroForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'is_active',
            'is_staff',
            
        ]
        labels = {
            'username': '* Nombre de usuario',
            'first_name': 'Nombre',
            'last_name': 'Apellidos',
            'email': '* Email',
            
        }

class PerfilForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = [
            'imagen'
        ]
        labels = {
            'imagen': 'Seleccione una imagen'
        }
        
class AlumnoForm(forms.ModelForm):
    class Meta:
        model = Alumno
        fields = [
            'nombre',
            'apellido_pat',
            'apellido_mat',
            'rut',
            'sexo',
            'email',
            'telefono',
            'direccion',
            'universidad_procedencia',
            'posee',
            'nivelacion',
            'resultados_nivelacion',
            'semestre_ingreso',
            'anio_ingreso',
            'estado_matricula',
            'antecedentes_academicos',
            'antecedentes_profesionales',
            'carta_recomendacion',
            'entrevista',
            'puntaje',
            'resultados_condicion'
        ]
        labels = {
            'nombre': '*Nombre de Alumno',
            'apellido_pat': '*Apellido paterno',
            'apellido_mat': '*Apellido materno',
            'rut': '*RUT',
            'sexo': 'Seleccione Sexo',
            'email': 'Email',
            'telefono': '*Teléfono',
            'direccion': 'Dirección',
            'universidad_procedencia': 'Universidad de Procedencia',
            'posee': '*Seleccione',
            'nivelacion': '*Nivelación',
            'resultados_nivelacion': 'Seleccione Resultado Nivelación',
            'semestre_ingreso': 'Semestre de Ingreso',
            'anio_ingreso': '*Año de Ingreso',
            'estado_matricula': 'Seleccione Estado de Matrícula',
            'antecedentes_academicos': 'Antecedentes Académicos',
            'antecedentes_profesionales': 'Antecedentes Profesionales',
            'carta_recomendacion': 'Carta de Recomendación',
            'entrevista': 'Entrevista',
            'puntaje': 'Puntaje',
            'resultados_condicion': 'Resultado'
        }

class ProfesorForm(forms.ModelForm):
    class Meta:
        model = Profesor
        fields = [
            'nombre',
            'apellido_pat',
            'apellido_mat',
            'rut',
            'sexo',
            'telefono',
            'direccion',
            'profesion',
            'cursosImpartados'
        ]
        labels = {
            'nombre': 'Nombre de Docente',
            'apellido_pat': 'Apellido Paterno',
            'apellido_mat': 'Apellido Materno',
            'rut': 'RUT',
            'sexo': 'Seleccione Sexo',
            'telefono': 'Teléfono',
            'direccion': 'Dirección',
            'profesion': 'Ingrese profesión del Docente',
            'cursosImpartados': 'Seleccione cursos que imparte el Docente'
        }

 
class UploadForm(forms.Form):
 filename = forms.CharField(max_length=100)
 file = forms.FileField(
     label='Selecciona un Archivo'
 )
 fields=['filename', 'docfile']

 def clean(self):
     print (self.cleaned_data)
     return self.cleaned_data
