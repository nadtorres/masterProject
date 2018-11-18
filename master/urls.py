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

# >>>>>>>>>>>>>>>>>>>>>>>>> URL DE ALUMNO <<<<<<<<<<<<<<<<<<<<<<<<<<<
    path('registroAlumno', views.registroAlumno.as_view(), name='registroAlumno'),
    
# >>>>>>>>>>>>>>>>>>>>>>>>>> URL DE PROFESOR <<<<<<<<<<<<<<<<<<<<<<<<<<

    path('registroProfesor', views.registroProfesor.as_view(), name='registroProfesor'),
    path('DocenteList', views.DocenteList.as_view(), name='DocenteList'),



]