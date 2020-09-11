#Desafío33: Transformando segundos a minutos
#Se tiene una lista con la cantidad de segundos que demoraron algunos procesos. Se necesita una función para trasformar todos los datos a minutos, (las fracciones de minutos serán ignoradas).
#_tip_: Por defecto Python 3 implementa una división que devuelve un flotante. Lo que necesitamos es la parte entera. Ocupe // para resolver este inconveniente.

def to_minutes(lista):
    results = []
    for i in lista:
        results.append(i // 60)
    return results

seconds = [100, 50, 1000, 5000, 1000, 500]
print(to_minutes(seconds))
