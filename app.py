import os
import pickle
import urllib.request
import numpy as np
from flask import Flask, request, jsonify

app = Flask(__name__)

MODELO_PATH = "modelo_california.pkl"
URL_MODELO_GITHUB = "https://raw.githubusercontent.com/aarooon10/Practica2_IA/main/modelo_california.pkl"

def download_model():
    if not os.path.exists(MODELO_PATH):
        print("Modelo no encontrado localmente. Descargando desde GitHub...")
        try:
            urllib.request.urlretrieve(URL_MODELO_GITHUB, MODELO_PATH)
            print("¡Modelo descargado con éxito!")
        except Exception as e:
            print(f"Error al descargar el modelo: {e}")

# Descargar modelo si es necesario antes de cargarlo
download_model()

# Cargar el modelo entrenado
with open(MODELO_PATH, "rb") as f:
    modelo = pickle.load(f)

@app.route("/", methods=["GET"])
def home():
    return "¡El modelo de California Housing está funcionando en Render!"

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json(force=True)
        features = [
            data.get("MedInc", 3.0),
            data.get("HouseAge", 20.0),
            data.get("AveRooms", 5.0),
            data.get("AveBedrms", 1.0),
            data.get("Population", 500.0),
            data.get("AveOccup", 3.0),
            data.get("Latitude", 34.0),
            data.get("Longitude", -118.0)
        ]
        datos_entrada = np.array([features])
        prediccion = modelo.predict(datos_entrada)
        
        return jsonify({
            "prediccion": float(prediccion[0])
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)