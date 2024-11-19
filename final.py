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
dfnew['presion_arterial'] = df['tension_arterial'].apply(func.clasifica_tension_arterial)


# Elimina las filas con presión baja
def eliminar_presion_baja(df, columna):
    condiciones_baja = ['Presion Baja']  # Ajusta los criterios según sea necesario
    df_filtrado = df[~df[columna].isin(condiciones_baja)]
    return df_filtrado


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

plt.figure(figsize=(16,10))
plt.subplot(3, 2, 1)
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

#Colesterol
dfEdad = dfnew.pivot_table(index='edad',columns='colesterol',aggfunc='size',fill_value=0)

dfEdad = round(dfEdad.div(dfEdad.sum(axis=1),axis=0)*100,2)
print(dfEdad)
columns = dfEdad.columns.tolist()[0:]
colors = ['#ff335e', '#335eff']
barWidth = 0.25

br1 = np.arange(dfEdad.shape[0]) - barWidth
br2 = br1 + barWidth
brs = [br1, br2]
print(br1)

plt.subplot(3, 2, 2)
for br, color, col_name in zip(brs, colors, columns):
    print(br,col_name)
    plt.bar(br, dfEdad[col_name], width=barWidth, color=color, label=col_name)


plt.xticks(br2, dfnew.groupby('edad').groups.keys())

ax = plt.gca()
for br, color, col_name in zip(brs, colors, columns):
    for j, v in enumerate(dfEdad[col_name].values):
        ax.text(br[j]-barWidth*0.5, v+1, f'{v:,.2f}', color=color, fontweight='bold',fontsize=8)

plt.title('Colesterol por Edad')
plt.legend(loc='best')

#Creatina
dfEdad = dfnew.pivot_table(index='edad',columns='creatina',aggfunc='size',fill_value=0)

dfEdad = round(dfEdad.div(dfEdad.sum(axis=1),axis=0)*100,2)
print(dfEdad)
columns = dfEdad.columns.tolist()[0:]
colors = ['#ff335e', '#335eff']
barWidth = 0.25

br1 = np.arange(dfEdad.shape[0]) - barWidth
br2 = br1 + barWidth
brs = [br1, br2]
print(br1)

plt.subplot(3, 2, 3)
for br, color, col_name in zip(brs, colors, columns):
    print(br,col_name)
    plt.bar(br, dfEdad[col_name], width=barWidth, color=color, label=col_name)


plt.xticks(br2, dfnew.groupby('edad').groups.keys())

ax = plt.gca()
for br, color, col_name in zip(brs, colors, columns):
    for j, v in enumerate(dfEdad[col_name].values):
        ax.text(br[j]-barWidth*0.5, v+1, f'{v:,.2f}', color=color, fontweight='bold',fontsize=8)

plt.title('Creatina por Edad')
plt.legend(loc='best')

#Glucosa
dfEdad = dfnew.pivot_table(index='edad',columns='glucosa',aggfunc='size',fill_value=0)

dfEdad = round(dfEdad.div(dfEdad.sum(axis=1),axis=0)*100,2)
print(dfEdad)
columns = dfEdad.columns.tolist()[0:]
colors = ['#ff335e', '#335eff', '#4cb274']
barWidth = 0.25

br1 = np.arange(dfEdad.shape[0]) - barWidth
br2 = br1 + barWidth
br3 = br2 + barWidth
brs = [br1, br2, br3]
print(br1)

plt.subplot(3, 2, 4)
for br, color, col_name in zip(brs, colors, columns):
    print(br,col_name)
    plt.bar(br, dfEdad[col_name], width=barWidth, color=color, label=col_name)


plt.xticks(br2, dfnew.groupby('edad').groups.keys())

ax = plt.gca()
for br, color, col_name in zip(brs, colors, columns):
    for j, v in enumerate(dfEdad[col_name].values):
        ax.text(br[j]-barWidth*0.5, v+1, f'{v:,.2f}', color=color, fontweight='bold',fontsize=8)

plt.title('Glucosa por Edad')
plt.legend(loc='best')

#Trigliceridos
dfEdad = dfnew.pivot_table(index='edad',columns='trigliceridos',aggfunc='size',fill_value=0)

dfEdad = round(dfEdad.div(dfEdad.sum(axis=1),axis=0)*100,2)
print(dfEdad)
columns = dfEdad.columns.tolist()[0:]
colors = ['#ff335e', '#335eff', '#4cb274']
barWidth = 0.25

br1 = np.arange(dfEdad.shape[0]) - barWidth
br2 = br1 + barWidth
br3 = br2 + barWidth
brs = [br1, br2, br3]
print(br1)

plt.subplot(3, 2, 5)
for br, color, col_name in zip(brs, colors, columns):
    print(br,col_name)
    plt.bar(br, dfEdad[col_name], width=barWidth, color=color, label=col_name)


plt.xticks(br2, dfnew.groupby('edad').groups.keys())

ax = plt.gca()
for br, color, col_name in zip(brs, colors, columns):
    for j, v in enumerate(dfEdad[col_name].values):
        ax.text(br[j]-barWidth*0.5, v+1, f'{v:,.2f}', color=color, fontweight='bold',fontsize=8)

plt.title('Trigliceridos por Edad')
plt.legend(loc='best')

#Insulina
dfEdad = dfnew.pivot_table(index='edad',columns='insulina',aggfunc='size',fill_value=0)

dfEdad = round(dfEdad.div(dfEdad.sum(axis=1),axis=0)*100,2)
print(dfEdad)
columns = dfEdad.columns.tolist()[0:]
colors = ['#ff335e', '#335eff']
barWidth = 0.25

br1 = np.arange(dfEdad.shape[0]) - barWidth
br2 = br1 + barWidth
brs = [br1, br2]
print(br1)

plt.subplot(3, 2, 6)
for br, color, col_name in zip(brs, colors, columns):
    print(br,col_name)
    plt.bar(br, dfEdad[col_name], width=barWidth, color=color, label=col_name)


plt.xticks(br2, dfnew.groupby('edad').groups.keys())

ax = plt.gca()
for br, color, col_name in zip(brs, colors, columns):
    for j, v in enumerate(dfEdad[col_name].values):
        ax.text(br[j]-barWidth*0.5, v+1, f'{v:,.2f}', color=color, fontweight='bold',fontsize=8)

plt.title('Insulina por Edad')
plt.legend(loc='best')
plt.show()

#Presion Arterial
dfEdad = dfnew.pivot_table(index='edad',columns='presion_arterial',aggfunc='size',fill_value=0)

dfEdad = round(dfEdad.div(dfEdad.sum(axis=1),axis=0)*100,2)
print(dfEdad)
columns = dfEdad.columns.tolist()[0:]
colors = ['#ff335e', '#335eff', '#4cb274','#a14cb2']
barWidth = 0.25

br1 = np.arange(dfEdad.shape[0]) - barWidth
br2 = br1 + barWidth
br3 = br2 + barWidth
br4 = br3 + barWidth
brs = [br1, br2, br3, br4]
print(br1)

plt.figure(figsize=(10,8))
for br, color, col_name in zip(brs, colors, columns):
    print(br,col_name)
    plt.bar(br, dfEdad[col_name], width=barWidth, color=color, label=col_name)


plt.xticks(br2, dfnew.groupby('edad').groups.keys())

ax = plt.gca()
for br, color, col_name in zip(brs, colors, columns):
    for j, v in enumerate(dfEdad[col_name].values):
        ax.text(br[j]-barWidth*0.5, v+1, f'{v:,.2f}', color=color, fontweight='bold',fontsize=8)

plt.title('Presion Arterial por Edad')
plt.legend(loc='best')
plt.show()

#Sueño
dfnew['sueno'] = df['sueno_horas'].apply(lambda x: 'Suficiente' if x >= 8 else 'Insuficiente')
dfSueno = dfnew.pivot_table(index='edad', columns='sueno', aggfunc='size', fill_value=0)
dfSueno = round(dfSueno.div(dfSueno.sum(axis=1), axis=0) * 100, 2)

columns = dfSueno.columns.tolist()
colors = ['#4caf50', '#f44336']  # Colores para 'Suficiente' e 'Insuficiente'
barWidth = 0.35
br1 = np.arange(dfSueno.shape[0]) - barWidth / 2
br2 = br1 + barWidth

plt.figure(figsize=(10, 6))
for br, color, col_name in zip([br1, br2], colors, columns):
    plt.bar(br, dfSueno[col_name], width=barWidth, color=color, label=col_name)

plt.xticks(br1 + barWidth / 2, dfSueno.index, rotation=45)
ax = plt.gca()
for br, color, col_name in zip([br1, br2], colors, columns):
    for j, v in enumerate(dfSueno[col_name].values):
        ax.text(br[j] - barWidth * 0.25, v + 1, f'{v:,.2f}%', color=color, fontweight='bold', fontsize=8)

plt.title('Clasificación de Sueño por Edad')
plt.ylabel('Porcentaje')
plt.legend(loc='best')
plt.tight_layout()
plt.show()
# ------------------------------------------------------------------------------------

plt.figure(figsize=(16,10))
#estudio Adulto Mayor
dfAmayor = dfnew[dfnew['edad'].isin(['Adulto Mayor'])]
#Glucosa
dfAmayorCol = dfAmayor.pivot_table(index='presion_arterial',columns=['colesterol'],aggfunc='size',fill_value=0)
dfAmayorCol = round(dfAmayorCol.div(dfAmayorCol.sum(axis=1),axis=0)*100,2)

dfAmayorGls = dfAmayor.pivot_table(index='presion_arterial',columns=['glucosa'],aggfunc='size',fill_value=0)
dfAmayorGls = round(dfAmayorGls.div(dfAmayorGls.sum(axis=1),axis=0)*100,2)
print(dfAmayorGls)
columns = dfAmayorGls.columns.tolist()[0:]
colors = ['#ff335e', '#335eff', '#4cb274']
barWidth = 0.25

br1 = np.arange(dfAmayorGls.shape[0]) - barWidth
br2 = br1 + barWidth
br3 = br2 + barWidth
brs = [br1, br2, br3]
print(br1)

plt.subplot(2, 2, 1)
for br, color, col_name in zip(brs, colors, columns):
    print(br,col_name)
    plt.bar(br, dfAmayorGls[col_name], width=barWidth, color=color, label=col_name)


plt.xticks(br2, dfnew.groupby('presion_arterial').groups.keys())

ax = plt.gca()
for br, color, col_name in zip(brs, colors, columns):
    for j, v in enumerate(dfAmayorGls[col_name].values):
        ax.text(br[j]-barWidth*0.5, v+1, f'{v:,.2f}', color=color, fontweight='bold',fontsize=8)

plt.title('Glucosa Adulto Mayor')
plt.legend(loc='best')

#estudio Adulto Mayor Insulina
dfAmayorGls = dfAmayor.pivot_table(index='presion_arterial',columns=['insulina'],aggfunc='size',fill_value=0)
dfAmayorGls = round(dfAmayorGls.div(dfAmayorGls.sum(axis=1),axis=0)*100,2)
print(dfAmayorGls)
columns = dfAmayorGls.columns.tolist()[0:]
colors = ['#ff335e', '#335eff', '#4cb274']
barWidth = 0.25

br1 = np.arange(dfAmayorGls.shape[0]) - barWidth
br2 = br1 + barWidth
br3 = br2 + barWidth
brs = [br1, br2, br3]
print(br1)

plt.subplot(2, 2, 2)
for br, color, col_name in zip(brs, colors, columns):
    print(br,col_name)
    plt.bar(br, dfAmayorGls[col_name], width=barWidth, color=color, label=col_name)


plt.xticks(br2, dfnew.groupby('presion_arterial').groups.keys())

ax = plt.gca()
for br, color, col_name in zip(brs, colors, columns):
    for j, v in enumerate(dfAmayorGls[col_name].values):
        ax.text(br[j]-barWidth*0.5, v+1, f'{v:,.2f}', color=color, fontweight='bold',fontsize=8)

plt.title('Insulina Adulto Mayor')
plt.legend(loc='best')

#estudio Adulto Mayor Sueno
dfAmayorGls = dfAmayor.pivot_table(index='presion_arterial',columns=['sueno'],aggfunc='size',fill_value=0)
dfAmayorGls = round(dfAmayorGls.div(dfAmayorGls.sum(axis=1),axis=0)*100,2)
print(dfAmayorGls)
columns = dfAmayorGls.columns.tolist()[0:]
colors = ['#ff335e', '#335eff', '#4cb274']
barWidth = 0.25

br1 = np.arange(dfAmayorGls.shape[0]) - barWidth
br2 = br1 + barWidth
br3 = br2 + barWidth
brs = [br1, br2, br3]
print(br1)

plt.subplot(2, 2, 3)
for br, color, col_name in zip(brs, colors, columns):
    print(br,col_name)
    plt.bar(br, dfAmayorGls[col_name], width=barWidth, color=color, label=col_name)


plt.xticks(br2, dfnew.groupby('presion_arterial').groups.keys())

ax = plt.gca()
for br, color, col_name in zip(brs, colors, columns):
    for j, v in enumerate(dfAmayorGls[col_name].values):
        ax.text(br[j]-barWidth*0.5, v+1, f'{v:,.2f}', color=color, fontweight='bold',fontsize=8)

plt.title('Sueño Adulto Mayor')
plt.legend(loc='best')
plt.show()
# dfnew.to_csv('test.csv',index=False,encoding='utf-8')

# Filtrar los datos para eliminar presión baja
dfnew = eliminar_presion_baja(dfnew, 'presion_arterial')

# Guardar DataFrame limpio en un nuevo CSV
dfnew.to_csv('New_Hipertension_Arterial.csv', index=False, encoding='utf-8')