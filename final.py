import functions as func
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
plt.style.use('ggplot')

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

# Acido Urico
dfEdad = dfnew.pivot_table(index='edad',columns='acido_urico',aggfunc='size',fill_value=0)

dfEdad = round(dfEdad.div(dfEdad.sum(axis=1),axis=0)*100,2)
print(dfEdad)
columns = dfEdad.columns.tolist()[0:]
colors = ['#ff335e', '#335eff']
barWidth = 0.25

br1 = np.arange(dfEdad.shape[0]) - barWidth
br2 = br1 + barWidth
brs = [br1, br2]
print(br1)

plt.figure(figsize=(10,6))
for br, color, col_name in zip(brs, colors, columns):
    print(br,col_name)
    plt.bar(br, dfEdad[col_name], width=barWidth, color=color, label=col_name)


plt.xticks(br2, dfnew.groupby('edad').groups.keys())

ax = plt.gca()
for br, color, col_name in zip(brs, colors, columns):
    for j, v in enumerate(dfEdad[col_name].values):
        ax.text(br[j]-barWidth*0.5, v+1, f'{v:,.2f}', color=color, fontweight='bold',fontsize=8)

plt.title('Acido Urico por Edad')
plt.legend(loc='best')
plt.show()
# dfnew.to_csv('test.csv',index=False,encoding='utf-8')
