#Ejercicio6: Imprime una lista en html
import sys

#Opción 1: Imprime los elementos de la lista hacia el lado
items = int(sys.argv[1])
html = ''
i=0
while i<items:
    i+=1
    html+='<li>Elemento {}<li>'.format(i)
print(html)

#Opción 2: Imprime los elementos de la lista hacia abajo
items = int(sys.argv[1])
html = '<ul>\n'
i=0
while i<items:
    i+=1
    html+='\t<li>Elemento {}</li>\n'.format(i)    #\t: símbolo para la tabulación
html+='</ul>\n'
print(html)



#Opción 3: Imprime listas y sublistas
limit = int(sys.argv[1])
print('<ul>\n')

for i in range (limit):
    print('\t<li>\n')
    print('\t\t<ul>\n')
    for j in range(limit):
        print('\t\t\t<li>{},{}<\li>'.format(i,j))
    print('\t\t</ul>\n')
    print('\t</li>\n')

print('</ul>\n')
