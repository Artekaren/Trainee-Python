#Desafío7: El mayor de tres números
#Se pide crear el programa mayor.py. Este script debe tomar los 3 argumentos y determinar cual es el mayor.

#Usando listas
#append: agrega elementos a la lista

import sys
numeros = []

n=len(sys.argv)
for i in range(1,n):
  numero = int(sys.argv[i])
  numeros.append(numero)

#print(sys.argv)

mayor = numeros[0]
# Recorrer y comparar
for numero in numeros:
    if numero > mayor:
        mayor = numero
print("Mayor:", mayor)
