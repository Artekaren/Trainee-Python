#Desafio30: Funciones de listas
ingredientes = ['Masa Tradicional','Salsa de tomate','Queso']

opcion=1
while opcion<6:
    print('Gracias por ordenar con nosotros. ¿Qué desea realizar?')
    print('1. Consultar ingredientes de la pizza' )
    print('2. Cambiar tipo de masa')
    print('3. Modificar tipo de salsa')
    print('4. Agregar ingredientes')
    print('5. Eliminar ingredientes')
    print('6. Ordenar')

    # Guardar opción ingresada como int
    opcion = int(input())

    if opcion == 1:
        print('Ingredientes seleccionados:', ingredientes)
        print()

    # Opción 2, cambiar tipo de masa
    elif opcion == 2:
        # 2a: Consultar si entre los ingredientes está la masa tradicional
        if 'masa tradicional' in ingredientes:
            print('¿Cambiar masa tradicional por masa delgada?')
            print('Escriba S para cambiar, o N para conservar masa tradicional')
            print()
            cambiar = input().upper()
            # Si la respuesta es sí, se elimina masa tradicional, y se inserta la masa delgada
            if cambiar == 'S':
                ingredientes.remove('Masa Tradicional')
                ingredientes.insert(0, 'Masa Delgada')

        # 2b: Si tiene masa delgada
        elif 'masa delgada' in ingredientes:
            print('¿Cambiar masa delgada por tradicional?')
            print('Escriba S para cambiar, o N para conservar masa delgada')
            print()
            cambiar = input().upper()
            if cambiar == 'S':
                ingredientes.remove('Masa Delgada')
                ingredientes.insert(0,'Masa Tradicional')
        else:
            print('¡Su pizza no tiene masa!')
            print('Escoja 1 si desea Masa Tradicional, o 2 si desea Masa Delgada')
            print()
            masa = input()
            if masa == '1':
                ingredientes.insert(0,'Masa Tradicional')
            elif masa == '2':
                ingredientes.insert(0,'Masa Delgada')

    #xxx
    elif opcion == 3:
        # 3a: Consultar si entre los ingredientes está la salsa de tomate
        if 'salsa de tomate' in ingredientes:
            print('Digite: ')
            print('S: Cambiar a Salsa BBQ')
            print('N: Mantener Salsa de tomate')
            print('E: No incorporar Salsa')
            print()
            cambiar = input().upper()
            if cambiar == 'S':
                ingredientes.remove('salsa de tomate')
                ingredientes.insert(1,'salsa BBQ')
            elif cambiar == 'E':
                ingredientes.remove('salsa de tomate')

        elif 'salsa BBQ' in ingredientes:
            print('Digite: ')
            print('S: Cambiar a Salsa de Tomate')
            print('N: Mantener Salsa BBQ')
            print('E: No incorporar Salsa')
            print()
            cambiar = input().upper()      #upper cambia de minúsculas a mayúsculas

            if cambiar == 'S':
                ingredientes.remove('salsa BBQ')
                ingredientes.insert(1,'Salsa de Tomate')
            elif cambiar == 'E':
                ingredientes.remove('Salsa BBQ')

    # Opción 4, agregar ingredientes
    elif opcion == 4:
        # Lista de ingredientes
        print('¿Qué ingrediente desea agregar?')
        print('1. Tomate')
        print('2. Aceitunas')
        print('3. Queso')
        print('4. Peperoni')
        print('5. Pollo')
        print()
        nuevo = input().lower()

        if nuevo=='1':
            ingredientes.append('Tomate')
        elif nuevo=='2':
            ingredientes.append('Aceitunas')
        elif nuevo=='3':
            ingredientes.append('Queso')
        elif nuevo=='4':
            ingredientes.append('Peperoni')
        elif nuevo=='5':
            ingredientes.append('Pollo')
        elif (nuevo!='1' and nuevo!='2' and nuevo!='3' and nuevo!='4' and nuevo!='5'):
            print('Opción no válida')

    elif opcion == 5:
        # Consultamos el ingrediente para eliminar
        print('Ingredientes actuales: ', ingredientes)
        print('¿Cuál ingrediente desea eliminar?')
        print('1. Tomate')
        print('2. Aceitunas')
        print('3. Queso')
        print('4. Peperoni')
        print('5. Pollo')
        nuevo = input().lower()
        if nuevo=='1':
            ingredientes.remove('Tomate')
        elif nuevo=='2':
            ingredientes.remove('Aceitunas')
        elif nuevo=='3':
            ingredientes.remove('Queso')
        elif nuevo=='4':
            ingredientes.remove('Peperoni')
        elif nuevo=='5':
            ingredientes.remove('Pollo')

    elif opcion == 6:
        print('Su pedido está listo. Disfrute su pizza')
        print(ingredientes)

    elif (opcion!=1 or opcion!=2 or opcion!=3 or opcion!=4 or opcion!=5 or opcion!=6):
            print('Debe ingresar una opción válida')
