#Ejercicio5: Concatenar strings con while
import sys
limite  = int(sys.argv[1])
i=0
suma = 0
while i< limite:
    i+=1
    suma+=i
print(suma)
saludo='hola'
saludo+=' mundo'
print(saludo)
