#Desafio21: Tablas de multiplicar.
#Tabla de un número: Supongamos que queremos mostrar una tabla de multiplicar. Por ejemplo la tabla del 5.

for i in range(10):
    print('5 * {} = {}'.format(i, (5 * i)))
    print()

#Tablas de todos los números. En este caso, el código no es complejo, y se justifica el uso de dos for anidados, porque facilita el problema planteado.

for j in range(10):
    for k in range(10):
        print('{} * {} = {}'.format(j,k, (k * j)))
    print()
