#Desafío24: Concatenando letras
#Crear una función llamada gen que reciba el número de letras a generar, y devuelva un string con todas las letras generadas concatendas.
#Ejemplo:
#gen 4
#"abcd"
#gen 10
#"abcdefghij"


def gen(cant):
    lista = ['a','b','c','d','e','f','g','h','i','j','l','m','n','ñ','o','p','q','r','s','t','u','v','w','x','y','z']
    if cant<=26:
        for i in range(-1,cant-1,1):
            i+=1
            print(lista[i],end="")
    else:
        print('No es posible procesar el script')

import sys
cant = int(sys.argv[1])
gen(cant)
