inventario = {} # Se crea un diccionario vacío 
inventario['repuestos'] = [] # Se crea una lista vacía de repuestos


# Función principal: Agregar nueva categoría
def app():

    #Agregar categoría bandera/flag
    agregar_categoria = True
    while agregar_categoria:
        nombre_categoria = input('¿Cómo deseas llamar a esta categoría de repuestos?')

        if nombre_categoria:
            inventario['nombre'] = nombre_categoria
            
            # Desactivamos el while al ingresar un nombre de categoría
            agregar_categoria = False
            print(inventario)

            # Invocamos la función para agregar los repuestos
            agregar_repuesto()

# Función secundaria: Agregar un nuevo repuesto
def agregar_repuesto():
    #print('Agregar Repuesto...') Esto era para probar el llamado a la función 
    add_repuesto = True # bandera/flag
    while add_repuesto:
        # Preguntar el nombre del repuesto que deseas agregar
        nombre_categoria = inventario['nombre']
        consulta = f'\r\n¿Cómo se llama el repuesto que deseas agregar en la categoría {nombre_categoria}: \r\n'
        consulta += 'Escribe "X" para dejar de agregar repuestos \r\n'
        repuesto = input(consulta)

        if repuesto == 'X':
            #Dejar de agregar repuestos
            print('Saliendo...')
            add_repuesto = False
            mostrar_inventario()
        else:
            inventario['repuestos'].append(repuesto)
            #print(playlist)
            mostrar_inventario()


def mostrar_inventario():
    nombre_categoria = inventario['nombre'] # para esta definición así como para la anterior debo extraer el valor del nombre de la categoría
    print(f'Inventario: {nombre_categoria} \r\n')
    print('Repuestos:\r\n')
    for repuesto in inventario['repuestos']:
        print(repuesto)          


app ()

