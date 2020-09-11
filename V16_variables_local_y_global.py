#Ejercicio16: Variables locales
def ejemplo_local(parametro):
    print('Este es el parametro ',parametro)
    definida_dentro='Esta variable también es local'
    return parametro, definida_dentro

#Defino la variables: retorno para que almacene el valor que entrega la función
retorno=ejemplo_local('hola')
print(retorno)





#Ejemplo: Variables globales
mascota='gato'

def imprimir_mascota():
    print(mascota)

imprimir_mascota()
