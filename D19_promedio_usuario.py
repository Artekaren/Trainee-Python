#Desafío19: promedio_usuario.py : El usuario debe ingresar un número, el cual indica al programa la cantidad de datos que se van a ingresar. Luego, debe ingresar la cantidad de datos indicada. El programa debe mostrar el promedio de los datos ingresados a continuación del primer argumento.

import sys
datos = []
num = int(sys.argv[1])
i=0
while i<num:
    i+=1
    datos.append(int(input('Ingrese valor: ')))
print(datos)

sum = 0
for j in datos:
    sum += j
prom=float(sum/num)
print('La suma es de los números es {} y dividido por {} es {}'.format(sum,num,prom))
