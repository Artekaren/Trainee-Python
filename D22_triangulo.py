#Desafío22: Dibujar un triángulo con for
num = int(input("Ingrese número\n"))
aux=num
for i in range(1,num+1):    #i son las filas
    for j in range(1,i+1):  #j son las columnas
        print('*',end="")
    print()
for i in range(aux,1,-1):    #i son las filas
    for j in range(i,1,-1):  #j son las columnas
        print('*',end="")
    print()
