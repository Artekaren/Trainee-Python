#Desafio32: Adictos v2
#Se pide crear el programa adictos2.0.py con una función llamada scan_addicts2 . La función debe recibir una lista con los minutos de uso de los usuarios. Debe retornar una nueva lista cambiando todas las medidas inferiores a 90 minutos como 'bien', entre 90 y 180 como 'mejorable', y todas las mayores o iguales a 180 como 'mal'. Tip: Cuidado con las condiciones de borde; analizar los casos de 90 y 180 ['mejorable', 'mejorable', 'mal', 'bien', 'mejorable', 'bien', 'mal', 'mal', 'mal']


def scan_addicts2(lista):
    results = []
    for i in lista:
        if i >= 180:
            results.append('mal')
        elif i >= 90:
            results.append('mejorable')
        else:
            results.append('bien')
    return results

lista_adictos = [120, 90, 600, 30, 90, 10, 200, 180, 500]
print(scan_addicts2(lista_adictos))
