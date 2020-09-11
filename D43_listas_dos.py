#Desafio43: Utilizar la función construída en el Desafío - Velocidad para obtener la media entre los 6 autos para cada uno de los campos numéricos.

import numpy as np
import pandas as pd
from functools import reduce

df_auto = pd.read_csv('auto.csv')
auto=df_auto.values.tolist()
print('Lista original: {}'.format(auto))
print('-----------------------------------------------------------------------')

print('Lista traspuesta:')
traspuesta = [[row[i] for row in auto] for i in range(len(auto)-1)]
print(traspuesta)
print('-----------------------------------------------------------------------')

print('Lista plana:')
lista_plana = [ element for sublist in traspuesta for element in sublist]
print(lista_plana)
print('-----------------------------------------------------------------------')

#Función filtra los strings
nueva_lista = []
def extraer_str(lista):
    for i, _ in enumerate(lista):
        if (type(lista[i]) is int or type(lista[i]) is float):
            nueva_lista.append(lista[i])
    return nueva_lista

print('Lista plana filtrada')
print(extraer_str(lista_plana))
print('-----------------------------------------------------------------------')

fil = int(len(nueva_lista)/len(auto))
col = len(auto)
lista_filtrada = [nueva_lista[col*i : col*(i+1)] for i in range(fil)]
print('Lista original filtrada:')
print(lista_filtrada)
print('-----------------------------------------------------------------------')


sum = 0
for i in lista_filtrada:
    for j in i:
        sum += j
        prom = sum / len(auto)
    print('El promedio de {} es {}'.format(i,prom))
print('-----------------------------------------------------------------------')
