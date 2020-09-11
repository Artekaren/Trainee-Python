#Desafio2: Se pide crear el programa escape.py donde el usuario ingrese la gravedad y el radio y como resultado obtenga la velocidad de escape.
# Importante: Utilizar args en lugar de input

import sys
aux=1
n=len(sys.argv)
for i in range(1,n):
    aux*=float(sys.argv[i])
    vel=(2*aux*1000)**(.5)
#print(sys.argv)
print('La velocidad de escape es ',vel,' m/s')
