#listas 

listado = [ 1, 2, 3, ]
listado_alf = ['a' , 'b']
listado_nombres = ['Jiménez Juan' , 'Mateus María', 'Pérez Pepita']

print(listado_nombres[2])

print(f"el último elemento de la lista es {listado_nombres[-1]}")
#{} [] '

listado_nombres[0] = "jiménez Julian"

print(f"el primer nombre de la lista es {listado_nombres[0].split(', ')[-1]}")

#agregar elementos 

listado_nombres.append("jorge")
print(listado_nombres)

listado_nombres.append(28)
print(listado_nombres)

dos_nombres = ['Johan' , 'Gabriela']
listado_nombres.insert(2,"Teresa")
print(listado_nombres)

listado_nombres.extend(dos_nombres)
print(listado_nombres)

del listado_nombres[-4]
print(listado_nombres)

listado_nombres.remove(28)
print(listado_nombres)

#ordenar listas 

listado_nombres.sort()
print(listado_nombres)

listado_nombres.sort(reverse=True)
print(listado_nombres)

#encontrar la extensión de la lista 

print({len(listado_nombres)})