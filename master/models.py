from django.db import models 
from django.contrib.auth.models import User, AbstractUser
from django.db.models.signals import post_save


# Create your models here.

class UserProfile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	imagen = models.ImageField(upload_to='profile_image', blank=True)

	def __str__(self):
		return self.user.username

def create_profile(sender, **kwargs):
	if kwargs['created']:
		user_profile = UserProfile.objects.create(user=kwargs['instance'])

post_save.connect(create_profile, sender=User)

class Alumno(models.Model):
	nombre = models.CharField(max_length=40)
	apellido_pat = models.CharField(max_length=10)
	apellido_mat = models.CharField(max_length=10)
	rut = models.CharField(max_length=13)
	sexo_masculino = 'Masculino'
	sexo_femenino = 'Femenino'
	sexo_choices = (
		(sexo_masculino, u'Masculino'),
		(sexo_femenino, u'Femenino'),
	)
	sexo = models.CharField(max_length=9, choices=sexo_choices, blank=False)
	email = models.EmailField(max_length=70,blank=True)
	telefono = models.IntegerField()
	direccion = models.CharField(max_length=100)
	universidadProcedencia = models.CharField(max_length=40)
	equivalencia_si = 'Equivalencia'
	homologacion_si = 'Homologación'
	ninguno_si = 'No Aplica'
	posee_choices = (
		(equivalencia_si, u'Equivalencia'),
		(homologacion_si, u'Homologación'),
		(ninguno_si, u'No Aplica'),
	)
	posee = models.CharField(max_length=30, choices=posee_choices, blank=False)
	nivelacion_si = 'Necesita'
	nivelacion_no = 'No necesita'
	nivelacion_choices = (
		(nivelacion_si, u'Necesita'),
		(nivelacion_no, u'No necesita'),
	)
	nivelacion = models.CharField(max_length=15, choices=nivelacion_choices, blank=False)
	aprueba = 'Aprueba'
	reprueba = 'Reprueba'
	ninguno_si = 'No Aplica'
	resultado_choices = (
		(aprueba, u'Aprueba'),
		(reprueba, u'Reprueba'),
		(ninguno_si, u'No Aplica'),
	)
	resultadosNivelacion = models.CharField(max_length=30, choices=resultado_choices, blank=False)
	semestreIngreso = models.IntegerField()	
	anioIngreso = models.IntegerField()
	estado_activo = 'Activo'
	estado_inactivo = 'Inactivo'
	estado_choices = (
		(estado_activo, u'Activo'),
		(estado_inactivo, u'Inactivo'),
	)
	estadoMatricula = models.CharField(max_length=9, choices=estado_choices, blank=False)
	antecedentesAcademicos = models.IntegerField()
	antecedentesProfesionales = models.IntegerField()
	cartaRecomendacion = models.IntegerField()
	entrevista = models.CharField(max_length=30)
	puntaje = models.IntegerField()
	aprueba_condicion = 'Aprueba'
	reprueba_condicion = 'Reprueba'
	ninguno_si = 'No Aplica'
	resultadoCondicion_choices = (
		(aprueba_condicion, u'Aprueba'),
		(reprueba_condicion, u'Reprueba'),
		(ninguno_si, u'No Aplica'),
	)
	resultadosCondicion = models.CharField(max_length=30, choices=resultadoCondicion_choices, blank=False)

	def __str__(self):
		cadena = self.nombre+' '+self.apellido_pat+' '+self.apellido_mat
		return cadena 


class Profesor(models.Model):
	nombre = models.CharField(max_length=40)
	apellido_pat = models.CharField(max_length=10)
	apellido_mat = models.CharField(max_length=10)
	rut = models.CharField(max_length=13)
	sexo_masculino = 'Masculino'
	sexo_femenino = 'Femenino'
	sexo_choices = (
		(sexo_masculino, u'Masculino'),
		(sexo_femenino, u'Femenino'),
	)
	sexo = models.CharField(max_length=9, choices=sexo_choices, blank=False)
	telefono = models.IntegerField()
	direccion = models.CharField(max_length=100)
	profesion = models.CharField(max_length=50)
	cursosImpartados = models.CharField(max_length=50)

	def __str__(self):
	    return "%s" % self.sexo

	def __str__(self):
	    return "%s" % self.nombre


class Document(models.Model):
	filename = models.CharField(max_length=100)
	docfile = models.FileField(upload_to='documents/%Y/%m/%d')

	def __str__(self):
	    return "%s" % self.filename