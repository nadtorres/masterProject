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
            'universidadProcedencia',
            'posee',
            'nivelacion',
            'resultadosNivelacion',
            'semestreIngreso',
            'anioIngreso',
            'estadoMatricula',
            'antecedentesAcademicos',
            'antecedentesProfesionales',
            'cartaRecomendacion',
            'entrevista',
            'puntaje',
            'resultadosCondicion'
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
            'universidadProcedencia': 'Universidad de Procedencia',
            'posee': '*Seleccione',
            'nivelacion': '*Nivelación',
            'resultadosNivelacion': 'Seleccione Resultado Nivelación',
            'semestreIngreso': 'Semestre de Ingreso',
            'anioIngreso': '*Año de Ingreso',
            'estadoMatricula': 'Seleccione Estado de Matrícula',
            'antecedentesAcademicos': 'Antecedentes Académicos',
            'antecedentesProfesionales': 'Antecedentes Profesionales',
            'cartaRecomendacion': 'Carta de Recomendación',
            'entrevista': 'Entrevista',
            'puntaje': 'Puntaje',
            'resultadosCondicion': 'Resultado'
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
 nombreArchivo = forms.CharField(max_length=100)
 docfile = forms.FileField(
        label='Selecciona un archivo'
    )