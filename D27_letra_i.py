#Desafío27: Programa de letras
#La función letra_i(n) , la cual al ser llamada, retornará una cadena de texto que al ser imprimida con print, dibujará una letra "i" según el ejemplo print(letra_i(5))

import sys
num=int(sys.argv[1])

def letra_i(num):
    contain=''
    for i in range(num):
        contain+='*'
    x='\n'+contain+'\n'

    contain_middle=''
    aux=num
    for i in range(0,num-3,1):
        contain_middle+=' '
    contain_middle+='*\n'
    y=contain_middle*(num-2)+contain

    return x+y

    #return x

print(letra_i(num))
