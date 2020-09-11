#Desafío26: Programa de letras
#La función letra_o(n) , la cual al ser llamada, retornará una cadena de texto que al ser imprimida con print, dibujará una letra "o" según el ejemplo print(letra_o(n))

import sys
num=int(sys.argv[1])

def letra_o(num):
    contain=''
    for i in range(num):
        contain+='*'
    x='\n'+contain+'\n'

    contain_middle='*'
    for i in range(0,num-3,1):
        contain_middle+=' '
    contain_middle+=' *\n'
    y=contain_middle*(num-2)+contain

    return x+y

print(letra_o(num))
