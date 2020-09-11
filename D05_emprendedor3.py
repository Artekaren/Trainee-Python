#Desafío5: Rentabilidad
#Un emprendedor quiere crear una aplicación y necesita saber si es rentable.

#3. Crear el programa emprendedor3.py donde el usuario ingrese el precio, el número de
#usuarios, los gastos y las utilidades del año anterior, este último parámetro será optativo,
#si el usuario no lo ingresa se asumirá 1000 como base.

import sys
Utilidad=1
n=len(sys.argv)
if (n==5):
    for i in range(1,n):
        Utilidad=int(sys.argv[1])*int(sys.argv[2])-int(sys.argv[3])
        if (Utilidad>0):
            Utilidad=0.65*Utilidad+int(sys.argv[4])
        else:
            Utilidad=Utilidad
else:
    for i in range(1,n):
        Utilidad=int(sys.argv[1])*int(sys.argv[2])-int(sys.argv[3])
        if (Utilidad>0):
            Utilidad=0.65*Utilidad+1000
        else:
            Utilidad=Utilidad

if (n==5):
    print('Precio de venta en dolares: ',sys.argv[1]+'\n','Número de usuarios:',sys.argv[2]+'\n','Gastos en dolares:',sys.argv[3]+'\n','Utilidad año anterior:',sys.argv[4])
    print('La utilidad del proyecto es',Utilidad,'dolares')
else:
    print('Precio de venta en dolares: ',sys.argv[1]+'\n','Número de usuarios:',sys.argv[2]+'\n','Gastos en dolares:',sys.argv[3]+'\n','Utilidad año anterior: 1000')
    print('La utilidad del proyecto es',Utilidad,'dolares')
#print(sys.argv)
