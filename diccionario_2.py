# Crear un diccionario sin valores
Amortiguador = {}

# Agregamos un valor
Amortiguador['Marca'] = 'Gabriel'
Amortiguador['Lado'] = 'Derecho'
Amortiguador['Precio'] = 50

print(Amortiguador)

#Iterar con for

for key, value in Amortiguador.items():
    print(key,value)

# Borrar un valor
# del Amortiguador['Marca']