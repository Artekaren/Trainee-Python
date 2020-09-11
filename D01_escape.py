#Desafio1: Se pide crear el programa escape.py donde el usuario ingrese la gravedad y el radio y como resultado obtenga la velocidad de escape.
# Importante: Utilizar args en lugar de input

def escape(*args):
    aux = 1
    for i in args:
        aux*=i
    vel=(2*aux*1000)**(.5)
    return vel

print('La velocidad de escape es',escape(9.8,6371),'m/s')
