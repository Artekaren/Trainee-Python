#Desafío49 - El caso de Chile

import pandas as pd

df_jolim = pd.read_csv('athlete_events.csv')

#1. Generar un nuevo subset a partir del DataFrame original, que almacene todas las observaciones correspondientes a Chile.
aux_1 = df_jolim[df_jolim['NOC'] == 'CHI']

#2. Utilizando el subset generado, reportar la cantidad de atletas chilenos registrados en cada año, y en qué año hubo la participación más alta.
aux_2 = aux_1.groupby(['Year']).size().reset_index(name = 'cantidadatletas')
aux_3 = aux_2[aux_2['cantidadatletas'] == aux_2['cantidadatletas'].max()]['Year']

#3. Reportar los nombres de todos los ganadores de alguna medalla.
ganaron = aux_1[aux_1['Medal'].notnull()]

#4. Reportar en qué año Chile obtuvo más medallas.
aux_4 = ganaron.groupby(['Year']).size().reset_index(name = 'cantidadmedallas')
aux_5 = aux_4[aux_4['cantidadmedallas'] == aux_4['cantidadmedallas'].max()]['Year']
