#Desafío9: Reemplazar instrucción for por while
#Reemplaza la instrucción for por while dentro del programa llamado cuenta_regresiva.py .

cuenta_regresiva = int(input("Ingrese un número para comenzar la cuenta regresiva\n"))
for i in range(cuenta_regresiva):
    tmp = cuenta_regresiva
    print("Iteración {}".format(tmp - i))

i = int(input("Ingrese un número para comenzar la cuenta regresiva\n"))
while i>0:
    print("Iteracion {}".format(i))
    i-=1
