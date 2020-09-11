#Desafío23: if-else
#El usuario debe ingresar un password en la plataforma. Si el password tiene menos de 6 letras, se debe mostrar un aviso. Si el password es 12345, se debe informar que el password es incorrecto.

password=input('Ingrese su password:  ')
num=int(password)

if(len(password)<6):
    print('password incorrecto')
elif(num==123456):
    print('password incorrecto')
else:
    print('password correcta')

#Desafío while
#Mismo enunciado

clave='hoja'
password =input('Ingrese el password:  ')
while (password!=clave):
    print('password incorrecta')
    password =input('Ingrese el password:  ')
print('password correcto')
