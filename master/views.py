from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from .models import User, Alumno, Profesor, Document
from .forms import RegistroForm, AlumnoForm, ProfesorForm, UploadForm
from django.urls import reverse_lazy
from django.views.generic import CreateView, UpdateView, DetailView, DeleteView, ListView
from django.utils.decorators import method_decorator

# Create your views here.


@login_required()
def index(request):
    return render(request, 'home.html')

# CLASES Y FUNCIONES DE USUARIOS 

@method_decorator(login_required, name='get')
class RegistroUsuario(CreateView):
    model = User
    template_name = 'registration/registrar.html'
    form_class = RegistroForm
    success_url = reverse_lazy('registrar')

@method_decorator(login_required, name='get')
class UsuariosList(ListView):
    model = User
    template_name = 'UsuariosList.html'
    form_class = RegistroForm
    success_url = reverse_lazy('UsuariosList')

@method_decorator(login_required, name='get')
class UsuariosDelete(DeleteView):
    model = User
    template_name = 'eliminarUsuario.html'
    form_class = RegistroForm
    success_url = reverse_lazy('UsuariosList')

# def Usuario_eliminar(request, id):
#     usuario = User.objects.get(id=id)
#     if request.method == 'POST':
#         usuario.delete()
#         return redirect('UsuariosList')
#     return render(request, 'eliminarUsuario.html', {'form':form})

@method_decorator(login_required, name='get')
class UsuarioUpdate(UpdateView):
    model = User
    form_class = RegistroForm
    template_name = 'usuariosList.html'
    success_url = reverse_lazy('usuariosList')

@login_required()
def actualizarUsuario(request, pk):
    usuario = User.objects.get(pk=pk)
    if request.method == 'GET':
        form = RegistroForm(instance=usuario)
    else:
        form = RegistroForm(request.POST, instance=usuario)
        if form.is_valid():
            form.save()
        return redirect('UsuariosList')
    return render(request, 'editar_usuario.html', {'form':form})

@method_decorator(login_required, name='get')
class UsuarioDelete(DeleteView):
    model = User
    template_name = 'eliminarUsuario.html'
    success_url = reverse_lazy('UsuariosList')

# CLASES Y FUNCIONES DE ALUMNOS 

@method_decorator(login_required, name='get')
class registroAlumno(CreateView):
    model = Alumno
    template_name = 'registroAlumno.html'
    form_class = AlumnoForm
    success_url = reverse_lazy('registroAlumno')
    def get_queryset(self, *args, **kwargs):
        return Alumno.objects.filter(user=request.user)

@method_decorator(login_required, name='get')
class alumnosList(ListView):
    model = Profesor
    template_name = 'alumnosList.html'
    form_class = ProfesorForm
    success_url = reverse_lazy('alumnosList')

@method_decorator(login_required, name='get')
class AlumnoDelete(DeleteView):
    model = Alumno
    template_name = 'eliminarAlumno.html'
    success_url = reverse_lazy('AlumnoList')


@method_decorator(login_required, name='get')
class AlumnoUpdate(UpdateView):
    model = Alumno
    form_class = AlumnoForm
    template_name = 'AlumnoList.html'
    success_url = reverse_lazy('AlumnoList')


@login_required()
def actualizarAlumno(request, pk):
    alumno = Alumno.objects.get(pk=pk)
    if request.method == 'GET':
        form = AlumnoForm(instance=alumno)
    else:
        form = AlumnoForm(request.POST, instance=alumno)
        if form.is_valid():
            form.save()
        return redirect('AlumnoList')
    return render(request, 'editar_alumno.html', {'form':form})


# CLASES Y FUNCIONES DE PROFESORES

@method_decorator(login_required, name='get')
class registroProfesor(CreateView):
    model = Profesor
    template_name = 'registroProfesor.html'
    form_class = ProfesorForm
    success_url = reverse_lazy('registroProfesor')

@method_decorator(login_required, name='get')
class DocenteList(ListView):
    model = Profesor
    template_name = 'DocenteList.html'
    form_class = ProfesorForm
    success_url = reverse_lazy('DocenteList')

@method_decorator(login_required, name='get')
class DocenteUpdate(UpdateView):
    model = Profesor
    form_class = ProfesorForm
    template_name = 'DocenteList.html'
    success_url = reverse_lazy('DocenteList')

@login_required()
def actualizarDocente(request, pk):
    docente = Profesor.objects.get(pk=pk)
    if request.method == 'GET':
        form = ProfesorForm(instance=docente)
    else:
        form = ProfesorForm(request.POST, instance=docente)
        if form.is_valid():
            form.save()
        return redirect('DocenteList')
    return render(request, 'editar_docente.html', {'form':form})


@method_decorator(login_required, name='get')
class DocenteDelete(DeleteView):
    model = Profesor
    template_name = 'eliminarDocente.html'
    success_url = reverse_lazy('DocenteList')

# CLASE PARA SUBIR DOCUMENTOS  
@login_required()
def upload_file(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
        	newdoc = Document(filename = request.POST['filename'],docfile = request.FILES['docfile'])
        	newdoc.save(form)
        	return redirect("upload")
    else:
        form = UploadForm()
    #tambien se puede utilizar render_to_response
    #return render_to_response('upload.html', {'form': form}, context_instance = RequestContext(request))
    return render(request, 'upload.html', {'form': form})