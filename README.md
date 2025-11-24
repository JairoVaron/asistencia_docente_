# Sistema de Gestión de Asistencias – Django
Este proyecto es una aplicación web desarrollada en Python, utilizando el framework Django, cuya finalidad es gestionar docentes, asistencias, programas y semestres académicos dentro de una institución educativa.
Incluye módulos para:
•	Registro y autenticación de usuarios.
•	Gestión de docentes.
•	Registro de asistencias.
•	Consulta de porcentajes de asistencia.
•	Administración de programas académicos.
•	Administración de semestres.

# Requisitos Previos
Antes de ejecutar el proyecto, asegúrate de tener instalado:
•	Python 3.10+
•	pip (gestor de paquetes de Python)
•	Virtualenv (opcional pero recomendado)

# Instalación y Ejecución del Proyecto
Sigue estos pasos para ejecutar correctamente la aplicación:

1. Clonar el repositorio
git clone https://github.com/usuario/tu-repositorio.git
cd tu-repositorio

2. Crear y activar entorno virtual (opcional, recomendado)
En Windows:
python -m venv venv
venv\Scripts\activate
En Linux / MacOS:
python3 -m venv venv
source venv/bin/activate

3. Instalar dependencias del proyecto
pip install -r requirements.txt
Si no tienes un archivo requirements.txt, puedes generarlo con:
pip freeze > requirements.txt

4. Realizar migraciones
Django utiliza migraciones para crear las tablas en la base de datos SQLite.
python manage.py migrate

5. Ejecutar el servidor
Este comando inicia la aplicación en el navegador:
python manage.py runserver
Luego abre:
http://127.0.0.1:8000/

# Estructura del Proyecto
AsistenciaDocente/
│
│── db.sqlite3
│── manage.py
│── estructura.txt
│
├── app/
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── models.py
│   ├── tests.py
│   ├── urls.py
│   ├── views.py
│   ├── __init__.py
│   │
│   ├── migrations/
│   │   ├── 0001_initial.py
│   │   ├── 0002_alter_asistencia_fecha.py
│   │   ├── 0003_programa_semestre.py
│   │   ├── 0004_asignatura.py
│   │   ├── 0005_alter_asistencia_tema.py
│   │   ├── __init__.py
│   │
│   ├── static/
│   │   ├── css/
│   │   │   └── styles.css
│   │   ├── img/
│   │   │   ├── logo.png
│   │   │   └── usuario.png
│   │   └── js/
│   │       └── scripts.js
│   │
│   └── templates/
│       ├── base.html
│       ├── login.html
│       ├── docentes.html
│       ├── registrar_docente.html
│       ├── asistencia.html
│       ├── porcentaje_asistencia.html
│       ├── programas.html
│       ├── semestre.html
│       └── error.html
│
└── asistencia_docente/
    ├── __init__.py
    ├── asgi.py
    ├── settings.py
    ├── urls.py
    └── wsgi.py

# Tecnologías Usadas
•	Python
•	Django
•	SQLite3
•	HTML5 / CSS3 / Bootstrap 5

# Comandos Útiles
Crear superusuario:
python manage.py createsuperuser
Limpiar migraciones (si es necesario):
find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
python manage.py makemigrations
python manage.py migrate

# Imágenes y Evidencias
Todas las capturas de pantalla del sistema se encuentran documentadas en el informe y pueden ser añadidas aquí si el repositorio lo requiere.

# Licencia
Este proyecto puede ser usado con fines educativos y académicos.


