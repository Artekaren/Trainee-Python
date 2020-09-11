#Ejercicio23:
import numpy as np
nombres = np.array(['sebastian','pedro','maria','fernanda'])
notas = np.array([[5,5,6],[6,6,7],[7,7,6],[5,4,6]])

print('pedro' in nombres)
print(nombres == 'pedro')
print(notas[nombres == 'pedro'])

print(notas[np.array([False, True, False, False])])
print(notas[~(nombres == 'pedro')])
