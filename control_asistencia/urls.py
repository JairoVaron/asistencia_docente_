from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.shortcuts import redirect
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', lambda request: redirect('login')),

    path('inicio/', views.inicio, name='inicio'),

    # DOCENTES
    path('docentes/', views.docentes, name='docentes'),
    path('docentes/nuevo/', views.crear_docente, name='docente_nuevo'),
    path('docentes/editar/<int:id>/', views.docente_editar, name='docente_editar'),
    path('docentes/eliminar/<int:id>/', views.docente_eliminar, name='docente_eliminar'),

    # PROGRAMAS
    path('programas/', views.programas, name='programas'),
    path('programas/nuevo/', views.programa_nuevo, name='programa_nuevo'),
    path('programas/editar/<int:id>/', views.programa_editar, name='programa_editar'),
    path('programas/eliminar/<int:id>/', views.programa_eliminar, name='programa_eliminar'),

    # SEMESTRES
    path('semestres/', views.semestres, name='semestres'),
    path('semestres/nuevo/', views.semestre_nuevo, name='semestre_nuevo'),
    path('semestres/editar/<int:id>/', views.semestre_editar, name='semestre_editar'),
    path('semestres/eliminar/<int:id>/', views.semestre_eliminar, name='semestre_eliminar'),

    # ASISTENCIAS
    path('asistencias/', views.asistencias, name='asistencias'),
    path('asistencias/nueva/', views.asistencia_nueva, name='asistencia_nueva'),
    path('asistencias/editar/<int:id>/', views.asistencia_editar, name='asistencia_editar'),
    path('asistencias/eliminar/<int:id>/', views.asistencia_eliminar, name='asistencia_eliminar'),

    # MATERIAS
    path("materias/", views.materias, name="materias"),
    path("materias/nueva/", views.materia_nueva, name="materia_nueva"),
    path("materias/editar/<int:id>/", views.materia_editar, name="materia_editar"),
    path("materias/eliminar/<int:id>/", views.materia_eliminar, name="materia_eliminar"),

    # ESTADISTICAS
    path("estadisticas/", views.estadisticas, name="estadisticas"),

    # REPORTES
    path("reporte/docente/<int:docente_id>/<int:year>/<int:month>/", views.reporte_mensual_docente, name="reporte_mensual_docente"),

    # LOGIN
    path('login/', views.login_view, name='login'),
    path("logout/", LogoutView.as_view(next_page="login"), name="logout"),

]

