from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required

from .models import User, Alumno
from .forms import RegistroForm, AlumnoForm
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView


# Create your views here.

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

@login_required()
def index(request):
    return render(request, 'home.html')

# @login_required()
# def registroAlumno(request):
# 	return render(request, 'registroAlumno.html')

# @login_required()
# def AdministradorArchivo(request):
# 	return render(request, 'AdministradorArchivo.html')

# @login_required()
# def registrar(request):
# 	return render(request, 'registrar.html')

# @login_required()
# def registroAlum(request):
#     if request.method == 'POST':
#         alumno = Alumno()
#         alumno.nombre = request.POST.get('Nombre')
#         alumno.apellido_pat = request.POST.get('Apellido_pat')
#         alumno.apellido_mat = request.POST.get('apellido_mat')
        # alumno.fechaIngreso= request.POST.get('fechaIngreso')


        # tarea.usuario = request.user
        # tarea.fechaInicio = time.strftime("%Y-%m-%d")
        # tarea.fechaTermino = request.POST.get('fechaTermino')
        # tarea.estadoTarea = EstadoTarea.objects.get(pk=request.POST.get('estadoT'))
        # tarea.tipoTarea = TipoTarea.objects.get(pk=request.POST.get('tipoTarea'))
    #     alumno.save()
    # return redirect('registroAlumno')