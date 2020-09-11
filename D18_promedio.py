#Desafío18: promedio.py : El usuario debe ingresar número. El programa debe sumar todos los números desde 1 hasta el número ingresado. Luego, debe mostrar el resultado de la suma divido por la cantidad de iteraciones.
import sys
num = int(sys.argv[1])
sum=0
i=0
while i<num:
    i+=1
    sum+=i
prom=float(sum/i)
print('La suma es {} y dividido por {} es {}'.format(sum,i,prom))
