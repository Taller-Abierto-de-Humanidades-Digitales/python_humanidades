## APUNTES LISTAS

# como crear listas

listado_ent = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
listado_alfa = ["a", "b", "c", "d", "e"]
listado_ent_alf = [1, "a", 3, "b", 15, "pepe"]

listado_nombres = ['Juan', 'Alvarez, Eduardo', 'Mafe', 'Lili']

# # para imprimir un elemento de una lista

# print(listado_nombres[0])

# # imprimir una parte de un elemento de la cadena

# print(listado_nombres[0][-2:])

# # partir un elemento de la lista en un caracter especifico
# # con split se crea una nueva lista

# print(f"El nombre y apellido del segundo elemento de la cadena es {listado_nombres[1].split(', ')}")
# print(f"El nombre del segundo elemento de la cadena es {listado_nombres[1].split(', ')[-1]}")

# Modificar elementos de la lista

listado_nombres[0] = 'Perez, Angélica'

# print(f"El primer nombre de la lista es: {listado_nombres[0]}")

# agregar nuevos elementos a la lista

listado_nombres.append("Ramirez, Carlos")

# print(f"El último nombre de la lista es: {listado_nombres[-1]}")

nuevo_nombre = "Romei, Bernabe"

listado_nombres.append(nuevo_nombre)

# print(f"El último nombre de la lista es: {listado_nombres[-1]}")

# Añadir en un lugar puntual de la lista

listado_nombres.insert(2,"Teresa")

# print(listado_nombres)

# agregar más de un elemento a la vez

nuevas_personas = ["Iguaran, Arnoldo", "Herrera, Chontico"]

listado_nombres.extend(nuevas_personas)

# print(listado_nombres)

# Eliminar un elemento de las lista de una posición

del listado_nombres[-3]

# print(listado_nombres)

# # Selecciona el último elemento
# print(listado_nombres.pop())

# # Eliminar uno de los elementos

# listado_nombres.remove("lili")
# print(listado_nombres)

# Ordenar alfabeticamente

listado_nombres.sort()
print(listado_nombres)
listado_nombres.sort(reverse=True)
print(listado_nombres)

