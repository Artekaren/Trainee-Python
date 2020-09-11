#Desafio48: Del comité de Juegos Olímpicos le sugieren la existencia de sesgos en la participación de los países. Para ello, se le solicita lo siguiente:

import pandas as pd
import numpy as np

#1 Crear 4 nuevos subsets de datos, donde cada uno contenga, respectivamente, a los atletas que ganaron Oro, Plata, Bronce y aquellos que no ganaron medallas.
df_jolim = pd.read_csv('athlete_events.csv')
bronce = df_jolim[df_jolim['Medal'] == 'Bronze']
oro = df_jolim[df_jolim['Medal'] == 'Gold']
plata = df_jolim[df_jolim['Medal'] == 'Silver']
no_ganaron = df_jolim[df_jolim['Medal'].isnull()]

#2 Generar una nueva columna de nombre 'Female' para cada una de los subsets creados. En esta nueva columna, se debe asignar 1 a las filas correspondientes a una mujer, y 0 a las correspondientes a un hombre.
"""
bronce['female'] = np.where(bronce['Sex']=='F', '1', '0')
oro['female'] = np.where(oro['Sex']=='F', '1', '0')
plata['female'] = np.where(plata['Sex']=='F', '1', '0')
no_ganaron['female'] = np.where(no_ganaron['Sex']=='F', '1', '0')
"""
#3 Reportar los 10 primeros países con mayor cantidad de participantes para cada una de los subsets creados.
aux_1 = no_ganaron.groupby(['NOC']).size().reset_index(name = 'cantidad')
aux_2 = aux_1.sort_values(['cantidad'], ascending=False)
ejercicio_3 = aux_2.head(10)
print(ejercicio_3)

#4 Reportar la cantidad de mujeres y hombres en cada uno de los subsets.
ejercicio_4 = bronce['Sex'].value_counts()

#5. Generar una función que permita reportar las medias entre hombres y mujeres de una columna.
def reportar(df,analyze,gender):
    if gender == 'F':
        aux_3 = df[df['Sex'] == gender]
        aux_4 = aux_3[analyze].mean()
        print(aux_4)
    else:
        aux_5 = df[df['Sex'] == 'M']
        aux_6 = aux_5[analyze].mean()
        print(aux_6)

#6. Aplicar la función del ejercicio 5 en los cuatro subsets creados.
#7. Reportar las medias de 'Height' y 'Weight' .
reportar(bronce,'Height','M')
