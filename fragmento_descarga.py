import os
 
import joblib
import requests
 
MODEL_PATH = "modelo_california.pkl"
MODEL_URL = "https://raw.githubusercontent.com/aarooon10/Practica2_IA/main/modelo_california.pkl"
DOWNLOAD_TIMEOUT = 30  # segundos
 
 
def download_model(url: str = MODEL_URL, path: str = MODEL_PATH):
    """Descarga el modelo desde `url` y lo guarda en `path`."""
    response = requests.get(url, timeout=DOWNLOAD_TIMEOUT)
    response.raise_for_status()
    with open(path, "wb") as f:
        f.write(response.content)
    print(f"Modelo descargado desde GitHub y guardado en {path}")
 
 
def load_model(path: str = MODEL_PATH):
    """Carga el modelo. Si no existe en local, lo descarga antes de GitHub."""
    if not os.path.exists(path):
        print(f"{path} no encontrado en local, descargando...")
        download_model()
    return joblib.load(path)
