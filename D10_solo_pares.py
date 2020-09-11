#Desafío10: Números pares
#Crear un programa llamado solo_pares.py , que muestre todos los números pares hasta "n" (incluyendo "n", si éste es par), donde "n" es un valor ingresado por el usuario.

par = int(input("¿Hasta qué número quiere generar pares?\n"))
if(par%2==0):
    for i in range(-2, par, 2):
        print('Los números pares son: ',i+2)
else:
    for i in range(0, par, 2):
        print('Los números pares son: ',i)
