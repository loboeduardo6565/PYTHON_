#Get y Set para editar atributos en modo PRIVATE
#
class Repuestos:

    def __init__(self,nombre,marca,precio):       
        self.nombre = nombre
        self.marca = marca
        self.__precio = precio      # Los atributos por lo general vienen por defecto en modo PUBLIC esto permite modificar su valor en cualquier parte del código
                                    # Para pasarlo a modo PROTECTED le agregamos un underscore, esto permite modificar su valor unicamente para la clase donde existe el atributo
                                    # Para cambiarlo a modo PRIVATE se debe agregar dos underscore al atributo y solo puede modificarse a través de un metodo "get y set"
    def mostrar_inventario(self):
        print(f'Nombre: {self.nombre}, Marca: {self.marca}, Precio: {self.__precio}')

    # Get permite obtener un valor, y Set permite agregar un valor
    def get_precio(self):
        return self.__precio # Se puede usar en vez de print la opción return para mostrar el valor del atributo. 
        #print(self.__precio)

    def get_precio_alt(self):
        print(self.__precio)

    def set_precio(self,precio):
        self.__precio = precio

#Instanciar una clase
amortiguadores = Repuestos('Amortiguador Delantero', 'Gabriel', 50) 
amortiguadores.mostrar_inventario()
amortiguadores.set_precio(60)
precio = amortiguadores.get_precio() # Se hace el get del valor desde el metodo ya que se está usando la opción return
print(precio)

#Segundo objeto de la clase repuestos
alternador = Repuestos('Alternardor Aveo', 'Monroe', 100)
alternador.mostrar_inventario()
alternador.set_precio(110)
alternador.get_precio_alt()

