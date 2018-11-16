from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from .models import User
from .forms import RegistroForm
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView


# Create your views here.

class RegistroUsuario(CreateView):
    model = User
    template_name = 'registration/registrar.html'
    form_class = RegistroForm
    success_url = reverse_lazy('registrar')

@login_required()
def index(request):
    return render(request, 'home.html')

@login_required()
def registroAlumno(request):
	return render(request, 'registroAlumno.html')

@login_required()
def AdministradorArchivo(request):
	return render(request, 'AdministradorArchivo.html')

# @login_required()
# def registrar(request):
# 	return render(request, 'registrar.html')
