#Ejercicio7: Suma los elementos de una lista que tiene 2 dimensiones
lista = [ [1, 2], [5, 4, 2], [12, 11, 120] ]
sum = 0
for i in lista:

    for j in i:
        sum += j
    print(i)
    print(sum)
