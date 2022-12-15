meses = ["Enero", "Febrero", "marzo"];
print (meses[0])

#Los arrays comienzan en la posición 0
lenguajes = ["Python", "Java", "JS", "Kotlin"];
print(lenguajes)
print(lenguajes[0])

#Si deseas acceder a un string con una variable hay que agregar la letra f, por ejemplo al acceder a un elemento dentro del arreglo y sumarlo a un texto
learn= f'Estoy aprendiendo {lenguajes[3]}'
print(learn)

#modificando un valor de un arreglo
lenguajes [2]= 'PHP'
print(lenguajes)

#Agregar un valor de un arreglo a través de un metodo
lenguajes.append('Ruby')
lenguajes.append('Kotlin')
print(lenguajes)

#Eliminar un valor de un arreglo a través de un metodo
del lenguajes[2]
print(lenguajes)

#Eliminar el ultimo elemento de un arreglo a través de un metodo
lenguajes.pop
print(lenguajes)

#Eliminar un elemento especifico de un arreglo a través de un metodo
lenguajes.pop(0)
print(lenguajes)

#Eliminar un elemento de un arreglo a través de un metodo desde el nombre
lenguajes.remove('Kotlin')
print(lenguajes)    