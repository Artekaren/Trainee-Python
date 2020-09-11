#Desafío37: Filtrado. Dados los siguientes datos, crear un METODO que devuelva otro diccionario pero filtrando todos aquellos pares con un valor inferior a 70000.

ventas_mensuales = {
"Octubre": 65000,
"Noviembre": 68000,
"Diciembre": 72000,
}

def filtrar_valores_altos(diccionario):
    diccionario_filtrado = {}
    for clave, valor in diccionario.items():
        if valor > 70000:
            diccionario_filtrado[clave] = valor
    return diccionario_filtrado
print(filtrar_valores_altos(ventas_mensuales))
