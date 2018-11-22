from django  import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Alumno, Profesor

class RegistroForm(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'username',
            'first_name',
            'last_name',
            'email',
            'password',
            'is_active',
            'is_staff'
        ]
        labels = {
            'username': '* Nombre de usuario',
            'first_name': 'Nombre',
            'last_name': 'Apellidos',
            'email': '* Email',
            'password': '* Contraseña',
            
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
            'anioIngreso',
            'anioEgreso',
            'telefono',
            'direccion',
            'semestreCursado',
            'creditos',
            'universidadProcedencia',
            'estadoMatricula'
        ]
        labels = {
            'nombre': 'Nombre de Alumno',
            'apellido_pat': 'Apellido paterno',
            'apellido_mat': 'Apellido materno',
            'rut': 'RUT',
            'sexo': 'Seleccione Sexo',
            'anioIngreso': 'Año de Ingreso',
            'anioEgreso': 'Año de Egreso',
            'telefono': 'Teléfono',
            'direccion': 'Dirreción',
            'semestreCursado': 'Semestre actual del alumno',
            'creditos': 'Ingrese cantidad de créditos',
            'universidadProcedencia': 'Universidad de Procedencia',
            'estadoMatricula': 'Seleccione Estado de Matrícula'
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
 docfile = forms.FileField(
        label='Selecciona un archivo'
    )