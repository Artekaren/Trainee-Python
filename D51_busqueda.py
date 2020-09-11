#Desafío51: Crear un programa llamado busqueda.py que pueda buscar a cuál mes pertenece una o mas cifras específicas. En caso de no encontrarlo mostrar el mensaje "no encontrado".

ventas = {
"Enero": 15000,
"Febrero": 22000,
"Marzo": 12000,
"Abril": 17000,
"Mayo": 81000,
"Junio": 13000,
"Julio": 21000,
"Agosto": 41200,
"Septiembre": 25000,
"Octubre": 21500,
"Noviembre": 91000,
"Diciembre": 21000,
}

import sys

def filtrar(diccionario,ingreso):
    for key,value in diccionario.items():
        if ingreso == value:
            return key

n = len(sys.argv)
for i in range(1,n):
    numero = int(sys.argv[i])
    key = filtrar(ventas,numero)
    if key == None:
        print('no encontrado')
    else:
        print(key)
