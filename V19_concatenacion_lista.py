#Ejercicio19:

#Concatenación de listas
colores_1=['rojo','naranjo','amarillo']
colores_2=['azul','celeste']
print(colores_1+colores_2)

concatenacion=colores_1+colores_2
print(concatenacion)

concatenacion=len(colores_1)+len(colores_2)
print(concatenacion)

#Operaciones repitiendo listas
colores_3=colores_1*3
print(colores_3)

#Membresía en listas
'verde' in colores_1     #devuelve false
'rojo' in colores_1        #devuelve true

print(colores_3.count('verde'))
print(colores_3.count('rojo'))

#Comprensiones de listas
nombres=['ariel','berta','cesar','diego','esteban']
nombre_mayusculas=[i.upper() for i in nombres]
print(nombre_mayusculas)

animales=['gato','perro','erizo']
animales_mayusculas=[i.upper() if i=='gato' else i.lower() for i in animales]
print(animales_mayusculas)



#Iteración: Primera forma
for i in animales:
    print(i)

#Iteración: Segunda forma
contador=0
for i in animales:
    print(animales)
    contador+=1

#iteracion con índices y elementos
for index,elemento in enumerate(animales):
    print('indice: ',index,'elemento: ',elemento)


#Transformacion del tipo de dato (string a int)

import sys
recibidos = sys.argv
cant = len(recibidos)
int_args = []
for i in range(1,cant):
    int_args.append(int(recibidos[i]))
print(int_args)

#Filtrar lista
num = [100,200,40,30,44,90,500]
mayores=[]
max_val = 80
for i in num:
    if i>max_val:
        mayores.append(i)
print(mayores)
