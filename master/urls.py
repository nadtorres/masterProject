from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.admin.views.decorators import staff_member_required

urlpatterns = [
    path('login', auth_views.LoginView.as_view(), name='login'),
    path('logout', auth_views.LogoutView.as_view(), name='logout'),
    path('home', views.index, name='home'),
    # path('Archivo', views.Archivo, name='Archivo'),
    path('registrar', views.RegistroUsuario.as_view(), name='registrar'),
    path('registroAlumno', views.registroAlumno.as_view(), name='registroAlumno'),
    path('Usuarios', views.User, name='Usuarios'),
    # path('registroAlumno', views.registroAlumno, name='registroAlumno'),




]