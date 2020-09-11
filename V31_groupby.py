#Ejercicio31


from itertools import groupby

#Agrupación por clave
lista_a_dicc = [(k,list(g)) for k,g in groupby('AAAABBBCCD')]
print(lista_a_dicc)

#cantidad de datos por clave
cant_values_list = {k:len(list(g)) for k,g in groupby('AAAABBBCCD')}
print(cant_values_list)


#Ejercicio: Tenemos una lista de palabras, que queremos agrupar según su largo.
words = ['hola', 'a', 'todos', 'y', 'cada', 'uno']

words.sort(key=lambda x:len(x))   #SE DEBE ORDENAR PREVIAMENTE!!!     #esto permite ordenar la lista por largo

words_ord_group = {k:list(v) for k,v in groupby(words, key=len)}     #agrupamos
print(words_ord_group)
