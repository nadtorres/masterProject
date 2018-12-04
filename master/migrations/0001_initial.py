# Generated by Django 2.1.3 on 2018-12-03 20:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alumno',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('apellido_pat', models.CharField(max_length=10)),
                ('apellido_mat', models.CharField(max_length=10)),
                ('rut', models.CharField(max_length=13)),
                ('sexo', models.CharField(choices=[('Masculino', 'Masculino'), ('Femenino', 'Femenino')], max_length=9)),
                ('email', models.EmailField(blank=True, max_length=70)),
                ('telefono', models.IntegerField()),
                ('direccion', models.CharField(max_length=100)),
                ('universidadProcedencia', models.CharField(max_length=40)),
                ('posee', models.CharField(choices=[('Equivalencia', 'Equivalencia'), ('Homologación', 'Homologación')], max_length=30)),
                ('nivelacion', models.CharField(choices=[('Necesita', 'Necesita'), ('No necesita', 'No necesita')], max_length=15)),
                ('resultadosNivelacion', models.CharField(choices=[('Aprueba', 'Aprueba'), ('Reprueba', 'Reprueba')], max_length=30)),
                ('semestreIngreso', models.IntegerField()),
                ('anioIngreso', models.IntegerField()),
                ('estadoMatricula', models.CharField(choices=[('Activo', 'Activo'), ('Inactivo', 'Inactivo')], max_length=9)),
                ('antecedentesAcademicos', models.IntegerField()),
                ('antecedentesProfesionales', models.IntegerField()),
                ('cartaRecomendacion', models.IntegerField()),
                ('entrevista', models.CharField(max_length=30)),
                ('puntaje', models.IntegerField()),
                ('resultadosCondicion', models.CharField(choices=[('Aprueba', 'Aprueba'), ('Reprueba', 'Reprueba')], max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filename', models.CharField(max_length=100)),
                ('docfile', models.FileField(upload_to='documents/%Y/%m/%d')),
            ],
        ),
        migrations.CreateModel(
            name='Profesor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=40)),
                ('apellido_pat', models.CharField(max_length=10)),
                ('apellido_mat', models.CharField(max_length=10)),
                ('rut', models.CharField(max_length=13)),
                ('sexo', models.CharField(choices=[('Masculino', 'Masculino'), ('Femenino', 'Femenino')], max_length=9)),
                ('telefono', models.IntegerField()),
                ('direccion', models.CharField(max_length=100)),
                ('profesion', models.CharField(max_length=50)),
                ('cursosImpartados', models.CharField(max_length=50)),
            ],
        ),
    ]
