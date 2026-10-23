import pickle
import numpy as np
from flask import Flask, request, jsonify

app = Flask(__name__)

# Cargar el modelo entrenado
with open("modelo_california.pkl", "rb") as f:
    modelo = pickle.load(f)

@app.route("/", methods=["GET"])
def home():
    return "¡El servicio web de California Housing está activo y funcionando!"

@app.route("/predict", methods=["POST"])
def predict():
    try:
        # Obtener los datos enviados en formato JSON
        data = request.get_json(force=True)
        
        # Extraer las características (features) requeridas por el modelo
        # El dataset de California Housing tiene 8 características:
        # MedInc, HouseAge, AveRooms, AveBedrms, Population, AveOccup, Latitude, Longitude
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
        
        # Convertir a matriz 2D para la predicción
        datos_entrada = np.array([features])
        prediccion = modelo.predict(datos_entrada)
        
        # Devolver el resultado en formato JSON
        return jsonify({
            "prediccion_precio_mediano_vivienda": float(prediccion[0])
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)