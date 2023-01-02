#opcion = str(input('3 + 2 es igual a 5: \r\n'))
#while (opcion.upper() != 'SI') or (opcion.upper() != 'NO'):
#    if (opcion.upper() != 'SI') or (opcion.upper() != 'NO'):
#        print("¡Se debe responder con SI O NO! Inténtelo de nuevo")
#        #opcion = str(input('3 + 2 es igual a 5: \r\n'))
#    elif opcion.upper() == 'SI':
#            print(f'¡Correcto!')
#            puntos=1
#    elif opcion.upper() == 'NO': 
#            print(f'¡La respuesta es incorrecta!')
#            puntos=0
#print("Gracias por su colaboración")

numero = int(input("Escriba un número positivo: "))
while numero < 0:
    print("¡Ha escrito un número negativo! Inténtelo de nuevo")
    numero = int(input("Escriba un número positivo: "))
print("Gracias por su colaboración")