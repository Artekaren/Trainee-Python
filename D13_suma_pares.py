#Desafío13: Sumar pares
#Crear un programa llamado suma_pares.py que sume todos los números pares hasta "n" (incluyendo "n" si éste es par), donde "n" es ingresado por el usuario.

par = int(input("¿Hasta qué número quiere generar pares?\n"))
suma=0
if(par%2==0):
    for i in range(-2, par, 2):
        suma=suma+i+2
        print('Los números pares son: ',i+2)

else:
    for i in range(0, par, 2):
        suma=suma+i
        print('Los números pares son: ',i)
        
print('La suma de los números pares hasta',par,'es',suma)
