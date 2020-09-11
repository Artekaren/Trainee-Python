#Ejercicio2: Generar un menú

opcion = ''
while opcion != 's':
    print('Ingrese una opción')
    print('1: Sumar 2+2')
    print('2: Multiplicar 2*3')
    print('s: Salida')

    opcion = input()

    if opcion=='1':
        print(2+2)
    elif opcion=='2':
        print(2*3)
    elif opcion=='s':
        print('Saliendo')
