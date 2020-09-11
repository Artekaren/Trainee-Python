#Ejercicio 3: Obtener la fecha y hora actuales en el sistema

import datetime
ahora=datetime.datetime.now()   
#primer datetime: de la importación, segundo datetime: objeto
print(ahora)

print(type(ahora))

#método strf
#Y mayúscula muestra los 4 dígitos del año
#y minúscula muestra solo 2 dígitos del año
print(ahora.strftime('%d/%m/%Y %H:%M:%S'))
