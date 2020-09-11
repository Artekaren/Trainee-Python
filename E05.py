# Ejercicio 5: Obtener la representación inversa de una cadena de caracteres
cadena=input('Ingrese la palabra a invertir: ')

for i in range(len(cadena)-1,-1,-1):
    print(cadena[i],end='')
print()
print('La longitud de la cadena es: ',len(cadena))

#Notacion de slicing
print('')
print(cadena[::])
print('La palabra invertida es: ',cadena[::-1])