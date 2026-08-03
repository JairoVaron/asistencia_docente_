# Sistema de Gestión de Asistencia Docente

Aplicación web desarrollada con **Python y Django** para gestionar el control de asistencia de docentes dentro de una institución educativa. El sistema permite administrar docentes, programas académicos, semestres y registros de asistencia, además de consultar porcentajes de asistencia y generar reportes.

> **Actualización reciente:** se realizó un **rediseño completo de la interfaz (frontend)** para ofrecer una experiencia visual más moderna, limpia y fácil de usar.

## Características principales

* Autenticación de usuarios.
* Gestión de docentes.
* Registro de asistencia.
* Consulta de porcentajes de asistencia.
* Administración de programas académicos.
* Administración de semestres.
* Interfaz responsive con un diseño renovado.

## Tecnologías utilizadas

* **Python 3**
* **Django**
* **SQLite3**
* **HTML5**
* **CSS3**
* **Bootstrap 5**
* **JavaScript**

## Instalación

### 1. Clonar el repositorio

```bash
git clone https://github.com/JairoVaron/asistencia_docente_.git
cd asistencia_docente_
```

### 2. Crear un entorno virtual (opcional, recomendado)

**Windows**

```bash
python -m venv venv
venv\Scripts\activate
```

**Linux / macOS**

```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

Si no existe el archivo `requirements.txt`, puedes generarlo con:

```bash
pip freeze > requirements.txt
```

### 4. Aplicar migraciones

```bash
python manage.py migrate
```

### 5. Ejecutar el servidor

```bash
python manage.py runserver
```

Abrir en el navegador:

```
http://127.0.0.1:8000/
```

## Estructura del proyecto

```text
AsistenciaDocente/
│── manage.py
│── db.sqlite3
│
├── app/
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   ├── urls.py
│   ├── templates/
│   └── static/
│
└── asistencia_docente/
    ├── settings.py
    ├── urls.py
    └── wsgi.py
```

## Funcionalidades

### Gestión de docentes

* Registrar nuevos docentes.
* Editar información.
* Consultar el listado de docentes.

### Control de asistencia

* Registrar hora de entrada y salida.
* Asociar asignatura, tema y jornada.
* Consultar registros por fecha y docente.

### Administración académica

* Programas académicos.
* Semestres.
* Organización de la información institucional.

## Comandos útiles

Crear un superusuario:

```bash
python manage.py createsuperuser
```

Crear nuevas migraciones:

```bash
python manage.py makemigrations
```

Aplicar migraciones:

```bash
python manage.py migrate
```

## Capturas del sistema

Se recomienda agregar capturas de pantalla del **nuevo diseño** en una carpeta `docs/images/` y mostrarlas aquí para visualizar la interfaz del sistema.

## Problema que resuelve

El sistema reemplaza el registro manual en papel por una plataforma digital que permite:

* Centralizar la información.
* Consultar registros rápidamente.
* Generar reportes.
* Mejorar la seguridad de los datos.
* Optimizar la gestión académica y administrativa.

## Autor

**Jairo Varón**
**Jhon Escorcia**

GitHub: https://github.com/JairoVaron

## Licencia

Este proyecto puede utilizarse con fines **educativos y académicos**.
