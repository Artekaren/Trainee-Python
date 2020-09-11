#Ejercicio34: Transformar diccionario a lista

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

#Primera forma
meses = list(ventas.keys())
montos = list(ventas.values())
print(meses)
print(montos)

#Segunda forma
meses = []
montos = []
for key in ventas:
    meses.append(key)
    montos.append(ventas[key])

#Tercera forma
meses = []
montos = []
for key,values in ventas.items():
    meses.append(key)
    montos.append(values)
