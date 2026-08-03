# control_asistencia/admin.py
from django.contrib import admin
from .models import Programa, Semestre, Docente, Asistencia

@admin.register(Programa)
class ProgramaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'codigo')
    search_fields = ('nombre', 'codigo')


@admin.register(Semestre)
class SemestreAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'fecha_inicio', 'fecha_fin')
    search_fields = ('nombre',)


@admin.register(Docente)
class DocenteAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'apellido', 'documento', 'programa')
    list_filter = ('programa',)
    search_fields = ('nombre', 'apellido', 'documento')


@admin.register(Asistencia)
class AsistenciaAdmin(admin.ModelAdmin):
    list_display = ('docente', 'fecha', 'presente', 'semestre')
    list_filter = ('presente', 'semestre')
    search_fields = ('docente__nombre', 'docente__apellido')
    date_hierarchy = 'fecha'
