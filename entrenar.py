import pickle
from sklearn.datasets import fetch_california_housing
from sklearn.linear_model import LinearRegression

print("Descargando datos...")
housing = fetch_california_housing(as_frame=True)
X, y = housing.data, housing.target

print("Entrenando el modelo...")
modelo = LinearRegression()
modelo.fit(X, y)

print("Guardando el modelo...")
with open("modelo_california.pkl", "wb") as archivo:
    pickle.dump(modelo, archivo)

print("¡Modelo guardado con éxito como modelo_california.pkl!")