#Desafío52 - Ventas. Considerar este diccionario para todos los siguientes ejercicios
#5. Generar programa quarters.py. Se pide generar un diccionario, llamado quarters , con las ventas de cada trimestre. Las claves tienen que ser "Q1" , "Q2" , "Q3" , "Q4".

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
meses = int(sys.argv[1])
if (meses == 6 or meses == 4 or meses == 3):
    cant_q = int(len(ventas)/meses)
else:
    print('Error!')
    sys.exit()


#Genera keys
keylist = []
for i in range(0,meses):
    keylist.append('Q'+str(i+1))

#Genera values
#Paso1: Transforma diccionario a lista de values
montos = list(ventas.values())

#Paso2: Transforma la lista de values a lista anidada
fil = meses
col = cant_q
order = [montos[col*i : col*(i+1)] for i in range(fil)]
#Paso3: Suma los elementos de la lista anidada
def sumar(list):
    ret = []
    suma = 0
    for i in range(fil):
        for j in range(col):
            suma = suma + list[i][j]
        ret.append(suma)
        suma = 0
    return ret

totales = sumar(order)

#Fusionar las listas para transformarlas en un diccionario
quarters = dict(zip(keylist,totales))
print(quarters)
