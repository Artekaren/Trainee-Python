#Desafío38: Integración. Se tiene la siguiente lista de productos: Se solicita: Si el producto tiene un valor menor a 120.000, se le debe aplicar un 10% de descuento (en el diccionario original). En caso contrario, se debe asignar a un nuevo diccionario de filtrado.

diccionario_productos = {"celular": 140000, "notebook": 489990, "tablet": 120000,
"cargador": 12400}

dic_prod_filtrado = {}
for producto, precio in diccionario_productos.items():
    if precio < 120000:
        diccionario_productos[producto] = precio * 0.9
    else:
        dic_prod_filtrado[producto] = precio

print(diccionario_productos)
print(dic_prod_filtrado)
