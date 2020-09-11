#Ejercicio30:

#Caso1: Convertir un diccionario en una lista con la función items()

list({"k1": 5, "k2": 7}.items())

#Caso2: Convertir una lista en diccionario con la función dict()
dict([('k1', 5), ('k2', 7)])

#Caso3: Cruzando información de dos listas. 2 formas.
nombres = ['Alumno1', 'Alumno2', 'Alumno3']
notas = [10, 3, 8]

#1 Forma1: Iterar las listas simultáneamente, con un índice.

notas_por_alumno = {}
for i in range(len(nombres)):
    alumno = nombres[i]
    nota = notas[i]
    notas_por_alumno[alumno] = nota
print(notas_por_alumno)

#2 Forma2: Utilizando el método zip
notas_por_alumno = dict(zip(nombres, notas))
print(notas_por_alumno)
