import os
import urllib.request
import pickle
from flask import Flask, request, jsonify
import numpy as np

app = Flask(__name__)

MODEL_URL = "https://raw.githubusercontent.com/aarooon10/Practica2_IA/main/modelo_california.pkl"
MODEL_PATH = "modelo_california.pkl"

def download_model():
    if not os.path.exists(MODEL_PATH):
        try:
            urllib.request.urlretrieve(MODEL_URL, MODEL_PATH)
        except Exception:
            pass

download_model()

try:
    with open(MODEL_PATH, "rb") as f:
        model = pickle.load(f)
except Exception:
    model = None

@app.route("/", methods=["GET"])
def home():
    return jsonify({
        "status": "online",
        "message": "API funcionando correctamente"
    })

@app.route("/predict", methods=["POST"])
def predict():
    if model is None:
        return jsonify({"error": "Modelo no cargado"}), 500
    
    try:
        data = request.get_json(force=True)
        features = [
            float(data.get("MedInc", 0)),
            float(data.get("HouseAge", 0)),
            float(data.get("AveRooms", 0)),
            float(data.get("AveBedrms", 0)),
            float(data.get("Population", 0)),
            float(data.get("AveOcc", 0)),
            float(data.get("Latitude", 0)),
            float(data.get("Longitude", 0))
        ]
        
        prediction = model.predict(np.array([features]))
        
        return jsonify({
            "prediction": float(prediction[0])
        })
        
    except Exception as e:
        return jsonify({"error": str(e)}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
