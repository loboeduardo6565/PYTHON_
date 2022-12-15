def name(nombre):
    print(f'My name is {nombre}')

name('Charlotte')
name('Carlota')
name('Princesa')

def name(nombre, quien = 'talentosa'):
    print(f'Mi nombre es {nombre} y soy {quien}')

name('Charlotte', 'Hija de la Reina')
name('Carlota','maravillosa')
name('Carlota Lobo')


def informacion(nombre):
    return nombre

empleado = informacion('Charlotte')
print(empleado)