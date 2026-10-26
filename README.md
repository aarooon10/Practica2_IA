# Práctica 2: Despliegue de Modelo de Machine Learning en Render

Este repositorio contiene la implementación y el despliegue de una aplicación web en Flask basada en un modelo de Machine Learning (California Housing).

## Pasos Seguidos para el Despliegue

1. **Creación de cuenta y servicio**: 
   - Se creó una cuenta gratuita en la plataforma de despliegue [Render](https://render.com).
   - Se configuró un nuevo servicio web (*Web Service*) conectado a este repositorio público de GitHub.

2. **Configuración del Repositorio**:
   - Se estructuró el proyecto incluyendo el archivo principal `app.py` con el *health-check* (`GET /`) y el endpoint de predicción (`POST /predict`).
   - Se añadió el archivo del modelo entrenado (`modelo_california.pkl`) y el script de prueba local (`test.py`).

3. **Comandos y Despliegue**:
   - El entorno se configuró utilizando `uv` y las dependencias necesarias de Python.
   - El despliegue automatizado se gestionó directamente desde GitHub, forzando la compilación y ejecución de la aplicación Flask en el puerto `10000`.

## Enlace del Servicio Desplegado
* **URL Pública**: https://practica2-ia.onrender.com/[cite: 5]