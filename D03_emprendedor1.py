#Desafío3: Rentabilidad
#Un emprendedor quiere crear una aplicación y necesita saber si es rentable.

#1. Crear el progama emprendedor1.py donde el usuario ingrese el precio, el número de
#usuarios, los gastos y el programa calcula las utilidades. Los impuestos aplicados a las utilidades son el 35% y solo aplican si es positivo.

import sys
Utilidad=1
n=len(sys.argv)
for i in range(1,n):
    Utilidad=int(sys.argv[1])*int(sys.argv[2])-int(sys.argv[3])
    if (Utilidad >0):
        Utilidad=0.65*Utilidad
    else:
        Utilidad=Utilidad

#print(sys.argv)
print('Precio de venta en dolares: ',sys.argv[1]+'\n','Número de usuarios al año:',sys.argv[2]+'\n','Gastos en dolares:',sys.argv[3])
print('La utilidad del proyecto es',Utilidad,'dolares')
