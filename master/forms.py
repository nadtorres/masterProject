from django  import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import Alumno

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
            'username': 'Nombre de usuario',
            'first_name': 'Nombre',
            'last_name': 'Apellidos',
            'email': 'Email',
            

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
