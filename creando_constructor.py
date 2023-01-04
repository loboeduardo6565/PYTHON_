#El constructor es una función que se ejecuta automaticamente al crear un nuevo objeto por medio de una clase
#Los constructores se definen con doble underscore
class Repuestos:

    def __init__(self,nombre,marca,precio):       
        self.nombre = nombre
        self.marca = marca
        self.precio = precio

    def mostrar_inventario(self):
        print(f'Nombre: {self.nombre}, Marca: {self.marca}, Precio: {self.precio}')


#Instanciar una clase
amortiguadores = Repuestos('Amortiguador Delantero', 'Gabriel', 50) 
amortiguadores.mostrar_inventario()

#Segundo objeto de la clase repuestos
alternador = Repuestos('Alternardor Aveo', 'Monroe', 100)
alternador.mostrar_inventario()

