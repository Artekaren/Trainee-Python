#Desafio46: Ahora necesitamos asociar cada registro de velocidad con la distancia recorrida. Para ello, se debe implementar la función zip . Ésta debe permitir asociar elementos entre dos listas (una de velocidades, y otra de distancias). Con esta función, se le solicita que cuente todas las observaciones que cumplan por lo menos con una de las siguientes condiciones:



#Velocidad sobre el promedio y distancia bajo el promedio.

velocidad = [4, 4, 7, 7, 8, 9, 10, 10, 10,
11, 11, 12, 12, 12, 12, 13, 13,
13, 13, 14, 14, 14, 14, 15, 15,
15, 16, 16, 17, 17, 17, 18, 18,
18, 18, 19, 19, 19, 20, 20, 20,
20, 20, 22, 23, 24, 24, 24, 24, 25]

distancia = [2, 10, 4, 22, 16, 10, 18, 26, 34,
17, 28, 14, 20, 24, 28, 26, 34, 34,
46, 26, 36, 60, 80, 20, 26, 54, 32,
40, 32, 40, 50, 42, 56, 76, 84, 36,
46, 68, 32, 48, 52, 56, 64, 66, 54,
70, 92, 93, 120, 85]

def promediar(lista):
    suma = 0
    for i in range(len(lista)):
        suma = suma + lista[i]
        prom = suma / len(lista)
    lista.append(prom)
    return lista[50]

print('La velocidad promedio es ',promediar(velocidad))
print('La distancia promedio es ',promediar(distancia))
print()

res = []
for i in range(len(velocidad)):
    if velocidad[i]>velocidad[50]:
        res.append(velocidad[i])
print('Velocidades sobre el promedio son',len(res),' :',list(zip(res,distancia)))
print()

res_2 = []
for i in range(len(velocidad)):
    if velocidad[i]<velocidad[50]:
        res_2.append(velocidad[i])
print('Velocidades bajo el promedio son',len(res_2),' :',list(zip(res_2,distancia)))
print()

res_3 = []
for i in range(len(distancia)):
    if distancia[i]<distancia[50]:
        res_3.append(distancia[i])
print('Distancia bajo el promedio son',len(res_3),' :',list(zip(velocidad,res_3)))
print()

res_4 = []
for i in range(len(distancia)):
    if distancia[i]>distancia[50]:
        res_4.append(distancia[i])
print('Distancia sobre el promedio son',len(res_4),' :',list(zip(velocidad,res_4)))
print()
