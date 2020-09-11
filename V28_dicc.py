#Ejercicio28: Diccionarios

#Creacion

notas = {'camila':7,'antonio':5,'felipe':6,'antonia':7}

#Entrega las notas de felipe
print(notas['felipe'])

#Si el valor está duplicado entrega el último valor asignado
duplicados = {'clave':1,'clave':2}
print(duplicados)

#Se puede agregar un nuevo elemento al final del Diccionario
notas['alejandro']=6
print(notas)

#Cambiar el valor a una clave: reasignación
notas['alejandro']=7
print(notas)

diccionario = {'nombre':'juan','apellido':'perez','edad':33,'altura':1.75}

#Imprime las llaves
for i in diccionario:
    print(i)

#Hace recorrido del diccionario: primera opción
for clave in diccionario:
    valor = diccionario[clave]
    print('La clave es {} y el valor es {}'.format(clave,valor))

#Para saber si existe una clave en un diccionario
print('nombre' in diccionario)

#Hace recorrido del diccionario: segunda opción
for clave,valor in diccionario.items():
    print(clave,valor)
