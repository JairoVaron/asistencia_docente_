from django import forms
from .models import Docente, Programa, Semestre, Asistencia, Materia

class DocenteForm(forms.ModelForm):
    class Meta:
        model = Docente
        fields = ['nombre', 'apellido', 'documento', 'programa']

class ProgramaForm(forms.ModelForm):
    class Meta:
        model = Programa
        fields = ['nombre', 'codigo']

class SemestreForm(forms.ModelForm):
    class Meta:
        model = Semestre
        fields = ['nombre', 'fecha_inicio', 'fecha_fin']

class AsistenciaForm(forms.ModelForm):
    class Meta:
        model = Asistencia
        fields = "__all__"
        widgets = {
            "fecha": forms.DateInput(attrs={"type": "date"}),
            "hora_entrada": forms.TimeInput(attrs={"type": "time"}),
            "hora_salida": forms.TimeInput(attrs={"type": "time"})
        }

class SemestreForm(forms.ModelForm):
    class Meta:
        model = Semestre
        fields = "__all__"
        widgets = {
            "fecha_inicio": forms.DateInput(attrs={"type": "date"}),
            "fecha_fin": forms.DateInput(attrs={"type": "date"}),
        }


class MateriaForm(forms.ModelForm):
    class Meta:
        model = Materia
        fields = "__all__"

class LoginForm(forms.Form):
    usuario = forms.CharField(
        label="Usuario",
        widget=forms.TextInput(attrs={
            "class": "form-control",
            "placeholder": "Usuario"
        })
    )
    contraseña = forms.CharField(
        label="Contraseña",
        widget=forms.PasswordInput(attrs={
            "class": "form-control",
            "placeholder": "Contraseña"
        })
    )
