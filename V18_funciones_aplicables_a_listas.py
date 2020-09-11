#Ejercicio18: Funciones aplicacles a listas
lista_de_numeros = [1,2,3,4,5,6,7,8,9,10]
#print(lista_de_numeros.__dir__())

#Funcion append (no tiene retorno)
colores=['verde','rojo','rosa','azul']
colores.append('celeste')
print(colores)

#Funcion insert (no tiene retorno)
colores.insert(3,'morado')    #Desplaza los elementos
print(colores)
colores.insert(20,'lila')    #Desplaza los elementos
print(colores)

#Funcion pop (sí tiene retorno)
popeado=colores.pop()   #Saca el último elemento de la lista
print(popeado)
print(colores)

popeado_2=colores.pop(1)   #Saca el último elemento de la lista
print(popeado_2)
print(colores)

#Funcion remove (no tiene retorno)
removido=colores.remove('verde')
print(removido)     #Entrega none porque no tiene retorno
print(colores)

#colores.remove('blanco')
#print(colores)    #Entrega Error porque el elemento no está en la lista

#Funcion reverse
animales=['perro','gato','hurón','erizo']
numeros=[100,20,70,500]
numeros.reverse()
print(numeros)
animales.reverse()
print(animales)

#Funcion sort
numeros.sort()  #los ordena de menor a mayor
print(numeros)
animales.sort()   #Los ordena en orden alfabetico
print(animales)
