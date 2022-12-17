# Ingresar datos desde la terminal 
user = input('Username: \r\n')
print(f'ha introducido el usuario {user}')


passw = input('Introduzca su contraseña: \r\n')
password = 123456
# Las entradas de datos siempre son interpretadas como string, para trabajar con números se deben convertir a enteros.
passw = int(passw) # también se puede usar para convertir a float, string 

if passw != password:
    print(f'La contraseña es Incorrecta')
else: 
    print(f'Iniciando sesión...')