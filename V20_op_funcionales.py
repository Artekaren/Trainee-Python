#Ejercicio20: Operaciones Funcionales

#1. Map
numeros=[1,2,3,4,5,6]
map_numeros = list(map(lambda i: i*2,numeros))    #lambda se llama la función anónima
#En este caso la función anónima establece que cada elemento iterado se multiplicará por 2
print(map_numeros)

print('comparación')
#con for
numeros=[1,2,3,4,5,6]
map_numeros_con_for = []
for i in numeros:
    map_numeros_con_for.append(i * 2)
print(map_numeros)
print()




#2. Filter
a = [1,2,3,4,5,6,7]
return_even_filter = list(filter(lambda x: x % 2 == 0, a))
print(return_even_filter)

print('comparación')
#con for
a = [1,2,3,4,5,6,7]
return_even = []
for i in a:
    if i % 2 == 0:
        return_even.append(i)
print(return_even)

#3. Reduce
#reduce() es una función que toma como argumento un conjunto de valores (una lista, una tupla, o cualquier objeto iterable) y lo "reduce" a un único valor. Como se obtiene ese único valor a partir de la colección pasada como argumento dependerá de la función aplicada.
from functools import reduce
b = [1,2,3,4,5]
r=reduce(lambda x, y:x+y, b)
print(r)

print('comparación')
#con for
suma = 0
for i in b:
    suma += i
print(suma)
