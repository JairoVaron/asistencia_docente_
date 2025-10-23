from django.contrib import admin
from .models import Docente, Asistencia

@admin.register(Docente)
class DocenteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'identificacion', 'correo', 'materia')
    search_fields = ('nombre', 'apellido', 'identificacion', 'materia')
    list_filter = ('materia',)

@admin.register(Asistencia)
class AsistenciaAdmin(admin.ModelAdmin):
    list_display = ('docente', 'fecha', 'hora_entrada', 'hora_salida', 'observaciones')
    list_filter = ('fecha', 'docente')
    search_fields = ('docente__nombre', 'docente__apellido')

