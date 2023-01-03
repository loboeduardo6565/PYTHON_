inventario = {} # Se crea un diccionario vacío 
inventario['repuestos'] = [] # Se crea una lista vacía de repuestos

# Función secundaria: Agregar un nuevo repuesto
def agregar_repuesto():
    #print('Agregar Repuesto...') Esto era para probar el llamado a la función 
    
agregar_repuesto()

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

app ()

