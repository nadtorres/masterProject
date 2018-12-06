from django.urls import path, include
from rest_framework import routers
from rest_framework.routers import DefaultRouter
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.admin.views.decorators import staff_member_required

from django.conf import settings
from django.conf.urls.static import static

router = DefaultRouter()


urlpatterns = [

#>>>>>>>>>>>>>>>>>>>>>>>>>>> URL DE LOGIN LOGOUT <<<<<<<<<<<<<<<<<<<<<<

    path('login', auth_views.LoginView.as_view(), name='login'),
    path('logout', auth_views.LogoutView.as_view(), name='logout'),
    path('home', views.index, name='home'),

    path('editardatos', views.RegistroPerfil.as_view(), name='editardatos'),

# >>>>>>>>>>>>>>>>>>>>>>>>>>> URL DE USUARIO <<<<<<<<<<<<<<<<<<<<<<<<<<
    path('registrar', views.RegistroUsuario.as_view(), name='registrar'),
    path('Usuarios', views.User, name='Usuarios'),
    path('UsuariosList', views.UsuariosList.as_view(), name='UsuariosList'),
    path('UsuariosList', views.UsuariosDelete.as_view(), name='UsuariosDelete'),
    path('<int:pk>', views.UsuarioDelete.as_view(), name='eliminar_usuario'),
    path('editartarea/<int:pk>', views.actualizarUsuario, name='editar_usuario'),
    path('<int:pk>', views.UsuariosDelete.as_view(), name='UsuariosDelete'),
    path('editarUsario/<int:pk>', views.actualizarUsuario, name='editar_usuario'),
    path('perfil', views.PerfilList.as_view(), name='perfil'),
    # path('actualizarFoto/<int:pk>', views.actualizarFoto, name='actualizarFoto'),



# >>>>>>>>>>>>>>>>>>>>>>>>> URL DE ALUMNO <<<<<<<<<<<<<<<<<<<<<<<<<<<
    path('registroAlumno', views.registroAlumno.as_view(), name='registroAlumno'),
    path('alumnosList', views.alumnosList.as_view(), name='alumnosList'),
    path('registroAlumno', views.AlumnoUpdate.as_view(), name='AlumnoUpdate'),
    path('editarAlumno/<int:pk>', views.actualizarAlumno, name='editar_alumno'),
    path('eliminarAlumno/<int:pk>', views.AlumnoDelete.as_view(), name='eliminar_alumno'),

    
# >>>>>>>>>>>>>>>>>>>>>>>>>> URL DE PROFESOR <<<<<<<<<<<<<<<<<<<<<<<<<<

    path('registroProfesor', views.registroProfesor.as_view(), name='registroProfesor'),
    path('DocenteList', views.DocenteList.as_view(), name='DocenteList'),
    path('DocenteList', views.DocenteDelete.as_view(), name='DocenteDelete'),
    path('editarDocente/<int:pk>', views.actualizarDocente, name='editar_docente'),
    path('eliminarDocente/<int:pk>', views.DocenteDelete.as_view(), name='eliminar_docente'),
# >>>>>>>>>>>>>>>>>>>>>>>>>> URL DE SUBIR ARCHIVOS <<<<<<<<<<<<<<<<<<<<<<<<<<

    path('upload', views.upload_file, name="upload"),


# >>>>>>>>>>>>>>>>>>>>>>>>> URL APIS <<<<<<<<<<<<<<<<<<<<<<

    path('api/alumnos', views.alumno_list),
    path('api/profesores', views.profesores_list),
    path('api/users', views.users_list),

# >>>>>>>>>>>>>>>>>>>>>>>>> QUIENES SOMOS <<<<<<<<<<<<<<<<<<<<<<

    path('quienesomos', views.quienesomos, name='quienesomos'),
    path('contacto', views.contacto, name='contacto'),


] 

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_URL)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_URL)
