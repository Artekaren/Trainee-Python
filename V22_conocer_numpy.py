#Ejercicio22:

#Ejemplo1:
import numpy as np
numpy_array = np.array([2,4,12])
print(type(numpy_array))
multiplicados_array_1 = numpy_array *3
print(multiplicados_array_1)

#Supongamos que no ocupamos numpy
array=[2,4,12]
multiplicados_array_2 = array *3
print(multiplicados_array_2)

#Conclusión: Numpy hace multiplicación vectorizada

print(multiplicados_array_1.shape)
print(multiplicados_array_1.dtype)


#Ejemplo2:
#Generamos un array de 100 observaciones con `np.arange`
n_sims = 100
demo_array = np.arange(n_sims)
demo_list = list(range(n_sims))
demo_list_2 = [x*2 for x in demo_list]
print(demo_list_2)
