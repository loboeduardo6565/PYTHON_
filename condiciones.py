saldo = 500

if saldo >0:
    print("Puedes pagar")

# Revisar si una condición es mayor a 
balance = 0 
if balance > 0:
    print ('Posee saldo positivo')
else:
    print ('No posee saldo positivo')

# Sumar likes 
likes = 200
if likes == 200:
    print(f'Tienes {likes} likes')

# Sumar likes 
likes = 200
if likes >= 200:
    print(f'Tienes {likes} likes')

# If con string 
lenguajes = 'sas'
if lenguajes == 'sas':
    print(f'Debes aprender lenguaje {lenguajes}')

# If con string negativo
lenguajes = 'python'
if not lenguajes == 'sas':
    print(f'El lenguaje es {lenguajes}')
else:
    print(f'El lenguaje es {lenguajes}')

# Evaluar un Boolean
#sing_on = True
sing_on = False

if sing_on:
    print('Accediendo al sistema')
else:
    print('Debes iniciar sesión')

# Evaluar si un elemento existe o no en una lista
lenguajes = ["Python", "Java", "JS", "Kotlin", "SAS", "Bash"];
name='SAS'
if name in lenguajes:
    print(f'{name} está en la lista')
else: 
    print(f'{name} no está en la lista')

#IF anidados
user_auth = False
user_admin = False

if user_auth:
    if user_admin:
        print('El usuario tiene permisos de administrador')
    else:
        print('El usuario tiene acceso básico al sistema')
else:
    print('El usuario no ha iniciado sesión')

