#Desafio35: Iteración de claves y valor: Tenemos un listado de países y la cantidad de usuarios por cada país en la siguiente tabla: Requerimientos:
#Mostrar solo los países
#Mostrar solo los países con más de 60 usuarios

usuarios_por_pais = {
'México': 65,
'Chile': 50,
'Argentina': 55,
}

# Mostrar solo los países
for pais in usuarios_por_pais:
    print(pais)

# Mostrar solo los países con más de 60 usuarios
for pais,usuarios in usuarios_por_pais.items():
    if usuarios > 60:
        print(pais)
