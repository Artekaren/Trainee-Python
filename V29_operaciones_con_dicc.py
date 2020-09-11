#Ejercicio29: Operaciones típicas en diccionarios

#1. Eliminar un elemento dentro de un diccionario. 2 formas. La principal diferencia entre ambas formas es que al utilizar pop obtendremos el valor del elemento eliminado.
diccionario = {"celular": 140000, "notebook": 489990, "tablet": 120000, "cargador":
12400}

#Del
del diccionario["celular"]
print(diccionario)

#Pop
eliminado = diccionario.pop("tablet")
print(eliminado)
print(diccionario)
print('-----------------------------------------------------------------------')

#2. Unir dos diccionarios en uno solo
diccionario_a = {"nombre": "Alejandra", "apellido": "López", "edad": 33, "altura": 1.55}
diccionario_b = { "mascota":"miti", "ejercicio":"bicicleta"}

diccionario_a.update(diccionario_b)
print(diccionario_a)     # Notar que la unión queda en el primer diccionario

#Alcance: Cuidado con las colisiones. Cuando ambos diccionarios tienen una clave en común, el valor del segundo diccionario sobreescribe al del primero

diccionario_a = {'nombre': 'Alejandra', 'apellido': 'López', 'edad': 33, 'altura': 155}
diccionario_b = {'mascota':
'miti', 'ejercicio': 'bicicleta','altura': 155}
diccionario_a.update(diccionario_b)
print(diccionario_a)
print('-----------------------------------------------------------------------')

#3. Invertir un diccionario
colors = {
"red": "#cc0000",
"green": "#00cc00",
"blue": "#0000cc",
}
colors_inv = {v:k for k,v in colors.items()}     #v: se refiere a value y k a key
print(colors_inv)
print('-----------------------------------------------------------------------')

#4. Obtener todas las claves y valores de un diccionario

#4.A. Obtener todas las claves
colors = {
"red": "#cc0000",
"green": "#00cc00",
"blue": "#0000cc",
}
print(colors.keys())

#4.B. Obtener todos las valores
colors = {
"red": "#cc0000",
"green": "#00cc00",
"blue": "#0000cc",
}
print(colors.values())
print('-----------------------------------------------------------------------')

#5. Construir un diccionario a partir de claves y valores. La función zip se usa para unir dos listas, una como key y la otra como value, y convertir esa unión en un diccionario.
print(dict(zip(["k1", "k2", "k3"], [1, 2, 3])))
print('-----------------------------------------------------------------------')





#4. Transformar las claves del diccionario en una lista






#5. Transformar los valores del diccionario en una lista
