import matplotlib.pyplot as plt

# Datos para la gráfica de barras
categorias = ['A', 'B', 'C', 'D']
valores = [4, 7, 1, 8]

# Crear la gráfica de barras
plt.bar(categorias, valores)

# Agregar los valores encima de cada barra
for i, valor in enumerate(valores):
    plt.text(i, valor + 0.1, str(valor), ha='center', va='bottom', fontsize=10, color='black')

# Opciones de la gráfica
plt.xlabel('Categorías')
plt.ylabel('Valores')
plt.title('Gráfica de barras con valores sobre cada barra')

# Mostrar la gráfica
plt.show()
