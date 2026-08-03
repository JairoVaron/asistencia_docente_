from django.shortcuts import render, redirect, get_object_or_404
from .models import Docente, Programa, Semestre, Asistencia, Materia
from .forms import DocenteForm, ProgramaForm, SemestreForm, AsistenciaForm, MateriaForm, LoginForm
from django.db.models import Count, Q
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib.pagesizes import letter
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from django.http import HttpResponse
from datetime import datetime
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django import forms
from .decorators import admin_required


# ==============================
#          PÁGINA INICIO
# ==============================
@login_required
def inicio(request):
    if request.user.is_superuser:
        return render(request, "admin_dashboard.html")
    else:
        docente = Docente.objects.get(user=request.user)
        return render(request, "docente_dashboard.html", {"docente": docente})


# ==============================
#       DOCENTES
# ==============================
@login_required
@admin_required
def docentes(request):

    # BLOQUEAR SI NO ES ADMIN
    if not request.user.is_superuser:
        return redirect("asistencias")

    busqueda = request.GET.get("busqueda", "")
    programa_id = request.GET.get("programa", "")

    docentes = Docente.objects.all()

    if busqueda:
        docentes = docentes.filter(nombre__icontains=busqueda)

    if programa_id:
        docentes = docentes.filter(programa_id=programa_id)

    programas = Programa.objects.all()

    return render(request, "control_asistencia/docentes.html", {
        "docentes": docentes,
        "programas": programas,
    })

@login_required
@admin_required
def crear_docente(request):
    if request.method == "POST":
        form = DocenteForm(request.POST)

        if form.is_valid():
            docente = form.save(commit=False)

            # username = documento
            username = docente.documento  

            # Validación por si intenta crear un usuario repetido
            if User.objects.filter(username=username).exists():
                return render(request, "control_asistencia/form_docente.html", {
                    "form": form,
                    "error": "Ya existe un usuario con ese documento"
                })

            # Crear usuario
            user = User.objects.create_user(
                username=username,
                password=docente.documento,   # contraseña = documento
                email=docente.email,
                first_name=docente.nombre,
                last_name=docente.apellido
            )

            docente.user = user
            docente.save()

            return redirect("docentes")

    else:
        form = DocenteForm()

    return render(request, "control_asistencia/form_docente.html", {"form": form})

@login_required
@admin_required
def docente_editar(request, id):
    if not request.user.is_superuser:
        return redirect("asistencias")

    docente = get_object_or_404(Docente, id=id)
    if request.method == "POST":
        form = DocenteForm(request.POST, instance=docente)
        if form.is_valid():
            form.save()
            return redirect("docentes")
    else:
        form = DocenteForm(instance=docente)
    return render(request, "control_asistencia/form_docente.html", {"form": form})

@login_required
@admin_required
def docente_eliminar(request, id):
    if not request.user.is_superuser:
        return redirect("asistencias")

    docente = get_object_or_404(Docente, id=id)
    docente.delete()
    return redirect("docentes")


# ==============================
#       PROGRAMAS
# ==============================
@login_required
@admin_required
def programas(request):
    if not request.user.is_superuser:
        return redirect("asistencias")

    lista = Programa.objects.all()
    return render(request, "control_asistencia/programas.html", {"programas": lista})

@login_required
@admin_required
def programa_nuevo(request):
    if not request.user.is_superuser:
        return redirect("asistencias")

    if request.method == "POST":
        form = ProgramaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("programas")
    else:
        form = ProgramaForm()
    return render(request, "control_asistencia/form_programa.html", {"form": form})

@login_required
@admin_required
def programa_editar(request, id):
    if not request.user.is_superuser:
        return redirect("asistencias")

    programa = get_object_or_404(Programa, id=id)
    if request.method == "POST":
        form = ProgramaForm(request.POST, instance=programa)
        if form.is_valid():
            form.save()
            return redirect("programas")
    else:
        form = ProgramaForm(instance=programa)
    return render(request, "control_asistencia/form_programa.html", {"form": form})

@login_required
@admin_required
def programa_eliminar(request, id):
    if not request.user.is_superuser:
        return redirect("asistencias")

    programa = get_object_or_404(Programa, id=id)
    programa.delete()
    return redirect("programas")


# ==============================
#       SEMESTRES
# ==============================
@login_required
@admin_required
def semestres(request):
    if not request.user.is_superuser:
        return redirect("asistencias")

    lista = Semestre.objects.all()
    return render(request, "control_asistencia/semestres.html", {"semestres": lista})

@login_required
@admin_required
def semestre_nuevo(request):
    if not request.user.is_superuser:
        return redirect("asistencias")

    if request.method == "POST":
        form = SemestreForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("semestres")
    else:
        form = SemestreForm()
    return render(request, "control_asistencia/form_semestre.html", {"form": form})

@login_required
@admin_required
def semestre_editar(request, id):
    if not request.user.is_superuser:
        return redirect("asistencias")

    semestre = get_object_or_404(Semestre, id=id)
    if request.method == "POST":
        form = SemestreForm(request.POST, instance=semestre)
        if form.is_valid():
            form.save()
            return redirect("semestres")
    else:
        form = SemestreForm(instance=semestre)
    return render(request, "control_asistencia/form_semestre.html", {"form": form})

@login_required
@admin_required
def semestre_eliminar(request, id):
    if not request.user.is_superuser:
        return redirect("asistencias")

    semestre = get_object_or_404(Semestre, id=id)
    semestre.delete()
    return redirect("semestres")


# ==============================
#       ASISTENCIAS
# ==============================
@login_required
def asistencias(request):

    # ==============================
    #   FILTRAR SEGÚN EL USUARIO
    # ==============================
    
    # Si es superusuario → ve todas
    if request.user.is_superuser:
        asistencias = Asistencia.objects.select_related("docente", "semestre")
    else:
        # Si es docente → solo ve sus asistencias
        asistencias = Asistencia.objects.select_related("docente", "semestre").filter(
            docente__user=request.user
        )

    # ==============================
    #      FILTROS YA EXISTENTES
    # ==============================
    docente_id = request.GET.get("docente")
    semestre_id = request.GET.get("semestre")
    programa_id = request.GET.get("programa")
    desde = request.GET.get("desde")
    hasta = request.GET.get("hasta")
    materia = request.GET.get("materia")
    jornada = request.GET.get("jornada")
    estado = request.GET.get("estado")

    if docente_id:
        asistencias = asistencias.filter(docente_id=docente_id)
    if semestre_id:
        asistencias = asistencias.filter(semestre_id=semestre_id)
    if programa_id:
        asistencias = asistencias.filter(docente__programa_id=programa_id)
    if desde:
        asistencias = asistencias.filter(fecha__gte=desde)
    if hasta:
        asistencias = asistencias.filter(fecha__lte=hasta)
    if materia:
        asistencias = asistencias.filter(materia__icontains=materia)
    if jornada:
        asistencias = asistencias.filter(jornada=jornada)
    if estado == "presente":
        asistencias = asistencias.filter(presente=True)
    elif estado == "ausente":
        asistencias = asistencias.filter(presente=False)

    # Consultas auxiliares solo para mostrar
    docentes = Docente.objects.all()
    semestres = Semestre.objects.all()
    programas = Programa.objects.all()

    return render(
        request,
        "control_asistencia/asistencias.html",
        {
            "asistencias": asistencias,
            "docentes": docentes,
            "semestres": semestres,
            "programas": programas,
        }
    )


def asistencia_nueva(request):
    if request.method == "POST":
        form = AsistenciaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("asistencias")
    else:
        form = AsistenciaForm()
    return render(request, "control_asistencia/form_asistencia.html", {"form": form})


def asistencia_editar(request, id):
    asistencia = get_object_or_404(Asistencia, id=id)
    if request.method == "POST":
        form = AsistenciaForm(request.POST, instance=asistencia)
        if form.is_valid():
            form.save()
            return redirect("asistencias")
    else:
        form = AsistenciaForm(instance=asistencia)
    return render(request, "control_asistencia/form_asistencia.html", {"form": form})


def asistencia_eliminar(request, id):
    asistencia = get_object_or_404(Asistencia, id=id)
    asistencia.delete()
    return redirect("asistencias")


# ==============================
#       MATERIAS
# ==============================
@login_required
@admin_required
def materias(request):
    if not request.user.is_superuser:
        return redirect("asistencias")

    materias = Materia.objects.all()
    return render(request, "control_asistencia/materias.html", {"materias": materias})

@login_required
@admin_required
def materia_nueva(request):
    if not request.user.is_superuser:
        return redirect("asistencias")

    if request.method == "POST":
        form = MateriaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("materias")
    else:
        form = MateriaForm()
    return render(request, "control_asistencia/form_materia.html", {"form": form})

@login_required
@admin_required
def materia_editar(request, id):
    if not request.user.is_superuser:
        return redirect("asistencias")

    materia = get_object_or_404(Materia, id=id)
    if request.method == "POST":
        form = MateriaForm(request.POST, instance=materia)
        if form.is_valid():
            form.save()
            return redirect("materias")
    else:
        form = MateriaForm(instance=materia)
    return render(request, "control_asistencia/form_materia.html", {"form": form})

@login_required
@admin_required
def materia_eliminar(request, id):
    if not request.user.is_superuser:
        return redirect("asistencias")

    materia = get_object_or_404(Materia, id=id)
    materia.delete()
    return redirect("materias")


# ==============================
#       ESTADÍSTICAS
# ==============================
@login_required
@admin_required
def estadisticas(request):
    if not request.user.is_superuser:
        return redirect("asistencias")

    total_presentes = Asistencia.objects.filter(presente=True).count()
    total_ausentes = Asistencia.objects.filter(presente=False).count()
    asistencias_por_dia = (
        Asistencia.objects.values("fecha")
        .annotate(total=Count("id"))
        .order_by("fecha")
    )
    asistencias_por_docente = (
        Docente.objects.annotate(total=Count("asistencias"))
        .order_by("-total")[:10]
    )
    asistencias_por_programa = (
        Programa.objects.annotate(total=Count("docentes__asistencias"))
        .order_by("-total")
    )

    return render(
        request,
        "control_asistencia/estadisticas.html",
        {
            "total_presentes": total_presentes,
            "total_ausentes": total_ausentes,
            "asistencias_por_dia": asistencias_por_dia,
            "asistencias_por_docente": asistencias_por_docente,
            "asistencias_por_programa": asistencias_por_programa,
        }
    )


# ==============================
#       REPORTES
# ==============================
def reporte_mensual_docente(request, docente_id, year, month):
    docente = get_object_or_404(Docente, id=docente_id)

    asistencias = Asistencia.objects.filter(
        docente=docente,
        fecha__year=year,
        fecha__month=month
    ).order_by("fecha")

    response = HttpResponse(content_type="application/pdf")
    filename = f"reporte_{docente.nombre}_{month}_{year}.pdf"
    response["Content-Disposition"] = f'attachment; filename="{filename}"'

    pdf = SimpleDocTemplate(response, pagesize=letter)
    styles = getSampleStyleSheet()
    elements = []

    titulo = Paragraph(
        f"<b>REPORTE MENSUAL DE ASISTENCIA</b><br/>{docente.nombre} {docente.apellido}<br/>{month}/{year}",
        styles["Title"]
    )
    elements.append(titulo)
    elements.append(Paragraph("<br/>", styles["Normal"]))

    data = [["Fecha", "Entrada", "Salida", "Materia", "Tema", "Estado"]]
    for a in asistencias:
        data.append([
            a.fecha.strftime("%Y-%m-%d"),
            a.hora_entrada.strftime("%H:%M") if a.hora_entrada else "-",
            a.hora_salida.strftime("%H:%M") if a.hora_salida else "-",
            a.materia or "-",
            a.tema or "-",
            "Presente" if a.presente else "Ausente"
        ])

    table = Table(data, repeatRows=1)
    table.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,0), colors.lightgrey),
        ("GRID", (0,0), (-1,-1), 1, colors.black),
        ("FONT", (0,0), (-1,-1), "Helvetica", 10),
        ("ALIGN", (0,0), (-1,-1), "CENTER"),
    ]))
    elements.append(table)
    pdf.build(elements)
    return response


# ==============================
#       LOGIN
# ==============================
def login_view(request):
    form = LoginForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        usuario = form.cleaned_data["usuario"]
        contraseña = form.cleaned_data["contraseña"]

        user = authenticate(request, username=usuario, password=contraseña)

        if user:
            login(request, user)

            # Si es admin va al panel admin
            if user.is_superuser:
                return redirect("docentes")

            # Si es docente va a asistencias
            return redirect("asistencias")

        return render(request, "login.html", {
            "form": form,
            "error": "Usuario o contraseña incorrecto"
        })

    return render(request, "login.html", {"form": form})


