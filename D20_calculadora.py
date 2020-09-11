#Desafío20: calculadora.py : Crear un programa que permita ingresar de 4 opciones, identificadas con un número (1: sumar, 2: restar, 3: multiplicar, 4: dividir). Luego el usuario debe ingresar 2 números, sobre los cuales se realice la operación escogida. El programa debe mostrar el resultado.


opcion = ''
while opcion != '5':
    print('Ingrese una opción')
    print('1: Sumar')
    print('2: Restar')
    print('3: Multiplicar')
    print('4: Dividir')
    print('5: Off')

    opcion = input()
    if opcion=='5':
        print('Off')
    if (opcion=='4' or opcion=='3' or opcion=='2' or opcion=='1'):
        num1 = int(input('Número 1: '))
        num2 = int(input('Número 2: '))

        if opcion=='1':
            print(num1+num2)
        elif opcion=='2':
            print(num1-num2)
        elif opcion=='3':
            print(num1*num2)
        elif opcion=='4':
            if num2==0:
                print('Error')
            else:
                print(float(num1/num2))
