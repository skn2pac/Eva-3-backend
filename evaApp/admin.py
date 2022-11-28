from django.contrib import admin
from evaApp.models import Alumno

# Register your models here.

class alumnoAdmin(admin.ModelAdmin):
    list_display = ['nombre','email','fono','direccion','ex_liceo','carrera']

admin.site.register(Alumno, alumnoAdmin)
