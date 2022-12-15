# Evaluar si un elemento existe o no en una lista usando un for y un if

repuesto = 'Bobina'
repuestos = ["Amortiguadores", "Bobina", "Collarin", "Diodera", "Empacadura", "Filtro"];

for item in repuestos:
    if item == repuesto:
        print(f'{repuesto} está en el inventario')
    else: 
        print(f'{item} no está en el inventario')