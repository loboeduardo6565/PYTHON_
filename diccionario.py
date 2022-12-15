# Diccionarios - creando un diccionario

Filtros = {
    'Marca' : 'Millar',      # llave - valor
    'Modelo' : 'MK15728',    # llave - valor
    'Tipo' : 'Aire',         # llave - valor
    'Aplicacion' : 'Ford',   # llave - valor
    'Precio' : 8
}

# Acceder a los elementos
print(Filtros['Modelo'])
costo = Filtros['Precio']
print(f' El precio es {costo} u$s')

# Para agregar más caracteristicas 
Filtros['Precio_oferta'] = '6'

print(Filtros['Precio_oferta'])
print(Filtros)

# Borrar una clave
del Filtros['Precio_oferta']


