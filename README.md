Sistema de Gestion de Comisiones (Arquitectura MVC)

Una aplicacion web monolitica desarrollada en Python utilizando el framework Py4web. Este proyecto fue diseñado aplicando estrictamente el patron arquitectonico Modelo-Vista-Controlador (MVC) para gestionar el registro de ventas y el calculo dinamico de comisiones basado en reglas de negocio.

Demo en vivo: https://comisiones-mvc.onrender.com/comisiones


Caracteristicas Principales

Calculo Automatico: Asignacion de comisiones basadas en porcentajes y montos minimos predefinidos.

Filtros Dinamicos: Busqueda y filtrado de registros de ventas por rangos de fechas (Desde - Hasta).

Base de Datos Embebida: Uso de SQLite gestionado a traves del ORM nativo de Py4web.

Database Seeding: Insercion automatica de datos semilla (vendedores y reglas de comision) al inicializar la aplicacion.

UI/UX Limpia: Interfaz grafica responsiva estilizada con Bulma CSS.

Stack Tecnologico

Backend: Python 3 / Py4web

Frontend: HTML5 / Bulma CSS

Base de Datos: SQLite

Despliegue (PaaS): Render / Gunicorn

Estructura MVC del Proyecto

La logica principal del sistema se encuentra dentro del directorio apps/comisiones/:

Modelo (models.py): Define el esquema de la base de datos relacional (Tablas: vendedor, regla_comision, venta). Incluye la logica de sembrado de datos (Seeding).

Controlador (controllers.py): Maneja las peticiones HTTP (GET/POST), ejecuta los cruces de tablas (LEFT JOIN), intercepta los parametros de URL para filtrar por fechas y contiene el algoritmo matematico que determina la comision aplicable.

Vista (templates/dashboard.html): Plantilla HTML extendida que recibe el diccionario de datos del controlador y lo renderiza de forma dinamica en una tabla y un formulario interactivo.

Instalacion y Ejecucion Local

Sigue estos pasos para clonar y correr el proyecto en tu maquina local:

Clonar el repositorio:

git clone https://github.com/Draxmox/Tarea4_EjercicioMVC.git
cd Tarea4_EjercicioMVC


Crear y activar un entorno virtual (Windows):

python -m venv env
.\env\Scripts\activate


Instalar dependencias:

pip install -r requirements.txt


Levantar el servidor:

py4web run apps


La aplicacion estara disponible en: http://localhost:8000/comisiones

Despliegue

Este proyecto esta configurado para ser desplegado facilmente en Render. El archivo requirements.txt incluye gunicorn y el comando de arranque configurado es:
py4web run apps --host 0.0.0.0 --port $PORT

Desarrollado como proyecto practico de Arquitectura de Software.
