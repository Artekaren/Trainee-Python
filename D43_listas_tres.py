#Desafio43:Generar un loop que muestre en pantalla aquellos autos cuyo segundo campo (el número flotante) es mayor al de la media de todos los autos.

import pandas as pd

df_auto = pd.read_csv('auto.csv')
auto=df_auto.values.tolist()
#print('Lista original: {}'.format(auto))
#print('-----------------------------------------------------------------------')

#print('Lista traspuesta:')
traspuesta = [[row[i] for row in auto] for i in range(len(auto)-1)]
#print(traspuesta)
#print('-----------------------------------------------------------------------')

def mostrar(matriz):
    for fila in matriz:
        print(fila)


fil = len(traspuesta)
col = len(traspuesta[0])

res = []
suma = 0
cont = 0
for i in range(fil):
    if (type(traspuesta[i][0]) is int or type(traspuesta[i][0]) is float):
        for j in range(col):
            suma = suma + traspuesta[i][j]
            prom = suma / col
        traspuesta[i].append(prom)

        suma = 0
        cont += 1

        for j in range(col):
            if traspuesta[i][j]>traspuesta[i][col]:
                res.append(traspuesta[0][j])
                res.append(traspuesta[i][j])

                fil_2 = len(auto)
                col_2 = int(len(auto)/cont)
                res_ord = [res[col_2*i : col_2*(i+1)] for i in range(fil_2)]

    else:
        traspuesta[i].append('NaN')

#mostrar(traspuesta)
mostrar(res_ord)
