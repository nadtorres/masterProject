from django.conf import settings
from rest_framework import serializers
from .models import Alumno, Profesor, User

    # If your <field_name> is declared on your serializer with the parameter required=False
    # then this validation step will not take place if the field is not included.

    #last_modify_date = serializers.DateTimeField(format=settings.DATETIME_FORMAT, required=False)
    #created = serializers.DateTimeField(format=settings.DATE_FORMAT, required=False)

    #class Meta:
     #   model = Alumno
        #fields = '__all__'
      #  fields = ('nombre', 'apellido_pat', 'last_modify_date', 'created')

class AlumnoSerializer(serializers.ModelSerializer):
	class Meta:
		model = Alumno
		fields = '__all__'
		#fields = ('id', 'nombre', 'apellido_pat', 'apellido_mat', 'rut' , 'sexo' , 'email' ,'telefono','direccion' ,'universidadProcedencia','posee','nivelacion','resultadosNivelacion' ,'semestreIngreso','anioIngreso' ,'estadoMatricula' ,'antecedentesAcademicos','antecedentesProfesionales' ,'cartaRecomendacion','entrevista','puntaje','resultadosCondicion')

class ProfesorSerializer(serializers.ModelSerializer):
  class Meta:
    model = Profesor
    fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
  class Meta:
    model = User
    fields = '__all__'