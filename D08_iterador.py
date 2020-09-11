#Desafío8: Reemplazar while por for
#Reemplazar la instrucción while por for dentro del programa llamado iterador.py .

i=0
while i<5:
    print("iteracion {}".format(i+1))
    i+=1

for i in range(0,5):
    i+=1
    print('iteracion',i)
