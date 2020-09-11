#Ejercicio10: Dibujar cuadrado vacío con for
import sys
n=int(sys.argv[1])
contain=''
for i in range(n):
    contain+='*'
print('\n',contain)

contain_middle=' *'
for i in range(0,n-3,1):
    contain_middle+=' '
contain_middle+=' *\n'

print(contain_middle*(n-2),contain)
