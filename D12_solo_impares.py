#Desafío12 - Números impares
#Crear un programa llamado solo_impares.py , que muestre todos los números impares hasta "n" (incluyendo "n", si éste es impar), donde "n" es un valor ingresado por el usuario.

impar = int(input("¿Hasta qué número quiere generar impares?\n"))
if(impar%2!=0):
    for i in range(1, impar+1, 2):
        print('Los números impares A son: ',i)
else:
    for i in range(1, impar, 2):
        print('Los números impares B son: ',i)
