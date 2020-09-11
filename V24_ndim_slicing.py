#Ejercicio24:

#import pandas as pd
#df = pd.read_csv(nations.csv)

#Generar una matriz en numpy
import numpy as np

matriz = np.array([[0,1,2],[3,4,5],[6,7,8]])
print(matriz)
print(matriz[2])
print(matriz[2,1])
print(matriz[2][1])

lista_3d = np.array([
[[3, 5, 7, 9],
[8, 10, 12, 14],
[5, 15, 20, 25]],
[[6, 10, 14, 18],
[16, 20, 24, 28],
[10, 30, 40, 50]]
])

print(lista_3d)
print(lista_3d[0][1][2])

#slice
print(matriz[:2])
print(matriz[:2,1:])
print(matriz[0,1:])
