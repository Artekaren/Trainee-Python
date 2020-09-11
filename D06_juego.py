#Desafío6: Piedra, Papel o Tijera
# Se pide crear el programa juego.py , el usuario pasará como argumento piedra, papel o tijera, el #programa escogerá una opción al azar jugará con número al azar.Para que el computador pueda jugar #escoger un número al azar entre 1 y 3, si es 1 entonces en piedra, si es 2 entonces papel y 3 #tijera. En caso que el argumento sea distinto a piedra papel o tijera el programa debe mostrar las #opciones que se pueden jugar.

import random
import sys
print('Piedra=1     Papel=2     Tijera=3')
resp=int(input('Piedra, Papel o Tijera:    '))
print('')

compu=random.randint(1,3)

if(resp==1 or resp==2 or resp==3):

    if (resp==compu):
        if(resp==1):
            print('Tu respuesta: Piedra')
            print('Computador juega Piedra')
            print('Empataste cabron')
        elif(resp==2):
            print('Tu respuesta: Papel')
            print('Computador juega Papel')
            print('Empataste cabron')
        elif(resp==3):
            print('Tu respuesta: Tijera')
            print('Computador juega Tijera')
            print('Empataste cabron')

    elif(compu==1 and resp==2):
        print('Tu respuesta: Papel')
        print('Computador juega Piedra')
        print('Ganaste wey')

    elif (compu==2 and resp==3):
        print('Tu respuesta: Tijera')
        print('Computador juega Papel')
        print('Ganaste wey')

    elif (compu==3 and resp==1):
        print('Tu respuesta: Piedra')
        print('Computador juega Tijera')
        print('Ganaste wey')

    else:
        aux=compu
        if(aux==1):
            print('Computador juega Piedra')
            print('Perdiste cabronazo')
        elif(aux==2):
            print('Computador juega Papel')
            print('Perdiste cabronazo')
        elif(aux==3):
            print('Computador juega Tijera')
            print('Perdiste cabronazo')
else:
    print('Opción no válida. Debe ingresar: Piedra=1     Papel=2     Tijera=3')
