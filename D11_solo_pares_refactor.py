#Desafío11: Números pares
#Crear una variante del Desafio10 llamado solo_pares_refactor.py. En este caso, el cero no debe ser considerado (el cero no es par).

par = int(input("¿Hasta qué número quiere generar pares?\n"))
if(par%2==0):
    for i in range(0, par, 2):
        print('Los números pares son: ',i+2)
else:
    for i in range(2, par, 2):
        print('Los números pares son: ',i)
