# Ingresar datos desde la terminal 
q1 = input('3 + 2 es igual a 5: \r\n')
puntos = 0
puntos = int(puntos)

if q1.upper() == 'SI':
    print(f'La respuesta es correcta')
    puntos=1
elif q1.upper() == 'NO': 
    print(f'La respuesta es incorrecta')
    puntos=0
else:
    print(f'Se debe responder con SI O NO')


q2 = input('3 * 2 es igual a 6: \r\n')

if q2.upper() == 'SI':
    print(f'La respuesta es correcta')
    puntos = puntos + 1
elif q2.upper() == 'NO': 
    print(f'La respuesta es incorrecta')
    puntos = puntos
else:
    print(f'Se debe responder con SI O NO')


q3 = input('3 - 2 es igual a 1: \r\n')

if q3.upper() == 'SI':
    print(f'La respuesta es correcta')
    puntos = puntos + 1
elif q3.upper() == 'NO': 
    print(f'La respuesta es incorrecta')
    puntos = puntos
else:
    print(f'Se debe responder con SI O NO')

print(f'El puntaje alcanzado es {puntos}')