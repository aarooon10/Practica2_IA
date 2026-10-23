import pickle
from flask import Flask

app = Flask(__name__)

# Cargar el modelo entrenado
with open("modelo_california.pkl", "rb") as f:
    modelo = pickle.load(f)

@app.route("/")
def home():
    return "¡El modelo de California Housing está funcionando en Render!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)