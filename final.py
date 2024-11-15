import functions as func
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('Hipertension_Arterial_Mexico.csv')

#Tratado de datos
df = df.drop_duplicates()
df = df.dropna()
df = df[df['estatura'] > 0]
dfnew = pd.DataFrame()
dfnew['IMC'] = df['peso'] / ((df['estatura'] / 100) ** 2)
dfnew['edad'] = df['edad'].apply(func.clasificar_edad)
dfnew['acido_urico'] = df['valor_acido_urico'].apply(func.clasificar_acido_urico)
dfnew['colesterol'] = df['valor_colesterol_total'].apply(func.clasificar_colesterol_total)
dfnew['creatina'] = df.apply(lambda x: func.clasificar_creatina(x['valor_creatina'], x['sexo'], x['edad']), axis=1)
dfnew['glucosa'] = df['resultado_glucosa'].apply(func.clasificar_glucosa)
dfnew['trigliceridos'] = df['valor_trigliceridos'].apply(func.clasificar_trigliceridos)
dfnew['insulina'] = df['valor_insulina'].apply(func.clasificar_insulina)

print(dfnew)

# dfnew.to_csv('test.csv',index=False,encoding='utf-8')
