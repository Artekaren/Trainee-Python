#Desafío25: Programa de letras
#1 La función letra_o(n) , la cual al ser llamada, retornará una cadena de texto que al ser imprimida con print, dibujará una letra "o" según el ejemplo print(letra_o(n))

import sys
num=int(sys.argv[1])

def dibujar(num):
    contain=''
    for i in range(num):
        contain+='*'
    print('\n',contain)

    contain_middle=' *'
    for i in range(0,num-3,1):
        contain_middle+=' '
    contain_middle+=' *\n'

    print(contain_middle*(num-2),contain)

dibujar(num)
