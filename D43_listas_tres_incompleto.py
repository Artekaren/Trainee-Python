#Desafio43:Generar un loop que muestre en pantalla aquellos autos cuyo segundo campo (el número flotante) es mayor al de la media de todos los autos.

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

def prom(list):
    lista_prom = []
    sum = 0
    for i in list:
        for j in i:
            sum += j
            prom = sum / len(auto)
        lista_prom.append(prom)
    return(lista_prom)

#print(prom(lista_filtrada,len(auto)))

prom_2 = []
prom_2 = prom(lista_filtrada)
filtro = []
for subl in traspuesta:
    for j, _ in enumerate(subl):
        if (type(subl[j]) is int or type(subl[j]) is float):
            filtro.append(subl[j])
filtrada_2 = [filtro[col*i : col*(i+1)] for i in range(fil)]

resp = []
for subl_2 in filtrada_2:
    for i, _ in enumerate(subl_2):
        if subl_2[i]>prom_2[0]:
            resp.append(subl_2[i])
print(resp)
