from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import render_to_response
from .serializers import AlumnoSerializer, ProfesorSerializer, UserSerializer
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt

from .models import Alumno, Profesor
from .models import User, Alumno, Profesor, Document, UserProfile
from .forms import RegistroForm, AlumnoForm, ProfesorForm, UploadForm, PerfilForm
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

@csrf_exempt
def users_list(request):
    if request.method == 'GET':
        users = User.objects.all()
        print (users)
        serializer = UserSerializer(users, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = UserSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializers.errors, status=400)

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

@method_decorator(login_required, name='get')
class PerfilList(ListView):
    model = UserProfile
    template_name = 'perfil.html'
    form_class = PerfilForm
    success_url = reverse_lazy('perfil')
    paginate_by = 10

# CLASES Y FUNCIONES DE ALUMNOS 

@method_decorator(login_required, name='get')
class registroAlumno(CreateView):
    model = Alumno
    template_name = 'registroAlumno.html'
    form_class = AlumnoForm
    success_url = reverse_lazy('registroAlumno')

@method_decorator(login_required, name='get')
class alumnosList(ListView):
    model = Alumno
    template_name = 'alumnosList.html'
    form_class = AlumnoForm
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
    template_name = 'alumnosList.html'
    success_url = reverse_lazy('alumnosList')


@login_required()
def actualizarAlumno(request, pk):
    alumno = Alumno.objects.get(pk=pk)
    if request.method == 'GET':
        form = AlumnoForm(instance=alumno)
    else:
        form = AlumnoForm(request.POST, instance=alumno)
        if form.is_valid():
            form.save()
        return redirect('alumnosList')
    return render(request, 'editar_alumno.html', {'form':form})

@csrf_exempt
def alumno_list(request):
    if request.method == 'GET':
        alumnos = Alumno.objects.all()
        print (alumnos)
        serializer = AlumnoSerializer(alumnos, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = AlumnoSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializers.errors, status=400)


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

@csrf_exempt
def profesores_list(request):
    if request.method == 'GET':
        profesores = Profesor.objects.all()
        print (profesores)
        serializer = ProfesorSerializer(profesores, many=True)
        return JSONResponse(serializer.data)

    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = ProfesorSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return JSONResponse(serializer.data, status=201)
        return JSONResponse(serializers.errors, status=400)

# CLASE PARA SUBIR DOCUMENTOS  
@login_required()
def upload_file(request):
    if request.method == 'POST':
        form = UploadForm(request.POST, request.FILES)
        if form.is_valid():
        	newdoc = Document(filename = request.POST['filename'],docfile = request.FILES['docfile'])
        	newdoc.save(form)
        	return redirect("uploads")
    else:
        form = UploadForm()
    #tambien se puede utilizar render_to_response
    #return render_to_response('upload.html', {'form': form}, context_instance = RequestContext(request))
    return render(request, 'upload.html', {'form': form})


# CLASE DE RETORNO JSONRESPONSE

@method_decorator(login_required, name='get')
class JSONResponse(HttpResponse):
    def __init__(self, data, **kwargs):
        content = JSONRenderer().render(data)
        kwargs['content_type'] = 'application/json'
        super(JSONResponse, self).__init__(content, **kwargs)

@method_decorator(login_required, name='get')
class RegistroPerfil(CreateView):
    model = UserProfile
    template_name = 'foto.html'
    form_class = PerfilForm
    success_url = reverse_lazy('foto')
    success_message = 'Se ha agregado correctamente'



# @login_required()
# def actualizarFoto(request, pk):
#     usuario = User.objects.get(pk=pk)
#     if request.method == 'GET':
#         form = PerfilForm(instance=usuario)
#     else:
#         form = PerfilForm(request.POST, instance=usuario)
#         if form.is_valid():
#             form.save()
#         return redirect('perfil')
#     return render(request, 'perfil.html', {'form':form})


    
# QUIENES SOMOS

@login_required()
def quienesomos(request):
    return render(request, 'quienesomos.html',{})

@login_required()
def contacto(request):
    return render(request, 'contacto.html', {})
