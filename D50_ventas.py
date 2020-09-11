#Desafío50 - Ventas. Considerar este diccionario para todos los siguientes ejercicios

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

#1. Crear el programa iter1.py . Se solicita iterar el diccionario ventas y mostrar en pantalla todas los ventas superiores a 45000 (sólo el valor de la venta)
for key,value in ventas.items():
    if value > 45000:
        print("Las ventas superiores a $45.000 son {}".format(value))

#2. Iterar el diccionario ventas y mostrar en pantalla todos los meses cuyas ventas sean superiores a 45000.
for key,value in ventas.items():
    if value > 45000:
        print("Los meses con ventas superiores a $45.000 son {}".format(key))

#3. Se pide crear un programa llamado iter3.py, que contenga un método llamado filter y que reciba 2 argumentos, un diccionario y un valor a filtrar, este método tiene que devolver un diccionario nuevo con los valores superiores al valor ingresado al momento de llamar al programa.
def filter(dicc,vporfiltrar):
    dicc_filtrado = {}
    for key,value in dicc.items():
        if value > vporfiltrar:
            dicc_filtrado[key] = value
    return dicc_filtrado

print(filter(ventas,80000))

#6. Generar programa agrupados.py. Se solicita generar un diccionario con "n" claves, una para cada posible valor de venta dentro del diccionario. Para cada clave generada, se debe indicar cuántas veces estuvo presente ese valor.

montos = sorted(list(ventas.values()))
d = {i:montos.count(i) for i in montos}
print(d)
