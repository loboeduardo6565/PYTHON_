import os #Permite importar una gran cantidad de funciones para manejar opciones de SO

DIRECTORIO = 'inventario/'  # Las mayusculas permiten definir una Constante. 
EXTENSION = '.txt'          # Se agrega la extensión del archivo1

#Creando la clase tipo constructor Repuesto
class Repuesto:
    def __init__(self, nombre, marca, categoria, aplicacion, precio):
        self.nombre = nombre
        self.categoria = categoria
        self.aplicacion = aplicacion
        self.marca = marca
        self.precio = precio

def app():

    crear_directorio()
    mostrar_opciones()

    consulta = True
    while consulta:
        opcion = input('Seleccione la opción que desee:')
        opcion = int(opcion)

        #Opciones
        if opcion == 1:
            agregar_repuesto()
            consulta = False
        elif opcion == 2:  
            editar_repuesto()
            consulta = False
        elif opcion == 3:  
            mostrar_inventario()
            consulta = False
        elif opcion == 4:  
            buscar_repuesto()
            consulta = False
        elif opcion == 5:  
            eliminar_repuesto()
            consulta = False
        else:
            print('La opción no es válida, intente de nuevo \r\n')


def eliminar_repuesto():
    nombre = input('Indique el nombre del repuesto que desea Eliminar: \r\n')

    try:
        
        print('Eliminando un Repuesto existente...')
    except expression as identifier:
        print('\r\n El repuesto indicado no existe...\r\n')
    
    # Reiniciando la app
    app()

    nombre = input('Indique el nombre del repuesto que desea buscar: \r\n')
    # Esta opción es la que usé, sin embargo abajo comentada hay otra opción que usa Juan Pablo De la torre Valdez en su curso Introducción a la programación con python. 
    existe = validar_repuesto(nombre)
    if existe:
        os.remove(DIRECTORIO + nombre + EXTENSION) 
            print('Eliminando un Repuesto existente...')
    else: 
        print('\r\n El repuesto indicado no existe...\r\n')
    app()  # Esto evita que la aplicación se cierre luego de no encontrar ningún repuesto. 

    

def buscar_repuesto():

    nombre = input('Indique el nombre del repuesto que desea buscar: \r\n')
    # Esta opción es la que usé, sin embargo abajo comentada hay otra opción que usa Juan Pablo De la torre Valdez en su curso Introducción a la programación con python. 
    existe = validar_repuesto(nombre)
    if existe:
        with open(DIRECTORIO + nombre + EXTENSION) as repuesto: 
            print('\r\n Información del Repuesto existente: \r\n')
            for linea in repuesto:
                print(linea.rstrip())
    else: 
        print('\r\n El repuesto indicado no existe...\r\n')
    app()  # Esto evita que la aplicación se cierre luego de no encontrar ningún repuesto. 

    ##-------------- Usando Try
    #try:
    #    with open(DIRECTORIO + nombre + EXTENSION) as repuesto: 
    #        print('\r\n Información del Repuesto existente: \r\n')
    #        for linea in repuesto:
    #            print(linea.rstrip())
    #except IOError:
    #    print('\r\n El repuesto indicado no existe...\r\n')
    ## Reiniciando la app
    #app()

# Mostrar los articulos que componen el inventario. 
def mostrar_inventario():
    listar = os.listdir(DIRECTORIO)
    listar_solo_txt = [i for i in listar if i.endswith(EXTENSION)] # Valida que solo se listen los archivos con extensión .txt 
    for objetos in listar_solo_txt:
        with open(DIRECTORIO + objetos) as repuestos:
            for linea in repuestos:
                # Muestra el contenido 
                print(linea.rstrip())
            print('------------------ \r\n')
    print('Listando el Inventario...')


# Actualizar los datos de un repuesto existente
def editar_repuesto():
    nombre_exist_repuesto = input('Ingrese el nombre del Repuesto a editar: \r\n')

    # existe = os.path.isfile(DIRECTORIO + nombre_exist_repuesto + EXTENSION) Lo podemos validar de esta forma o a través de una función. 
    
    existe = validar_repuesto(nombre_exist_repuesto)
    if existe:
        with open(DIRECTORIO + nombre_exist_repuesto + EXTENSION, 'w') as archivo:    # el simbolo "+" permite concatenar parametros

            nombre_repuesto = input('Ingrese el nuevo nombre: \r\n')
            categoria_repuesto = input('Ingrese la categoría del Repuesto: \r\n')
            aplicacion_repuesto = input('Ingrese la aplicación del Repuesto: \r\n')
            marca_repuesto = input('Ingrese la marca del Repuesto: \r\n')
            precio_repuesto = input('Ingrese el precio del Repuesto: \r\n')

            repuesto = Repuesto(nombre_repuesto, categoria_repuesto, aplicacion_repuesto, marca_repuesto, precio_repuesto)

            # Reescribir los nuevos datos en el archivo
            archivo.write('Nombre: ' + repuesto.nombre + '\r\n')
            archivo.write('Categoría: ' + repuesto.categoria + '\r\n')
            archivo.write('Aplicación: ' + repuesto.aplicacion + '\r\n')
            archivo.write('Marca: ' + repuesto.marca + '\r\n')
            archivo.write('Precio: ' + repuesto.precio + '\r\n')

            # Renombrando el archivo
            archivo.close() # Se debe cerrar el archivo antes de renombrarlo
            os.rename(DIRECTORIO + nombre_exist_repuesto + EXTENSION, DIRECTORIO + nombre_repuesto + EXTENSION)

            print('Editando un Repuesto existente...')
    else:
        print('El repuesto indicado no existe...')
    app()  # Esto evita que la aplicación se cierre luego de no encontrar ningún repuesto. 
# Agregar los datos de un nuevo repuesto 
def agregar_repuesto():
    nombre_repuesto = input('Ingrese el nombre del Repuesto: \r\n')

    # Validar si el archivo a crear ya existe en base al nombre
    existe = validar_repuesto(nombre_repuesto)
    if not existe:

        with open(DIRECTORIO + nombre_repuesto + EXTENSION, 'w') as archivo:    # el simbolo "+" permite concatenar parametros

            #Se agregan los campos categoria, aplicacion y precio
            categoria_repuesto = input('Ingrese la categoría del Repuesto: \r\n')
            aplicacion_repuesto = input('Ingrese la aplicación del Repuesto: \r\n')
            marca_repuesto = input('Ingrese la marca del Repuesto: \r\n')
            precio_repuesto = input('Ingrese el precio del Repuesto: \r\n')
            

            #Se instancia la clase constructora
            repuesto = Repuesto(nombre_repuesto, categoria_repuesto, aplicacion_repuesto, marca_repuesto, precio_repuesto)

            archivo.write('Nombre: ' + repuesto.nombre + '\r\n')
            archivo.write('Categoría: ' + repuesto.categoria + '\r\n')
            archivo.write('Aplicación: ' + repuesto.aplicacion + '\r\n')
            archivo.write('Marca: ' + repuesto.marca + '\r\n')
            archivo.write('Precio: ' + repuesto.precio + '\r\n')
            print('Agregando un nuevo repuesto...')
    else:
        print('El nombre de repuesto indicado ya existe, intente con otro nombre \r\n')
    
    app()

def mostrar_opciones():
    print('Seleccione la opción que desee: \r\n')
    print('1) Agregar un nuevo Repuesto')
    print('2) Editar un Repuesto existente')
    print('3) Visualizar el Inventario')
    print('4) Buscar un Repuesto existente')
    print('5) Eliminar un Repuesto existente \r\n')

def crear_directorio():
    if not os.path.exists(DIRECTORIO):
        # Crea un directorio
        os.makedirs(DIRECTORIO)
    #else:
    #    print('El directorio ya existe')

# Función de validación de existencia 
def validar_repuesto(nombre):
    return  os.path.isfile(DIRECTORIO + nombre + EXTENSION)

app()