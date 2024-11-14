import pandas as pd

# Cargar archivo CSV
df = pd.read_csv('Hipertension_Arterial_Mexico.csv')

# Limpieza de datos
df = df.drop_duplicates()
df = df.dropna()
df = df[df['estatura'] > 0]
df['IMC'] = df['peso'] / ((df['estatura'] / 100) ** 2)

# Clasificación de edad
def clasificar_edad(edad):
    if edad < 13:
        return 'Niño'
    elif 13 <= edad < 18:
        return 'Adolescente'
    elif 18 <= edad < 65:
        return 'Adulto'
    else:
        return 'Adulto Mayor'

df['clasificación_edad'] = df['edad'].apply(clasificar_edad)

# Clasificación de ácido úrico
def clasificar_acido_urico(valor):
    if 3.5 <= valor <= 7:
        return 'Normal'
    else:
        return 'Fuera de rango'

df['clasificación_acido_urico'] = df['valor_acido_urico'].apply(clasificar_acido_urico)

# Clasificación de colesterol total
def clasificar_colesterol_total(valor):
    if valor < 200:
        return 'Riesgo bajo'
    else:
        return 'Riesgo alto'

df['clasificación_colesterol_total'] = df['valor_colesterol_total'].apply(clasificar_colesterol_total)

# Clasificación de creatinina según sexo y edad
def clasificar_creatina(valor, sexo, edad):
    if sexo == 2:  # Mujer
        if 0.6 <= valor <= 1.1:
            return 'Normal'
    elif sexo == 1:  # Hombre
        if 0.7 <= valor <= 1.3:
            return 'Normal'
    elif 13 <= edad <= 17:  # Adolescentes
        if 0.5 <= valor <= 1.0:
            return 'Normal'
    elif edad < 13:  # Niños
        if 0.3 <= valor <= 0.7:
            return 'Normal'
    return 'Fuera de rango'

df['clasificación_creatina'] = df.apply(lambda x: clasificar_creatina(x['valor_creatina'], x['sexo'], x['edad']), axis=1)

# Clasificación de glucosa
def clasificar_glucosa(valor):
    if 80 <= valor <= 130:
        return 'Óptimo'
    elif valor <= 180:
        return 'Normal elevado'
    else:
        return 'Alto'

df['clasificación_glucosa'] = df['resultado_glucosa'].apply(clasificar_glucosa)

# Clasificación de triglicéridos
def clasificar_trigliceridos(valor):
    if valor < 150:
        return 'Normal'
    elif valor <= 200:
        return 'Límite alto'
    else:
        return 'Alto'

df['clasificación_trigliceridos'] = df['valor_trigliceridos'].apply(clasificar_trigliceridos)

# Clasificación de horas de sueño
df['clasificación_sueno'] = df['sueno_horas'].apply(lambda x: 'Suficiente' if x >= 8 else 'Insuficiente')

# Clasificación de insulina
def clasificar_insulina(valor):
    if 5 <= valor <= 25:
        return 'Normal'
    else:
        return 'Fuera de rango'

df['clasificación_insulina'] = df['valor_insulina'].apply(clasificar_insulina)

# Crear DataFrame solo con las clasificaciones
df_clasificaciones = df[['clasificación_edad', 'clasificación_acido_urico', 'clasificación_colesterol_total', 'clasificación_creatina', 'clasificación_glucosa', 'clasificación_trigliceridos', 'clasificación_sueno', 'clasificación_insulina']]

# Verificar el resultado
print("Datos completos con clasificaciones:")
print(df.head())
print("\nSolo clasificaciones:")
print(df_clasificaciones.head())

# Exportar datos completos (con valores originales y clasificaciones)
df.to_csv('Hipertension_Arterial_Procesado.csv', index=False, encoding='utf-8')
df.to_json('Hipertension_Arterial_Procesado.json', orient='records', lines=True, force_ascii=False)

# Exportar solo las clasificaciones
df_clasificaciones.to_csv('Clasificaciones_Hipertension_Arterial.csv', index=False, encoding='utf-8')
df_clasificaciones.to_json('Clasificaciones_Hipertension_Arterial.json', orient='records', lines=True, force_ascii=False)
