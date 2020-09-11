#Ejercicio32: Contando elementos dentro de un diccionario. Contar la cantidad de veces que aparece cada uno de los elementos.



#2 formas:

#Forma1: Iterar y contar
num = [1, 2, 6, 7, 2, 5, 8, 9, 1, 3, 6, 7]
diccionario = {}
for i in num:
    if i in diccionario:
        diccionario[i] += 1
    else:
        diccionario[i] = 1
print(diccionario)

#Forma2: Agrupar y contar
from itertools import groupby
num = [1, 2, 6, 7, 2, 5, 8, 9, 1, 3, 6, 7]
num.sort()
diccionario = {k:len(list(v)) for k,v in groupby(num)}
print(diccionario)
