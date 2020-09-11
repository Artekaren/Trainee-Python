#Ejercicio17: Se prioriza la variable local por sobre la global

mascota='gato'
def imprimir_mascota():
    mascota='perro'
    print(mascota)

imprimir_mascota()   #imprime el valor de la variable local

print(mascota)       #imprime el valor de la variable local (desde el espacio MAIN)
