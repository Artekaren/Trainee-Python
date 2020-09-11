#Ejercicio13: Se presentan dos formas de definir una función para transformar de grados Fahrenheit a grados Celcius.

# Opción 1:
def fahrenheit():
    fahrenheit = int(input('Ingrese la temperatura en Fahrenheit: '))
    celsius = (fahrenheit + 40) / 1.8 - 40
    print('La temperatura es de {} grados Celsius'.format(celsius))

# Opción 2:
def fahrenheit(f):
    celsius = (f + 40) / 1.8 - 40
    print("La temperatura es de {} grados Celsius".format(celsius))
fahrenheit(int(input('Ingrese la temperatura en Fahrenheit: ')))


#Se puede llamar a la función utilizando un valor al azar y también se puede llamar utilizando un valor entregado por el usuario, el cual se puede previamente guardar en una variable:

import random
def fahrenheit(f):
    celsius = (f + 40) / 1.8 - 40
    print('La temperatura es de {} grados Celsius'.format(celsius))
fahrenheit(random.randint(1, 100))

#Y también se puede llamar utilizando un valor entregado por el usuario, el cual se puede previamente guardar en una variable:

far_user = int(input('Ingrese la temperatura en Fahrenheit: '))
fahrenheit(far_user)
