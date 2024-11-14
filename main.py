import pandas as pd

#Cargar archivo CSV
df = pd.read_csv('D:/clases/6to Semestre/Minería de Datos/Proyecto/Hipertension_Arterial_Mexico.csv')


# Limpieza
# Eliminar duplicados
df = df.drop_duplicates()
#Eliminar filas con un valor vacio
df = df.dropna()
# Manejar valores faltantes
df = df.fillna(df.mean())  # Imputar valores faltantes con la media
df['tension_arterial'].fillna(df['tension_arterial'].mean(), inplace=True)

#Seleccion de datos
# Selección de columnas relevantes
selected_columns = ['edad', 'valor_colesterol_total', 'valor_trigliceridos', 'tension_arterial']
df_selected = df[selected_columns]

#Transformación de datos
#Nueva variable: Índice de Masa Corporal (IMC)
df['IMC'] = df['peso'] / ((df['estatura'] / 100) ** 2)


def clasificar_hipertension(valor):
    if valor < 120:
        return 'Normal'
    elif valor < 130:
        return 'Elevado'
    elif valor < 140:
        return 'Hipertensión grado 1'
    else:
        return 'Hipertensión grado 2'

df['clasificación_hipertensión'] = df['tension_arterial'].apply(clasificar_hipertension)



# Exportar datos procesados
df.to_csv('Hipertension_Arterial_Procesado.csv', index=False, encoding='utf-8')
df.to_json('Hipertension_Arterial_Procesado.json', orient='records', lines=True, force_ascii=False)
print("Datos procesados guardados en 'Hipertension_Arterial_Procesado.csv' y 'Hipertension_Arterial_Procesado.json'")
