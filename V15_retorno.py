#Ejercicio15: Ejemplo de retorno

#Definamos la función:
def transformar_a_fahrenheit(f):
    celsius = (f + 40) / 1.8 - 40
    return celsius


#De esta forma, si se desea mostrar el resultado de la función transformar_a_fahrenheit , se debe envolver la función en un print() :
print(transformar_a_fahrenheit(110))


#También se puede guardar el valor de una función en una variable
grados_celsius=transformar_a_fahrenheit(110)
print('La variable grados_celsius es del tipo: ', type(grados_celsius))
print(grados_celsius)


#También es posible realizar operaciones con el retorno de esta función. Supongamos que se desea corregir el cálculo al incrementar en 10:
print(grados_celsius+10)


#Importante: Todo lo que viene después de la instrucción return es ignorado.
