#Condicionales con elif 

tipo_cliente = 'Jubilado'

if tipo_cliente == 'asociado':
    print('Tienes 20% de descuento')
elif tipo_cliente == 'Estudiante':
    print('Tienes 10% de descuento')
elif tipo_cliente == 'Jubilado':
    print('Tienes 40% de descuento')
else:
    print('No existe descuento para este cliente')

# Operador and 

user_auth = True
user_admin = False

if user_auth and user_admin:
    print('El usuario tiene permisos de administrador')
elif user_auth:
    print('El usuario tiene acceso básico al sistema')
else:
    print('El usuario no ha iniciado sesión')