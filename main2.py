import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('D:/clases/6to Semestre/Minería de Datos/Proyecto/Hipertension_Arterial_Mexico.csv')

df = df.drop(columns=['concentracion_hemoglobina',
'temperatura_ambiente',
'valor_albumina',
'valor_colesterol_hdl',
'valor_colesterol_ldl',
'resultado_glucosa_promedio',
'valor_hemoglobina_glucosilada',
'valor_ferritina',
'valor_folato',
'valor_homocisteina',
'valor_proteinac_reactiva',
'valor_transferrina',
'valor_vitamina_bdoce',
'valor_vitamina_d',
'medida_cintura',
'segundamedicion_peso',
'segundamedicion_estatura',
'distancia_rodilla_talon',
'circunferencia_de_la_pantorrilla',
'segundamedicion_cintura',
'riesgo_hipertension'], axis=1)