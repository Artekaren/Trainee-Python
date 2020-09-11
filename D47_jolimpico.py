#Desafio47: Por parte de la organización de los Juegos Olímpicos, se nos ha solicitado realizar un análisis de todos los competidores a lo largo de las olimpiadas. Para lograr este análisis, se requiere:









import pandas as pd
df_jolim = pd.read_csv('athlete_events.csv')

#1. Importar la base de datos athlete_events.csv, y reportar la cantidad de registros (filas) y de campos (columnas). El resultado debe guardarse en una variable llamada ejercicio_1 . tip: Puede hacer uso de .shape para esto.
ejercicio_1 = df_jolim.shape

#2. Reportar cuántas competencias se han realizado a lo largo del tiempo. El resultado debe ser un número entero y debe guardarse en una variable llamada ejercicio_2.
ejercicio_2 = df_jolim['Event'].value_counts()
#print(df_jolim['Season'].value_counts())

#3. Reportar el porcentaje (número entre 0 y 1) de atletas que participaron tanto en los juegos olímpicos de Verano como en los de Invierno. El resultado debe guardarse en una variable llamada ejercicio_3 .
ejercicio_3 = df_jolim['Season'].value_counts(normalize=True)*100    #With normalize set to True, returns the relative frequency by dividing all values by the sum of values.

#4. Informar dónde fue la primera celebración de un Juego Olímpico de Verano. El resultado debe guardarse en una variable llamada ejercicio_4 .
df_jolim_fil = df_jolim[df_jolim['Season'] == 'Summer']
df_jolim_fil['Year'].min()
aux = df_jolim_fil[df_jolim_fil['Year'] == df_jolim_fil['Year'].min()]['City']
ejercicio_4 = aux.head(1)

#5. Informar dónde fue la primera celebración de un Juego Olímpico de Invierno. El resultado debe guardarse en una variable llamada ejercicio_5 .
df_jolim_fil_2 = df_jolim[df_jolim['Season'] == 'Winter']
df_jolim_fil_2['Year'].min()
aux_2 = df_jolim_fil_2[df_jolim_fil_2['Year'] == df_jolim_fil_2['Year'].min()]['City']
ejercicio_5 = aux_2.head(1)

#6. Reportar los 10 primeros países con mayor cantidad de atletas participantes a lo largo de los juegos. El resultado debe guardarse en una variable llamada ejercicio_6.
aux_3 = df_jolim.groupby(['NOC']).size().reset_index(name = 'cantidad')
aux_4 = aux_3.sort_values(['cantidad'], ascending=False)
ejercicio_6 = aux_4.head(10)

#7. Reportar el porcentaje de medallas asignadas (oro, bronce, plata). El resultado debe guardarse en una variable llamada ejercicio_7.
aux_5 = df_jolim.groupby(['Medal']).size().reset_index(name = 'cantidadmedallas')
#print(aux_5)   #Muestra la cantidad de medallas por tipo
ejercicio_7 = df_jolim['Medal'].value_counts(normalize=True)*100

#8. Reportar cuáles fueron los países participantes en las primeras olimpiadas de verano. El resultado debe guardarse en una variable llamada ejercicio_8
aux_6 = df_jolim[df_jolim['Year'] == 1896]
ejercicio_8 = len(aux_6.groupby(['NOC']))

#Cuenta la razón de NAN en un dataframe
#na_ratio = ((aux_5.sum() / len(aux_5)*100).sort_values(ascending = False)
#print(na_ratio)
