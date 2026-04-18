# 💼 Alke Wallet - Billetera Digital

Alke Wallet es una aplicación web financiera desarrollada en Python y Django. Este proyecto fue creado para simular el entorno de una empresa Fintech (Alke Financial), permitiendo a los usuarios gestionar sus cuentas digitales, registrar transacciones (ingresos y egresos), consultar saldos dinámicos y administrar sus activos de forma segura y centralizada.

---

## 🎯 El Problema que Resuelve
En la actualidad, la dispersión de la información financiera dificulta que las personas tengan un control claro de sus finanzas personales. Alke Wallet resuelve este problema proporcionando una plataforma unificada y segura donde los usuarios pueden:
- Visualizar el estado de múltiples cuentas bancarias o billeteras en un solo dashboard.
- Registrar el flujo de dinero (ingresos y gastos) de manera categorizada.
- Mantener la integridad de sus datos financieros mediante un sistema robusto y autenticado.

---

## 🚀 El Desafío Técnico
El desarrollo de esta plataforma implicó superar varios retos técnicos propios de una aplicación financiera:
1. **Arquitectura de Datos Relacional:** Diseñar e implementar un modelo de base de datos robusto que relacione de manera eficiente a los `Clientes` con sus múltiples `Cuentas` y el historial de `Transacciones` (relaciones 1:1, 1:N y N:N), garantizando que no haya pérdida de integridad referencial.
2. **Cálculos Dinámicos y Eficiencia:** Reemplazar cálculos manuales en memoria por consultas avanzadas directamente en la base de datos utilizando el ORM de Django (filtros, anotaciones y, en casos específicos, consultas SQL personalizadas con cursores) para calcular los saldos en tiempo real de forma optimizada.
3. **Seguridad y Accesos:** Proteger las rutas y operaciones CRUD (Crear, Leer, Actualizar, Eliminar) asegurando que solo usuarios autenticados puedan modificar sus propios activos, implementando protección CSRF en todos los formularios.

---

## 🛠️ Tecnologías Utilizadas
* **Backend:** Python 3.x, Django 4.x
* **Base de Datos:** SQLite (Entorno de desarrollo) / Preparado para PostgreSQL (Producción)
* **Frontend:** HTML5, CSS3, Django Templates
* **Control de Versiones:** Git & GitHub
* **Seguridad:** Autenticación nativa de Django, Tokens CSRF.

---

## 🧠 Mis Principales Aprendizajes
Durante la construcción de Alke Wallet, logré consolidar conocimientos clave para el desarrollo backend:
* **Dominio del ORM de Django:** Aprendí a traducir lógica de negocios compleja en consultas de base de datos eficientes, utilizando herramientas como `filter()`, `exclude()`, `annotate()`, e incluso la ejecución de SQL raw (`raw()`).
* **Gestión de Migraciones:** Comprendí la importancia del versionado de la base de datos (`makemigrations` y `migrate`) para mantener el esquema sincronizado de manera segura en un entorno de desarrollo continuo.
* **Patrón MVT (Model-View-Template):** Perfeccioné la separación de responsabilidades, creando vistas basadas en clases y funciones para manejar la lógica, y utilizando el sistema de plantillas de Django para renderizar la información de manera dinámica.
* **Uso de Aplicaciones Integradas:** Aproveché al máximo las herramientas "out-of-the-box" de Django, como `django.contrib.admin` para crear un panel de administración potente en minutos y `django.contrib.auth` para gestionar la seguridad de las sesiones de usuario.

---

## ⚙️ Funcionalidades Principales
- [x] **Autenticación Segura:** Sistema de Login/Logout utilizando la autenticación nativa de Django.
- [x] **Gestión de Cuentas (CRUD):** Creación, lectura, edición y eliminación de cuentas financieras.
- [x] **Registro de Transacciones:** Historial detallado de depósitos y retiros vinculados a cuentas específicas.
- [x] **Panel de Administración:** Interfaz gráfica privada (`/admin/`) para la gestión integral de Clientes, Cuentas y Transacciones.
- [x] **Saldos Dinámicos:** Cálculo automatizado del balance de las cuentas en función del historial de transacciones.

---

## 💻 Instalación y Ejecución Local

Si deseas probar el proyecto en tu entorno local, sigue estos pasos:

1. **Clonar el repositorio:**
   ```bash
   git clone https://github.com/Bercc7/AlkeWallet_Billetera-Digital.git
   cd AnkeWallet_Modulo7

Crear y activar entorno virtual:
Bash

python -m venv venv
# En Windows:
venv\Scripts\activate
# En macOS/Linux:
source venv/bin/activate

# Instalar dependencias:
Bash

pip install django

# Aplicar migraciones y crear base de datos:
Bash

python manage.py migrate

# (Opcional) Crear un superusuario para acceder al panel admin:
Bash

python manage.py createsuperuser

# Ejecutar el servidor de desarrollo:
Bash

python manage.py runserver

# Acceder a la aplicación:

    Frontend / Login: http://127.0.0.1:8000/login/

    Panel de Administración: http://127.0.0.1:8000/admin/
