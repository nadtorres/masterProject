from django.db import models 
from django.contrib.auth.models import User

# Create your models here.


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
	anioIngreso = models.DateField()
	anioEgreso = models.DateField()
	anioGraduacion = models.DateField()
	nivelacion_si = 'Necesita'
	nivelacion_no = 'No necesita'
	nivelacion_choices = (
		(nivelacion_si, u'Necesita'),
		(nivelacion_no, u'No necesita'),
	)
	nivelacion = models.CharField(max_length=15, choices=nivelacion_choices, blank=False)
	equivalencia_si = 'Equivalencia'
	homologacion_si = 'Homologacion'
	ninguno_q = 'Ninguno'
	posee_choices = (
		(equivalencia_si, u'Equivalencia'),
		(homologacion_si, u'Homologacion'),
		(ninguno_q, u'Ninguno'),
	)
	posee = models.CharField(max_length=30, choices=posee_choices, blank=False)
	nivelacion_si = 'Necesita'
	nivelacion_no = 'No necesita'
	nivelacion_q = 'Ninguno'
	nivelacion_choices = (
		(nivelacion_si, u'Necesita'),
		(nivelacion_no, u'No necesita'),
		(nivelacion_q, u'Ninguno')
	)
	nivelacion = models.CharField(max_length=15, choices=nivelacion_choices, blank=False)
	equivalencia_si = 'Equivalencia'
	homologacion_si = 'Homologacion'
	ninguno_si = 'Ninguno'
	posee_choices = (
		(equivalencia_si, u'Equivalencia'),
		(homologacion_si, u'Homologacion'),
		(ninguno_si, u'Ninguno'),	
	)
	telefono = models.IntegerField()
	direccion = models.TextField()
	semestreCursado = models.CharField(max_length=20)
	creditos = models.CharField(max_length=140)
	universidadProcedencia = models.CharField(max_length=40)
	estado_activo = 'Activo'
	estado_inactivo = 'Inactivo'
	estado_choices = (
		(estado_activo, u'Activo'),
		(estado_inactivo, u'Inactivo'),
	)
	estadoMatricula = models.CharField(max_length=9, choices=estado_choices, blank=False)

	def __str__(self):
	    return "%s" % self.sexo

	def __str__(self):
	    return "%s" % self.nombre


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