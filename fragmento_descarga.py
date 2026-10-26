import os
import urllib.request

MODELO_PATH = "modelo_california.pkl"
URL_MODELO_GITHUB = "https://raw.githubusercontent.com/aarooon10/Practica2_IA/main/modelo_california.pkl"

if not os.path.exists(MODELO_PATH):
    print("Modelo no encontrado en local. Descargando desde GitHub...")
    try:
        urllib.request.urlretrieve(URL_MODELO_GITHUB, MODELO_PATH)
        print("¡Modelo descargado con éxito desde la nube!")
    except Exception as e:
        print(f"Error al descargar el modelo: {e}")