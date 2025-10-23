from django.db import models

# Modelo para el docente
class Docente(models.Model):
    nombre = models.CharField(max_length=100, blank=False, null=False)
    apellido = models.CharField(max_length=100, blank=False, null=False)
    identificacion = models.CharField(max_length=20, unique=True)
    correo = models.EmailField(unique=True)
    materia = models.CharField(
        max_length=100,
        choices=[
            ('Matemáticas', 'Matemáticas'),
            ('Lengua', 'Lengua'),
            ('Ciencias', 'Ciencias'),
            ('Historia', 'Historia'),
            ('Inglés', 'Inglés'),
        ]
    )

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


# Modelo para registrar la asistencia
class Asistencia(models.Model):
    docente = models.ForeignKey(Docente, on_delete=models.CASCADE)
    fecha = models.DateField(auto_now_add=True)
    hora_entrada = models.TimeField()
    hora_salida = models.TimeField(null=True, blank=True)
    observaciones = models.TextField(blank=True)

    def __str__(self):
        return f"Asistencia de {self.docente} el {self.fecha}"

