# Sistema de Gestión de Proyectos y Tareas

Una aplicación web desarrollada con Django para gestionar proyectos personales y tareas asociadas. Este proyecto implementa autenticación segura, operaciones CRUD y un panel de administración personalizado.

## 🚀 Características Principales
* **Autenticación de Usuarios:** Sistema de Login, Logout y protección de rutas mediante `@login_required`.
* **Gestión de Proyectos:** Los usuarios pueden crear y visualizar sus propios proyectos.
* **Gestión de Tareas:** Cada proyecto contiene tareas independientes que pueden marcarse como "Pendientes" o "Completadas".
* **Seguridad:** Aislamiento de datos (un usuario no puede ver ni modificar los proyectos de otro).
* **Panel de Administración:** Interfaz administrativa de Django personalizada con barras de búsqueda y filtros.

## 🛠️ Tecnologías Utilizadas
* Python
* Django (Framework MVT)
* SQLite (Base de datos por defecto)
* HTML/CSS (Diseño frontend)

## ⚙️ Instalación y Ejecución

Sigue estos pasos para ejecutar el proyecto en tu máquina local:

1. **Crear y activar el entorno virtual:**
   ```bash
   python -m venv venv
   # En Windows:
   venv\Scripts\activate
   # En Mac/Linux:
   source venv/bin/activate

Acceder a la aplicación:

    Frontend: http://127.0.0.1:8000/login/

    Panel Admin: http://127.0.0.1:8000/admin/