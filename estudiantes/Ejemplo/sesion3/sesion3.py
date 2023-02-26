"""
Apuntes para trabajar con listas
"""

# Crear una lista

listado = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
listado_alf = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
listado_mez = [1, 'a', 2, 'b', 3, 'c', 4, 'd', 5, 'e']

lista_nombres = ['Jiménez, Juan', 'Pedro', 'Maria', 'Luisa', 'Jose', 'Ana', 'Luis', 'Rosa', 'Marta', 'Pablo']

# Acceder a los elementos de una lista

#print(f"El primer nombre de la lista es {lista_nombres[0][-4:]}")
print(f"El primer nombre de la lista es {lista_nombres[0].split(', ')[-1]}")
print(f"El último nombre de la lista es {lista_nombres[-1].lower()}")
print(f"El tercer nombre de la lista es {lista_nombres[2].capitalize()}")

# Modificar la lista

lista_nombres[0] = "Jiménez, Julián"
lista_nombres[-1] = "Linda"
lista_nombres[2] = "Benito"

print(f"El primer nombre de la lista es {lista_nombres[0].split(', ')[-1]}")
print(f"El último nombre de la lista es {lista_nombres[-1].lower()}")
print(f"El tercer nombre de la lista es {lista_nombres[2].capitalize()}")

# Añadir elementos

lista_nombres.append("Jorge")

#print(lista_nombres)

nuevo_nombre = "Paul"

lista_nombres.append(nuevo_nombre)

#print(lista_nombres[-1])

dos_nombres = ["Clara", "Keila"]

lista_nombres.append(dos_nombres)

#print(lista_nombres)

lista_nombres.append(28)

#print(lista_nombres)

# añadir a cualquier lugar de la lista

lista_nombres.insert(2, "Teresa")

# print(lista_nombres)

lista_nombres.extend(dos_nombres)

del lista_nombres[-4]

print(lista_nombres)

lista_nombres_sin_ultimo = lista_nombres.pop()
print(lista_nombres)
print(lista_nombres_sin_ultimo)

lista_nombres.remove(28)
print(lista_nombres)

# Ordenar listas

lista_nombres.sort()
print(lista_nombres)

lista_nombres.sort(reverse=True)
print(lista_nombres)

# encontrar la extensión de la lista

print(f"Este listado contiene {len(lista_nombres)} elementos.")








