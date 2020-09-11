#Desafío51 - API
#Para este desafío, se debe usar la API de pruebas de reqres , disponible en https://reqres.in/. Esta API no requiere autenticación, y su único recurso es users. Todas las solicitudes se hacen a https://reqres.in/api/users. Puede utilizar el código entregado por Postman. Se considerará para la evaluación que las respuestas de la API sean exitosas.

#Desafío 1 Crear el programa fake_request.py , que contenga la función request . Esta función debe: Recibir como parámetro obligatorio un method , que será el verbo a utilizar en la request. Recibir como parámetro obligatorio una url, que será la url a usar en la request. Recibir como parámetro opcional un payload (por defecto string vacío), que será la data a utilizar en la request. La función debe realizar una solicitud a la api con la URL, el verbo, y el payload indicado, y retornar la respuesta obtenida: Para los casos de GET, POST y PUT, la respuesta exitosa entrega un json y un código. En estos casos, debe retornar el json como diccionario de Python. Para el caso de DELETE, la respuesta exitosa solo entrega el código de respuesta. En este caso, debe retornar el código de respuesta.

#Desafío 2 Utilice la función del ejercicio 1 para listar los usuarios, e imprima el retorno en pantalla.

#Desafío 3 Utilice la función del Ejercicio 1 para crear un usuario, e imprima el retorno en pantalla.

#Desafío 4 Utilice la función del ejercicio 1 para actualizar un usuario, e imprima el retorno en pantalla

#Desafío 5 Utilice la función del ejercicio 1 para eliminar un usuario, e imprima el retorno en pantalla
