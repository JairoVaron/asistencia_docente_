from django.db import models
from django.contrib.auth.models import User

class Programa(models.Model):
    nombre = models.CharField(max_length=200, unique=True)
    codigo = models.CharField(max_length=50, blank=True, null=True)

    class Meta:
        verbose_name = "Programa"
        verbose_name_plural = "Programas"

    def __str__(self):
        return f"{self.nombre} ({self.codigo})" if self.codigo else self.nombre


class Semestre(models.Model):
    nombre = models.CharField(max_length=100, unique=True)
    fecha_inicio = models.DateField(blank=True, null=True)
    fecha_fin = models.DateField(blank=True, null=True)

    class Meta:
        verbose_name = "Semestre"
        verbose_name_plural = "Semestres"

    def __str__(self):
        return self.nombre


class Docente(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    nombre = models.CharField(max_length=100)
    apellido = models.CharField(max_length=100)
    documento = models.CharField(max_length=50, unique=True)
    email = models.EmailField(null=True, blank=True)
    programa = models.ForeignKey(
        Programa, 
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='docentes'
    )

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Materia(models.Model):
    nombre = models.CharField(max_length=200)
    codigo = models.CharField(max_length=20, blank=True, null=True)
    programa = models.ForeignKey(
        Programa,
        on_delete=models.CASCADE,
        related_name='materias'
    )

    def __str__(self):
        return self.nombre
    


JORNADAS = [
    ('mañana', 'Mañana'),
    ('tarde', 'Tarde'),
    ('noche', 'Noche'),
]


class Asistencia(models.Model):
    docente = models.ForeignKey(
        Docente,
        on_delete=models.CASCADE,
        related_name='asistencias'
    )
    fecha = models.DateField()
    presente = models.BooleanField(default=True)
    comentario = models.TextField(blank=True, null=True)
    semestre = models.ForeignKey(
        Semestre,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='asistencias'
    )

    hora_entrada = models.TimeField(null=True, blank=True)
    hora_salida = models.TimeField(null=True, blank=True)

    materia = models.CharField(max_length=200, blank=True, null=True)
    tema = models.CharField(max_length=255, blank=True, null=True)

    jornada = models.CharField(
        max_length=10,
        choices=JORNADAS,
        blank=True,
        null=True
    )

    def __str__(self):
        return f"Asistencia: {self.docente} - {self.fecha} - {'Presente' if self.presente else 'Ausente'}"



#python manage.py makemigrations
#python manage.py migrate
###
#python manage.py runserver ==> con esto funciona el programa
###
# Username: Jairo
# Email address: jhonescorciacaraballo@gmail.com
# Password: Jhon272003 