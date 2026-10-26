# Práctica 2: Despliegue de Modelo de Machine Learning en Render

Repositorio para el desarrollo y despliegue de una API en Flask basada en el modelo de Machine Learning de California Housing.

## Autores
- David Tella Miranda
- Aaron Hernández Ocejo

## Pasos Seguidos para el Despliegue
1. **Creación del repositorio**: Se estructuró el proyecto en GitHub incluyendo el script principal (`app.py`), el modelo entrenado (`modelo_california.pkl`) y el archivo de dependencias (`requirements.txt`).
2. **Despliegue en Render**: Se creó un nuevo Web Service en Render vinculado a este repositorio público.
3. **Comando de Arranque (Start Command)**: Configurado en Render para producción mediante Gunicorn:
   ```bash
   gunicorn app:app```

Enlace del Servicio Desplegado
https://practica2-ia.onrender.com
