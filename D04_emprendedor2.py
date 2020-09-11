#Desafío4: Rentabilidad
#Un emprendedor quiere crear una aplicación y necesita saber si es rentable.

#2. Crear el programa emprendedor2.py donde el usuario ingrese el precio, el número de
#usuarios totales(incluyendo a usuarios premium y gratuitos), el número de usuarios
#premium(pagan el doble), el número de usuarios gratuitos(no pagan) y los gastos. El programa debe calcular las utilidades.

import sys
Utilidad=1
n=len(sys.argv)
for i in range(1,n):
    Utilidad=2*int(sys.argv[1])*int(sys.argv[2])+0*int(sys.argv[1])*int(sys.argv[3])-int(sys.argv[4])
    if (Utilidad>0):
        Utilidad=0.65*Utilidad
    else:
        Utilidad=Utilidad

#print(sys.argv)
print('Precio de venta en dolares: ',sys.argv[1]+'\n','Número de usuarios premium:',sys.argv[2]+'\n','Número de usuarios gratuitos:',sys.argv[3]+'\n','Gastos en dolares:',sys.argv[4])
print('La utilidad del proyecto es',Utilidad,'dolares')









#3. Crear el programa emprendedor3.py donde el usuario ingrese el precio, el número de
#usuarios, los gastos y las utilidades del año anterior, este último parámetro será optativo, si el usuario no lo ingresa se asumirá 1000 como base.
