import pandas as pd

'''Edad'''
def clasificar_edad(edad):
    if edad < 13:
        return 'Nino'
    elif 13 <= edad < 18:
        return 'Adolescente'
    elif 18 <= edad < 65:
        return 'Adulto'
    else:
        return 'Adulto Mayor'

'''acido urico'''
def clasificar_acido_urico(valor):
    if 3.5 <= valor <= 7:
        return 'Normal'
    else:
        return 'Fuera de rango'
    
'''colesterol'''
def clasificar_colesterol_total(valor):
    if valor < 200:
        return 'Riesgo bajo'
    else:
        return 'Riesgo alto'

'''Creatina'''
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

'''Glucosa'''
def clasificar_glucosa(valor):
    if 80 <= valor <= 130:
        return 'Óptimo'
    elif valor <= 180:
        return 'Normal elevado'
    else:
        return 'Alto'

'''Trigliceridos'''
def clasificar_trigliceridos(valor):
    if valor < 150:
        return 'Normal'
    elif valor <= 200:
        return 'Límite alto'
    else:
        return 'Alto'
    
'''Insulina'''
def clasificar_insulina(valor):
    if 5 <= valor <= 25:
        return 'Normal'
    else:
        return 'Fuera de rango'
