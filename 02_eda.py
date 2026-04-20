import pandas as pd

# Cargar el dataset
df = pd.read_csv("Amazon Sale Report.csv")

# 1. Shape — cuántas filas y columnas
print("=" * 50)
print("SHAPE DEL DATASET:")
print(f"Filas: {df.shape[0]}")
print(f"Columnas: {df.shape[1]}")

# 2. Tipos de datos por columna
print("\n" + "=" * 50)
print("TIPOS DE DATOS POR COLUMNA:")
print(df.dtypes)

# 3. Porcentaje de nulos por columna
print("\n" + "=" * 50)
print("PORCENTAJE DE NULOS POR COLUMNA:")
nulos = (df.isnull().sum() / len(df) * 100).round(2)
print(nulos[nulos > 0])

# 4. Estadísticas descriptivas de columnas numéricas
print("\n" + "=" * 50)
print("ESTADÍSTICAS DESCRIPTIVAS:")
print(df[["Qty", "Amount"]].describe().round(2))
