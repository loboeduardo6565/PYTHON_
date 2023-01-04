class Repuestos: #Los nombres de clases deben comenzar con mayusculas

    def agregar_repuestos(self,nombre):     #Las funciones definidas dentro de una clase se denominan metodos - se agrega el parametro self para enviarle un parametro al metodo
        self.nombre = nombre # Atributo     # Self es una forma de referirse al objeto que se está ejecutando
    
    def mostrar_inventario(self):
        print(f'Nombre: {self.nombre}')

#Instanciar una clase
amortiguadores = Repuestos() #El objeto está en minúscula para que no se confunda con el nombre de la clase
amortiguadores.agregar_repuestos('Amortiguador Delantero') #Invocar una función o "Metodo"
amortiguadores.mostrar_inventario() #Invocar una función o "Metodo"

#Segundo objeto de la clase repuestos
alternador = Repuestos() #El objeto está en minúscula para que no se confunda con el nombre de la clase
alternador.agregar_repuestos('Alternardor Aveo') #Invocar una función o "Metodo"
alternador.mostrar_inventario() #Invocar una función o "Metodo"

#Tambien podemos mostrar los objetos de otra forma no necesariamente desde un metodo. 
print(f'Nombre del Repuesto: {amortiguadores.nombre}')
print(f'Nombre del Repuesto: {alternador.nombre}')