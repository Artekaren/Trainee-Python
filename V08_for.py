#Ejercicio8: Ciclo for
for i in range(0,10,2):
    print(i)
print(list(range(10)))  #función list

for j in range(0,1000000,37):
    print(j)
    if j==296 :
        print('Encontrado')
        break   #break permite salida forzada del ciclo
    elif j>296:
        print('No existe el número 296')
        break

import sys

n = int(sys.argv[1])
contain=''
for k in range(n):
    if k%2==0:
        contain +='*'
    else:
        contain+='.'
print(contain)     #contain: contenedor
