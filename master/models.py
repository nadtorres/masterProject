from django.db import models 
from django.contrib.auth.models import User, AbstractUser
from django.db.models.signals import post_save



# Create your models here.

class UserProfile(models.Model):
	user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
	imagen = models.ImageField(upload_to='static/img', null=True)


class Alumno(models.Model):
	nombre = models.CharField(max_length=40, null=True)
	apellido_pat = models.CharField(max_length=40, null=True)
	apellido_mat = models.CharField(max_length=40, null=True)
	rut = models.CharField(max_length=13, null=True)
	sexo_masculino = 'Masculino'
	sexo_femenino = 'Femenino'
	sexo_choices = (
		(sexo_masculino, u'Masculino'),
		(sexo_femenino, u'Femenino'),
	)
	sexo = models.CharField(max_length=20, choices=sexo_choices, blank=True, null=True)
	email = models.EmailField(max_length=70,blank=True, null=True)
	telefono = models.IntegerField(blank=False, null=True)
	direccion = models.CharField(max_length=100, null=True)
	universidad_procedencia = models.CharField(max_length=40, null=True)
	equivalencia_si = 'Equivalencia'
	homologacion_si = 'Homologación'
	posee_choices = (
		(equivalencia_si, u'Equivalencia'),
		(homologacion_si, u'Homologación'),
	)
	posee = models.CharField(max_length=30, choices=posee_choices, blank=False, null=True)
	nivelacion_si = 'Necesita'
	nivelacion_no = 'No necesita'
	nivelacion_choices = (
		(nivelacion_si, u'Necesita'),
		(nivelacion_no, u'No necesita'),
	)
	nivelacion = models.CharField(max_length=30, choices=nivelacion_choices, blank=False, null=True)
	aprueba = 'Aprueba'
	reprueba = 'Reprueba'
	resultado_choices = (
		(aprueba, u'Aprueba'),
		(reprueba, u'Reprueba')
	)
	resultados_nivelacion = models.CharField(max_length=30, choices=resultado_choices, blank=False, null=True)
	semestre_ingreso = models.IntegerField(null=True)	
	anio_ingreso = models.IntegerField(null=True)
	estado_activo = 'Activo'
	estado_inactivo = 'Inactivo'
	estado_choices = (
		(estado_activo, u'Activo'),
		(estado_inactivo, u'Inactivo'),
	)
	estado_matricula = models.CharField(max_length=20, choices=estado_choices, blank=False, null=True)
	antecedentes_academicos = models.IntegerField(null=True)
	antecedentes_profesionales = models.IntegerField(null=True)
	carta_recomendacion = models.IntegerField(null=True)
	entrevista = models.CharField(max_length=30, null=True)
	puntaje = models.IntegerField(null=True)
	aprueba_condicion = 'Aprueba'
	reprueba_condicion = 'Reprueba'
	resultadoCondicion_choices = (
		(aprueba_condicion, u'Aprueba'),
		(reprueba_condicion, u'Reprueba')
	)
	resultados_condicion = models.CharField(max_length=30, choices=resultadoCondicion_choices, blank=False)

	def _str_(self):
		cadena = self.nombre
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
		cadena = self.nombre+''+self.apellido_pat+''+self.apellido_mat
		return cadena

class Document(models.Model):
	filename = models.CharField(max_length=100, blank=True)
	docfile = models.FileField(upload_to='documents/%Y/%m/%d')

	def __str__(self):
	    return "%s" % self.filename


