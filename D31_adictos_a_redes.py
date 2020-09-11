#Desafio31: Adictos a redes
#Se tiene una lista con la cantidad de minutos usados en redes sociales de distintos usuarios. Se pide crear la función adictos_a_redes(lista) que reciba una lista con los minutos de uso. La función debe retornar un nuevo arreglo con todas las medidas inferiores a 90 minutos como 'bien' y todas las mayores o iguales a 90 como 'mal'.

#El output debería ser algo similar a lo siguiente ['mal', 'bien', 'mal', 'bien', 'bien', 'bien', 'mal', 'bien', 'mal']

def adictos_a_redes(lista):
    results = []
    for i in lista:
        if i > 90:
            results.append('mal')
        else:
            results.append('bien')
    return results

lista_adictos = [120, 50, 600, 30, 90, 10, 200, 0, 500]
print(adictos_a_redes(lista_adictos))
