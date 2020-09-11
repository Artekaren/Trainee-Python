#Ejercicio21:

#1.- Dataframe

#Importar archivo csv
import pandas as pd
df = pd.read_csv('nations.csv')
print(df)
print('-----------------------------------------------------------------------')

#Entrega las dimensiones
print(df.shape)
print('-----------------------------------------------------------------------')

#Entrega por defecto 5 filas
print(df.head())
print('-----------------------------------------------------------------------')

#Entrega 3 filas
print(df.head(3))
print('-----------------------------------------------------------------------')

#drop: elimina columnas del DF
df_sin=df.drop(columns='Unnamed: 0')
print(df_sin)
print('-----------------------------------------------------------------------')


#2.- Series
print(df['region'])
print(type(df['region']))
print('-----------------------------------------------------------------------')

#frecuencia relativa de los valores de la Serie
print(df['region'].value_counts())
print('----------------------------------------------------------------------')

#promedio
print(df['region'].value_counts().mean())
print('-----------------------------------------------------------------------')

#Entrega un valor localizado dentro del Dataframe
print(df.loc[8,'life'])
print(type(df.loc[8,'life']))
print('-----------------------------------------------------------------------')

#Creación de un subset (sub dataframe)
#   : operador slice (desde-hasta)
df_subset = df.loc[:,['gdp','school','adfert','chldmort']]
print(type(df_subset))
print(df_subset.head())
print('-----------------------------------------------------------------------')

df_subset2 = df.loc[:,'gdp':'pop']
print(type(df_subset2))
print(df_subset2.head())
print('-----------------------------------------------------------------------')

#Otra forma de crear un subset (sub dataframe)
df_americas = df_sin[df_sin['region']=='Americas']
print(df_americas.head())
print(df_americas.shape)
print('-----------------------------------------------------------------------')

# el valor más alto del producto interno bruto
print(df_americas.gdp.max())
# a qué país corresponde éste?
print(df_americas[df_americas['gdp'] == df_americas['gdp'].max()]['country'])
print(type(df_americas[df_americas['gdp'] == df_americas['gdp'].max()]['country']))
print('-----------------------------------------------------------------------')

#Datos perdidos en una Serie
#Isnull entrega la cantidad de valores NaN existentes en la columna 'gdp'
print(df['gdp'].isnull().sum())

df_gdp_nan=df[df['gdp'].isnull()==True]
print(df_gdp_nan)
print('-----------------------------------------------------------------------')

#Formas de iteración en un Dataframe

#iteritems(): Recorre todos los elementos de un DataFrame por columna. Esto significa que se va a estar recorriendo todos los campos de una base de datos a la vez.
for colname,serie in df_sin.iteritems():
    print(colname)
    print(serie)
    break
print('-----------------------------------------------------------------------')

#Inspeccionemos si todos los datos corresponden al tipo numérico o no. Para ello, se hará uso de la siguiente función de pandas : pd.api.types.is_numeric_dtype .

for colname,serie in df_sin.iteritems():
    tmp = pd.api.types.is_numeric_dtype(serie)
    print("{} es {}".format(colname, tmp))
print('-----------------------------------------------------------------------')

#iterrrows(): Recorre todos los elementos de un DataFrame por fila. Esto significa que se va a estar recorriendo todas las columnas, por registro, de una base de datos a la vez.

for index,row_serie in df_sin.iterrows():
    print(index)
    print(row_serie)
    print(type(row_serie))
    break
print('-----------------------------------------------------------------------')

for index,row_serie in df_sin.iterrows():
    if index == 1:
        print(row_serie)
        print(type(row_serie))
print('-----------------------------------------------------------------------')
