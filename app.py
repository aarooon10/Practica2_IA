import pickle
import numpy as np
from flask import Flask, request, jsonify

app = Flask(__name__)

# Cargar el modelo entrenado
with open("modelo_california.pkl", "rb") as f:
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