import pandas as pd

# 1. CARGA Y LIMPIEZA DE DATOS
# 1.1 Cargamos el dataset
df = pd.read_csv("dataset.txt")
df.isnull().sum()  # Verificamos nulos en el dataset "Total Price"

# 1.2 Eliminacion de nulos
df = df.dropna()  # Eliminamos filas con nulos
df.isnull().sum()
