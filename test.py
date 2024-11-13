import pandas as pd

# Crear un DataFrame de ejemplo
data = {
    'categoria': ['A', 'B', 'A', 'C', 'B', 'A'],
    'valor': [10, 15, 10, 10, 15, 20],
    'cantidad': [1, 2, 1, 2, 1, 1]
}
df = pd.DataFrame(data)

print(df)
# Agrupar por la columna 'categoria' y calcular la suma de 'valor' y 'cantidad' por cada categoría
df_agrupado = df.groupby('categoria').sum()

print(df_agrupado)

