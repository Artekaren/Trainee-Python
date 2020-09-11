#Desafío15: Generador de Lorem ipsum
#Crear un programa llamado lorem_generator.py , que sea capaz de mostrar en pantalla varios párrafos de "Lorem ipsum", donde el número de párrafos se especifica al cargar el script.
#El texto puede ser extraído del primer párrafo de https://www.lipsum.com/feed/html

import sys

import nltk




from urllib.request import urlopen
html = urlopen("https://www.lipsum.com/feed/html")
print(html)




aux=1
n=len(sys.argv)
for i in range(1,n):
    aux=int(sys.argv[i])

#print(sys.argv)
print(aux)
#print('La velocidad de escape es ',vel,' m/s')
