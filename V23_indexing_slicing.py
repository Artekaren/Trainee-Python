#Ejercicio23:
import numpy as np
secuencia = np.arange(10)
print(secuencia)
print(secuencia[3])

#slice:
#secuencia[inf:sup]
print(secuencia[1:8])
print(secuencia[3:])
print(secuencia[:7])

sub_secuencia = secuencia[5:9]
sub_secuencia[0] = 1234
print(sub_secuencia)
print(secuencia)
