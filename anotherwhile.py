q1 = input('3 + 2 es igual a 5: \r\n')

if q1.upper() == 'SI':
        print(f'¡Correcto!')
        puntos=1
elif q1.upper() == 'NO': 
        print(f'¡La respuesta es incorrecta!')
        puntos=0
else:
    while (q1.upper() != 'SI') or (q1.upper() != 'NO'):
        print(f'Se debe responder con SI O NO')
        q1 = input('3 + 2 es igual a 5: \r\n')

        if q1.upper() == 'SI':
            print(f'¡Correcto!')
            puntos=1
            break;
        elif q1.upper() == 'NO': 
            print(f'¡La respuesta es incorrecta!')
            puntos=0
            break;