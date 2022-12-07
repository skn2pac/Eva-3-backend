from django.contrib import admin
from evaApp.models import Alumno, Docente, Sala, Seccion, DirectorC

# Register your models here.

class alumnoAdmin(admin.ModelAdmin):
  list_display = ['nombre','apellido','email','fono','direccion','ex_liceo','carrera']

class DocenteAdmin(admin.ModelAdmin):
  list_display = ['nombre', 'apellido', 'fono', 'nivelAcademico', 'anos_exp', 'especialidad']


class SalaAdmin(admin.ModelAdmin):
  list_display = ['cod_sala','cod_seccion']

# class SeccionAdmin(admin.ModelAdmin):
#   list_display = ['cod_seccion','docente_cargo','alumno_asignado']

# class directorCAdmin(admin.ModelAdmin):
#   list_display = ['nombre','apellido','rut','seccion_cargo']

admin.site.register(DirectorC)#,directorCAdmin)
admin.site.register(Alumno, alumnoAdmin)
admin.site.register(Docente, DocenteAdmin)
admin.site.register(Sala, SalaAdmin)
admin.site.register(Seccion)#, SeccionAdmin)