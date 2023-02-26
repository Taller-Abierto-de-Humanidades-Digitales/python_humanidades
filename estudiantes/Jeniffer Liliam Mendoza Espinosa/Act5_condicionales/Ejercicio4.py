#Ejercicio 4: Inventario de libros por categoría

libros = ['Vallejo, Irene; El infinito en un junco; 2021; Ensayo', 'de Saint-Exupery, Antoine; El Principito; 1943; Novela', 'Dostoiewski, Fedor; Pobres gentes; 1846; Novela', 'Mistral, Gabriela; Sonetos de la muerte; 1915; Poesía', 'García, Luis; I took Panama; 1973; Teatro', 'Bonnet, Piedad; Explicaciones no pedidas; 2011; Poesía', 'Restrepo, Laura; Hot sur; 2012; Novela', 'Abad, Héctor; El olvido que seremos; 2006; Novela', 'Malcom, Janet; El periodista y el asesino; 1989; Crónica', 'Caparrós, Martín; El hambre; 2014; Crónica', 'Walsh, Rodolfo; Operación masacre; 1987; Novela']

categoria_ficcion = 'Ficción'
categoria_no_ficcion = 'No ficción'
otras_categorias = 'Otras categorías'

lista_libros = []
for libro in libros:
    libro = libro.split("; ")
    lista_libros.append(libro)
#print(lista_libros)

lista_libros[0].append('No ficción')
lista_libros[7].append('No ficción')
lista_libros[8].append('No ficción')
lista_libros[9].append('No ficción')
lista_libros[10].append('No ficción')
lista_libros[1].append('Ficción')
lista_libros[2].append('Ficción')
lista_libros[6].append('Ficción')
lista_libros[3].append('Otras categorías')
lista_libros[4].append('Otras categorías')
lista_libros[5].append('Otras categorías')
#print(*lista_libros, sep="\n")

libros_ficcion = []
libros_no_ficcion = []
libros_otros = []

#NO FICCIÓN
for lista_libro in lista_libros:
    if lista_libro[-1] == 'No ficción':
        libros_no_ficcion.append(lista_libro)
     
lista_no_ficcion = []
for libro_no_ficcion in libros_no_ficcion:
    lista_no_ficcion.append("; ".join(libro_no_ficcion))

#FICCIÓN
for lista_libro in lista_libros:
    if lista_libro[-1] == 'Ficción':
        libros_ficcion.append(lista_libro)
#print('Libros de ficción en el catálogo:\n', *libros_ficcion, sep="\n")

lista_ficcion = []
for libro_ficcion in libros_ficcion:
    lista_ficcion.append("; ".join(libro_ficcion))

# OTRAS CATEGORÍAS

for lista_libro in lista_libros:
    if lista_libro[-1] == 'Otras categorías':
        libros_otros.append(lista_libro)
#print('Libros de otras categorías en el catálogo:\n', *libros_otros, sep="\n")

lista_otros = []
for libro_otros in libros_otros:
    lista_otros.append("; ".join(libro_otros))

print("\n"'Libros de no ficción en el catálogo:\n', *lista_no_ficcion, sep="\n")
print("\n"'Libros de ficción en el catálogo:\n', *lista_ficcion, sep="\n")
print("\n"'Libros de otras categorías en el catálogo:\n', *lista_otros, sep="\n")
