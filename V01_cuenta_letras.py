# Ejercicio1: Obtener el número de caracteres que contiene una palabra
content = input('Ingrese una palabra:  ')
letters = len(content)
print("El contenido {} tiene {} letras".format(content, letters))

#Ejercicio 7: Cambiar minúscula a mayúsculas
cadena='gato'
print(cadena.upper())   #cambia minúsculas a mayúsculas. Metodo asociado a un objeto
print(len(cadena))      #entrega la longitud de caracteres. Metodo nativo

#Ejercicio 8: Creación de una calculadora
a = int(input())
b = int(input()) 
print("a + b es: {}".format(a + b))
print("a * b es: {}".format(a * b))
