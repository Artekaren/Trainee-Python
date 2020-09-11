#Desafio42: Generar una lista anidada que contenga los 6 autos.

#Primera forma: POCO ELEGANTE Y NO ESCALABLE
auto1 = ['Mazda RX4', 21.0, 6, False, 4]
auto2 = ['Merc 240D', 24.4, 4, True, 2]
auto3 = ['Merc 280', 19.2, 6, True, 4]
auto4 = ['Valiant', 18.1, 6, True, 1]
auto5 = ['Merc 450SL', 17.3, 8, False, 3]
auto6 = ['Toyota Corolla', 33.9, 4, True, 1]

import numpy as np
union=auto1+auto2+auto3+auto4+auto5+auto6
print(union)
union_np = np.array(union)
union_redim = union_np.reshape(6,5)
print(union_redim)

#Segunda forma:
import numpy as np
import pandas as pd

df_auto = pd.read_csv('auto.csv')
auto=df_auto.values.tolist()
print('-----------------------------------------------------------------------')
