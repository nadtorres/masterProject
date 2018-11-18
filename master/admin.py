from django.contrib import admin
from .models import *

# Register your models here.
admin.site.site_header="Master Project"
admin.site.site_title="Master Project"

admin.site.register(Alumno)
admin.site.register(Profesor)
