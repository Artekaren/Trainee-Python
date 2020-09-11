#Ejemplo27:
import numpy as np
array_funciones = np.array([4,9,16,25])
#sqrt
print(np.sqrt(array_funciones))


#Operador terniario
#np.where(una condicion,se cumple,no se cumple)
notas = np.array([4.5,6.6,7.0,2.0,3.6,4.6,5.6,5.8,2.5])
notas_bin = np.where(notas>=notas.mean(),1,0)
print(notas_bin)
print(notas.mean())


#Otro ejemplo de operador terniario:
altura_gatas = [3.60, 2.35, 2.97,
3.79, 2.37, 2.56,3.49, 3.38, 4.70, 1.82]
altura_gatos = [4.20, 4.14, 3.41, 4.24, 4.96, 3.80,
2.23, 2.69, 1.02, 4.67]
tabby = [True, False, False, True, False,
True , True, False, False, False]

gatos_grandes = np.where(altura_gatos > np.mean(altura_gatos),
True, False)
print(gatos_grandes)

gatas_pequenas_tabby = np.where(
(altura_gatas < np.mean(altura_gatas)) & (tabby == True),True,False)
print(gatas_pequenas_tabby)
