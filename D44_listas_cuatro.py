#Desafio44: Utilizar los valores booleanos de cada lista (penúltimo campo) para mostrar en pantalla el nombre del auto correspondiente, en caso de que este valor sea True.

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
cont = 0
for i in range(fil):
    if type(traspuesta[i][0]) is bool:
        for j in range(col):
            if traspuesta[i][j] is True:
                res.append(traspuesta[0][j])
                res.append(traspuesta[i][j])

fil_2 = i
col_2 = 2
res_ord = [res[col_2*i : col_2*(i+1)] for i in range(fil_2)]

mostrar(traspuesta)
print('')
mostrar(res_ord)
