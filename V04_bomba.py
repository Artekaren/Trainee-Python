#Ejercicio4: Bomba de 5 segundos
import time
i=5
while i>0:
    i-=1
    time.sleep(1)
    if i==0:
        print('BOOM!')
