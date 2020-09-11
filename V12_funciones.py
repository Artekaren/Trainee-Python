#Ejercicio12: Diferentes tipos de funciones

#Llamadas

#Caso1:
print(len('arbol'))

#Caso2:
print('casa'.upper())

#Caso3:
nombre = 'mateo'
print(nombre.upper())

#Caso4:
import random
print(random.randint(2,12))

#Creación de funciones
def multiplicar():                 #Ej1
    print(2*2)

def multiplicar_dos_numeros(x,y):    #Ej2
    print(x*y)

def multiplicar_opcional(x,y=10):    #Ej3
    print(x*y)



multiplicar()                    #Primer ejemplo de llamado

multiplicar_dos_numeros(5,7)     #Segundo ejemplo de llamado

a=int(input())
b=int(input())
multiplicar_dos_numeros(a,b)     #Tercer ejemplo de llamado



multiplicar_opcional(4)       #Cuarto ejemplo de llamado

multiplicar_opcional(4,2)     #Quinto ejemplo de llamado


for i in range(1,6):
    for j in range(1,6):
        multiplicar_dos_numeros(i,j)     #Sexto ejemplo de llamado
