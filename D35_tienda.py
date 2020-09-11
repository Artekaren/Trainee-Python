#Desafio35: Artículos de tienda
#Se tiene una lista de categoría, nombres y precios de artículos que están intercalados, donde primero viene la categoría, luego el nombre del artículo y luego su precio. Los precios están ingresados como datos de texto, no como numéricos: El dueño de la tienda requiere detectar aquellos artículos que cuesten más de $80.000, que no sean notebooks, y aplicarles un descuento de 10%. Se requiere que estos nuevos precios se separen en listas por categoría de artículo, ordenados de mayor a menor.


articulos = ['celular', 'LG K10', '90000', 'tablet', 'Galaxy TAB', '80000', 'smart tv',
'LED 43 Samsung', '485000', 'celular', 'Galaxy J7', '120000', 'celular', 'Huawei Y5', '59900', 'notebook', 'Lenovo ideapad', '250000', 'tablet', 'Huawei media', '139000', 'notebook', 'Acer', '145000']

celulares = []
tablets = []
smart_tv = []
notebooks = []

# Generamos variable auxiliar para almacenar la categoría recorrida
aux = ''
# Luego se itera la lista de artículos con enumerate
for index, elemento in enumerate(articulos):

# Se almacena el precio en una variable auxiliar
    if (index == 0 or index % 3 == 0):
        aux = elemento

    elif (index - 2) % 3 == 0:

        int_precio = int(elemento)
        precio_final = int_precio

        if (precio_final > 80000 and aux is not 'notebook'):
            precio_final = int(precio_final * 0.9)

        if aux == 'celular':
            celulares.append(precio_final)
        elif aux == 'notebook':
            notebooks.append(precio_final)
        elif aux == 'smart tv':
            smart_tv.append(precio_final)
        elif aux == 'tablet':
            tablets.append(precio_final)

# Ordenar precios de mayor a menor
celulares.sort()
celulares.reverse()

notebooks.sort()
notebooks.reverse()

smart_tv.sort()
smart_tv.reverse()

tablets.sort()
tablets.reverse()

# Output
print('Celulares: ', celulares)
print('Notebooks: ', notebooks)
print('Smart tv: ', smart_tv)
print('Tablets: ', tablets)
