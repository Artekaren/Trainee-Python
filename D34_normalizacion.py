#Desafio34: Normalizacion
#Normalización.py. La normalización vectorial busca reexpresar entre 0 y 1 una serie de valores contenidos en una lista. Suena mucho más complejo de lo que es. Consiste en que, dado un arreglo con valores, se genere un nuevo arreglo donde todos los valores están entre cero y uno. Para lograrlo, cada valor del arreglo se debe dividir por el módulo, y el módulo se calcula como la raíz de la suma de cada uno de los elementos al cuadrado.
#Se necesita:
#Una función para cacular el módulo de un arreglo.
#Dividir cada uno de los elementos del arreglo por el módulo y guardarlos en un nuevo arreglo. El resultado es posible de verificar dado que la suma de todos los valores al cuadrado debe ser uno.
#_Tip:_ Para implementar la raíz cuadrada, importar el módulo math y ocupar la función sqrt


import math
def modulo(lista):
    suma = 0
    for i in lista:
        suma = suma + i**2
    return math.sqrt(suma)

vector = [1, 2, 3, 4, 5, 6]
print(modulo(vector))

def normalizar(lista):
    m = modulo(lista)
    normalized_array = []
    for i in lista:
        normalized_array.append(i / m)
    return normalized_array

output_array = normalizar([1, 2, 3])
print(output_array)

## Verificamos el resultado: la suma de cada uno de los números al cuadrado debe ser uno, esto lo podemos probar iterando el arreglo.
suma = 0
for i in output_array:
    suma += i ** 2
print('Verificación: ',suma)
