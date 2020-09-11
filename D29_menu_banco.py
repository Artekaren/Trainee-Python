#Desafío29: Menú de banco (Opcional)
"""Crear un programa que al ser ejecutado llame a la función mostrar_menu(saldo = x) la cual debe mostrar un menú con las siguientes opciones:
Bienvenido al portal del Banco Amigo. Escoja una opción:
1. Consultar saldo
2. Hacer depósito
3. Realizar giro
4. Salir

El parámetro saldo es opcional, y corresponde al saldo inicial con el que inicia el programa al ejecutarse. Por defecto debe ser 0 . El programa debe contar además con las siguientes funciones: Estas funciones no deben ser llamadas al ejecutar el programa. El llamado hacia cada una se explica después en la sección de requerimientos.

depositar(saldo, cantidad)
Función que recibe los parámetro saldo (int) y cantidad (int). Debe retornar el nuevo saldo , correspondiente al saldo ingresado más la cantidad .

girar(saldo, cantidad)
Función que recibe los parámetros saldo (int) y cantidad (int). Debe validar que cantidad no exceda a saldo . Si es así, debe retornar False . En caso contrario, debe restar esta cantidad a saldo , y retornar el resultado.

Requerimientos
1. Una vez que el usuario escoge una opción, se debe validar que las únicas opciones que se
pueda ingresar son 1 , 2 , 3 o 4 . Si se introduce otra opción, se debe mostrar el mensaje
"Opción inválida. Por favor ingrese 1, 2, 3 ó 4." , y volver a solicitar una opción.
2. Las funciones depositar() y girar() no deben contener print() . Las salidas deben
manejarse desde mostrar_menu() .
3. Al escoger la opción 1 , se debe mostrar el saldo actual en pantalla. Luego se vuelve a mostrar
el menú.
4. Al escoger la opción 2 , se debe solicitar la cantidad a depositar, y con ella llamar a la función depositar(saldo, cantidad) . Luego se debe mostrar el nuevo saldo en pantalla, y volver a
mostrar el menú.
5. Al escoger la opción 3 , primero se debe validar que exista saldo (debe ser mayor a 0). Si no
existe saldo, debe mostrar mensaje "No puede realizar giros. Su saldo es 0" . Si existe
saldo, se debe solicitar la cantidad a girar, y con ella llamar a la función girar(saldo,
cantidad).
Si la función retorna False , se debe mostrar el mensaje "No se puede girar esta
cantidad. Su saldo es de " (concatenar el valor de saldo ). Se debe solicitar
nuevamente la cantidad a girar y volver a llamar a la función girar(cantidad) . Nota: El
operador de comparación is es más estricto que == . En Python, de manera general se
considera el valor 0 como False . Si se desea comprobar que un objeto tiene
exactamente el valor False (y no 0 ), se debe usar is.
Si la función retorna un nuevo saldo (o sea, "no retorna False "), se debe mostrar el
nuevo saldo en pantalla, y volver a mostrar el menú.
5. Solo se detiene la ejecución del programa al escoger la opción 4 .
6. El saldo debe conservarse, de acuerdo a las operaciones que se realicen, durante una misma
ejecución del programa."""

def mostrar_menu():
    print('Bienvenido al portal del Banco Amigo. Escoja una opción:')
    print('1. Consultar saldo')
    print('2. Hacer depósito')
    print('3. Realizar giro')
    print('4. Salir')
    print()

def depositar(saldo,cantidad):
    saldo=saldo+cantidad
    return saldo




def girar(saldo,cantidad):
    if cantidad<=saldo:
        saldo = saldo - cantidad
        return saldo
    else:
        return saldo

opt_menu = 'cualquier valor'     #esta es la inicialiazión
saldo=30000
while opt_menu != '4':
    mostrar_menu()                # Se llama a la función
    opt_menu = input()
    if opt_menu == '1':
        print('Su saldo es $ ',saldo)
    elif opt_menu == '2':
        cantidad=int(input('Ingrese depósito: '))
        print('Su nuevo saldo es $ ',depositar(saldo,cantidad))
        saldo=depositar(saldo,cantidad)

    elif opt_menu == '3':
        if saldo==0:
            print('No puede realizar giros. Su saldo es $ 0')
        elif saldo!=0:
            cantidad=int(input('Ingrese giro: $ '))

            if cantidad<=saldo:
                print('Su nuevo saldo es $ ',girar(saldo,cantidad))
                saldo=girar(saldo,cantidad)
            else:
                print('No se puede girar esta cantidad. Su saldo es de $ ',saldo)

    elif opt_menu == '4':
        print('Saliendo')
    else:
        print('Opción inválida. Por favor ingrese 1, 2, 3 ó 4')
    print()
