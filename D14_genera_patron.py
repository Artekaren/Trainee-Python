#Desafío14: Generar patrón
#Debe crear un programa que logre replicar el siguiente patrón, donde el usuario ingrese un número, y ese número corresponderá al número de filas que se debe generar. La soluciṕon debe estar dentro delprograma llamado genera_patron.py .
#1
#12
#123
#1234
#12345

num = int(input("Ingrese número\n"))
for i in range(1,num+1):    #i son las filas
    for j in range(1,i+1):  #j son las columnas
        print(j,end="")
    print()
