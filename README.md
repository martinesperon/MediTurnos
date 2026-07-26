# MediTurnos

Sistema web de gestión de turnos médicos desarrollado con Django. Permite a los pacientes explorar especialidades y médicos, reservar turnos online y gestionarlos, y a los administradores gestionar todo el catálogo médico desde el panel de Django.

Proyecto integrador de la materia **Backend** — Instituto de Formación Técnica Superior N°18.

## Funcionalidades

- **Registro y autenticación de usuarios**, con perfil de paciente extendido (teléfono, obra social, fecha de nacimiento).
- **Catálogo de especialidades médicas**, con búsqueda por nombre.
- **Catálogo de médicos**, cada uno asociado a una o más especialidades, con filtro por especialidad y horario de atención.
- **Reserva de turnos**: los pacientes reservan turnos con el médico elegido, respetando su horario de atención y evitando fechas pasadas.
- **Gestión de turnos propios**: cada paciente ve, edita y cancela únicamente sus propios turnos, filtrando por estado y rango de fechas.
- **Panel de administración de Django** para gestionar todos los modelos, con búsqueda, filtros y ordenamiento.
- Validación de datos tanto en el **front-end** (HTML5 + JavaScript) como en el **back-end** (Django Forms y validaciones de modelo).

## Stack técnico

- **Backend:** Python 3 + Django 5
- **Base de datos:** SQLite (por defecto). Puede configurarse PostgreSQL cambiando `DATABASES` en `settings.py`.
- **Frontend:** Django Templates, CSS propio, JavaScript vanilla para validaciones.
- **Autenticación:** sistema de auth nativo de Django.

## Estructura del proyecto

El proyecto está dividido en apps, cada una con una responsabilidad concreta:

| App | Responsabilidad | Modelos |
|---|---|---|
| `accounts` | Registro, login, logout y perfil de usuario | — (usa `User` de Django) |
| `patients` | Datos extendidos del paciente (relación 1 a 1 con `User`) | `PatientProfile` |
| `specialties` | Catálogo de especialidades médicas (CRUD) | `Specialty` |
| `doctors` | Catálogo de médicos, con especialidades (relación N a M) (CRUD) | `Doctor` |
| `appointments` | Reserva y gestión de turnos (CRUD) | `Appointment` |

## Instalación y puesta en marcha

1. Cloná el repositorio y entrá a la carpeta del proyecto:
```bash
   git clone <url-del-repo>
   cd mediturnos
```

2. Creá y activá un entorno virtual:
```bash
   python -m venv venv
   source venv/bin/activate   # En Windows: venv\Scripts\activate
```

3. Instalá las dependencias:
```bash
   pip install -r requirements.txt
```

4. Aplicá las migraciones:
```bash
   python manage.py migrate
```

5. Creá un superusuario para acceder al panel de administración:
```bash
   python manage.py createsuperuser
```

6. Levantá el servidor de desarrollo:
```bash
   python manage.py runserver
```

7. Accedé a la aplicación en `http://127.0.0.1:8000/` y al panel de administración en `http://127.0.0.1:8000/admin/`.

## Uso básico

1. Registrate como paciente desde **Registrarme**.
2. Cargá especialidades y médicos (necesitás estar logueado, o hacerlo desde el `/admin/`).
3. Buscá un médico por especialidad y reservá un turno.
4. Gestioná tus turnos desde **Mis turnos**: podés editarlos o cancelarlos.
5. Completá tu ficha de paciente desde **Mi perfil**.

## Autor

Desarrollado por Martín Esperon como proyecto integrador de la materia Backend, IFTS N°18.