#Desafío36: Transformación. Dada la información de ventas de 3 meses. Requerimientos: Modificar el diccionario para incrementar las ventas en un 10%. Hacer un nuevo diccionario pero con las ventas disminuidas un 20%

ventas_mensuales = {
"Octubre": 65000,
"Noviembre": 68000,
"Diciembre": 72000,
}

for mes, venta in ventas_mensuales.items():
    ventas_mensuales[mes] = venta * 1.1
print(ventas_mensuales)

nuevas_ventas_mensuales = {}
for mes, venta in ventas_mensuales.items():
    nuevas_ventas_mensuales[mes] = venta * 0.8
print(nuevas_ventas_mensuales)
print(ventas_mensuales)
