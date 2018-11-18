from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from .models import User, Alumno, Profesor
from .forms import RegistroForm, AlumnoForm, ProfesorForm
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView, ListView


# Create your views here.


@login_required()
def index(request):
    return render(request, 'home.html')

class RegistroUsuario(CreateView):
    model = User
    template_name = 'registration/registrar.html'
    form_class = RegistroForm
    success_url = reverse_lazy('registrar')

class registroAlumno(CreateView):
    model = Alumno
    template_name = 'registroAlumno.html'
    form_class = AlumnoForm
    success_url = reverse_lazy('registroAlumno')

class UsuariosList(ListView):
    model = User
    template_name = 'UsuariosList.html'
    form_class = RegistroForm
    success_url = reverse_lazy('UsuariosList')

# CLASES Y FUNCIONES DE PROFESORES

class registroProfesor(CreateView):
    model = Profesor
    template_name = 'registroProfesor.html'
    form_class = ProfesorForm
    success_url = reverse_lazy('registroProfesor')

class DocenteList(ListView):
    model = Profesor
    template_name = 'DocenteList.html'
    form_class = ProfesorForm
    success_url = reverse_lazy('DocenteList')


