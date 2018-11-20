from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.admin.views.decorators import staff_member_required

urlpatterns = [

#>>>>>>>>>>>>>>>>>>>>>>>>>>> URL DE LOGIN LOGOUT <<<<<<<<<<<<<<<<<<<<<<

    path('login', auth_views.LoginView.as_view(), name='login'),
    path('logout', auth_views.LogoutView.as_view(), name='logout'),
    path('home', views.index, name='home'),
# >>>>>>>>>>>>>>>>>>>>>>>>>>> URL DE USUARIO <<<<<<<<<<<<<<<<<<<<<<<<<<
    path('registrar', views.RegistroUsuario.as_view(), name='registrar'),
    path('Usuarios', views.User, name='Usuarios'),
    path('UsuariosList', views.UsuariosList.as_view(), name='UsuariosList'),
    path('UsuariosList', views.UsuariosDelete.as_view(), name='UsuariosDelete'),
    # path('eliminarUsuario', views.Usuario_eliminar, name='eliminarUsuario'),
    # path('registrar', views.UsuariosUpdate.as_view(), name='UsuariosUpdate'),
    path('<int:pk>', views.UsuarioDelete.as_view(), name='eliminar_usuario'),
    path('editartarea/<int:pk>', views.actualizarUsuario, name='editar_usuario'),



# >>>>>>>>>>>>>>>>>>>>>>>>> URL DE ALUMNO <<<<<<<<<<<<<<<<<<<<<<<<<<<
    path('registroAlumno', views.registroAlumno.as_view(), name='registroAlumno'),
    
# >>>>>>>>>>>>>>>>>>>>>>>>>> URL DE PROFESOR <<<<<<<<<<<<<<<<<<<<<<<<<<

    path('registroProfesor', views.registroProfesor.as_view(), name='registroProfesor'),
    path('DocenteList', views.DocenteList.as_view(), name='DocenteList'),

# >>>>>>>>>>>>>>>>>>>>>>>>>> URL DE SUBIR ARCHIVOS <<<<<<<<<<<<<<<<<<<<<<<<<<

    path('upload', views.upload_file, name="upload"),

]