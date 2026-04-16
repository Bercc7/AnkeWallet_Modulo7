# Alke Wallet

Alke Wallet es una billetera digital desarrollada en Python y Django, creada para gestionar activos financieros personales. Permite registrar múltiples cuentas, controlar ingresos y egresos, y categorizar transacciones.

## Funcionalidades
* Autenticación de usuarios nativa de Django.
* Operaciones CRUD para cuentas y transacciones.
* Relaciones de base de datos robustas (1:1, 1:N, N:N).
* Consultas personalizadas y cálculo de saldos dinámicos con el ORM.

## Instalación y ejecución local
1. Clonar el repositorio: `git clone https://github.com/Bercc7/AnkeWallet_Modulo7.git`
2. Crear y activar entorno virtual: `python -m venv venv`
3. Instalar dependencias: `pip install django`
4. Crear base de datos: `python manage.py migrate`
5. Ejecutar servidor: `python manage.py runserver`

## Acceder a la aplicación:

Frontend: http://127.0.0.1:8000/login/
Panel Admin: http://127.0.0.1:8000/admin/