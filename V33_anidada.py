#Ejercicio33:

lista_anidada = [1, [2, [3, 4, [5, 6], 7]], 8, [9, 10]]
for elemento in lista_anidada:
    print(elemento)


a = 5
b = 'casa'
c = [1, 2]
print(isinstance(a, list))
print(isinstance(b, list))
print(isinstance(c, list))

#Esta función aplana la lista
#isinstance indica si el elemento dentro de la lista correspode a una sublista
def imprimir(lista):
    for elemento in lista:
        if isinstance(elemento, list):
            imprimir(elemento)
        else:
            print(elemento)

imprimir(lista_anidada)
