import pandas as pd

# Cargar archivo CSV
df = pd.read_csv('Hipertension_Arterial_Mexico.csv')

# Limpieza de datos
df = df.drop_duplicates()
df = df.dropna()
df = df[df['estatura'] > 0]
# Filtrar pesos irreales
df = df[(df['peso'] >= 30) & (df['peso'] <= 300)]


df['IMC'] = df['peso'] / ((df['estatura'] / 100) ** 2)

# Clasificacion de edad
def clasificar_edad(edad):
    if edad < 13:
        return 'Nino'
    elif 13 <= edad < 18:
        return 'Adolescente'
    elif 18 <= edad < 65:
        return 'Adulto'
    else:
        return 'Adulto Mayor'

df['clasificacion_edad'] = df['edad'].apply(clasificar_edad)

# Clasificacion de acido urico
def clasificar_acido_urico(valor):
    if 3.5 <= valor <= 7:
        return 'Normal'
    else:
        return 'Fuera de rango'

df['clasificacion_acido_urico'] = df['valor_acido_urico'].apply(clasificar_acido_urico)

# Clasificacion de colesterol total
def clasificar_colesterol_total(valor):
    if valor < 200:
        return 'Riesgo bajo'
    else:
        return 'Riesgo alto'

df['clasificacion_colesterol_total'] = df['valor_colesterol_total'].apply(clasificar_colesterol_total)

# Clasificacion de creatinina segun sexo y edad
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
    elif edad < 13:  # Ninos
        if 0.3 <= valor <= 0.7:
            return 'Normal'
    return 'Fuera de rango'

df['clasificacion_creatina'] = df.apply(lambda x: clasificar_creatina(x['valor_creatina'], x['sexo'], x['edad']), axis=1)

# Clasificacion de glucosa
def clasificar_glucosa(valor):
    if 80 <= valor <= 130:
        return 'Optimo'
    elif valor <= 180:
        return 'Normal elevado'
    else:
        return 'Alto'

df['clasificacion_glucosa'] = df['resultado_glucosa'].apply(clasificar_glucosa)

# Clasificacion de trigliceridos
def clasificar_trigliceridos(valor):
    if valor < 150:
        return 'Normal'
    elif valor <= 200:
        return 'Limite alto'
    else:
        return 'Alto'

df['clasificacion_trigliceridos'] = df['valor_trigliceridos'].apply(clasificar_trigliceridos)

# Clasificacion de horas de sueno
df['clasificacion_sueno'] = df['sueno_horas'].apply(lambda x: 'Suficiente' if x >= 8 else 'Insuficiente')

# Clasificacion de insulina
def clasificar_insulina(valor):
    if 5 <= valor <= 25:
        return 'Normal'
    else:
        return 'Fuera de rango'

df['clasificacion_insulina'] = df['valor_insulina'].apply(clasificar_insulina)

# Columna de posible enfermedad basada en clasificaciones
def posible_enfermedad(row):
    if row['clasificacion_glucosa'] == 'Alto' or row['clasificacion_insulina'] == 'Fuera de rango':
        return 'Diabetes'
    elif row['clasificacion_trigliceridos'] == 'Alto' or row['clasificacion_colesterol_total'] == 'Riesgo alto':
        return 'Enfermedad Cardiovascular'
    elif row['clasificacion_acido_urico'] == 'Fuera de rango':
        return 'Gota'
    elif row['IMC'] >= 30:
        return 'Obesidad'
    elif row['clasificacion_sueno'] == 'Insuficiente' and row['clasificacion_glucosa'] == 'Normal elevado':
        return 'Riesgo de Diabetes'
    else:
        return 'Saludable'

df['posible_enfermedad'] = df.apply(posible_enfermedad, axis=1)

# Exportar datos completos (con valores originales, clasificaciones y posibles enfermedades)
df.to_csv('Hipertension_Arterial_Procesado.csv', index=False, encoding='utf-8')
df.to_json('Hipertension_Arterial_Procesado.json', orient='records', lines=True, force_ascii=False)

# Crear DataFrame solo con las clasificaciones y posible enfermedad
df_clasificaciones = df[['clasificacion_edad', 'clasificacion_acido_urico', 'clasificacion_colesterol_total', 'clasificacion_creatina', 'clasificacion_glucosa', 'clasificacion_trigliceridos', 'clasificacion_sueno', 'clasificacion_insulina', 'posible_enfermedad']]

# Exportar solo las clasificaciones y posible enfermedad
df_clasificaciones.to_csv('Clasificaciones_Hipertension_Arterial.csv', index=False, encoding='utf-8')
df_clasificaciones.to_json('Clasificaciones_Hipertension_Arterial.json', orient='records', lines=True, force_ascii=False)

# Verificar el resultado
print("Datos completos con clasificaciones y posibles enfermedades:")
print(df.head())
print("\nSolo clasificaciones y posibles enfermedades:")
print(df_clasificaciones.head())
