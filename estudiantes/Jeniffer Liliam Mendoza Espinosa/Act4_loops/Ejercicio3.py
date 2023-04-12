#Ejercicio 3: Eliminar la categoría “género” del microcatálogo bibliográfico

libros = ['Vallejo, Irene; El infinito en un junco; 2021; Ensayo', 'de Saint-Exupery, Antoine; El Principito; 1943; Novela', 'Dostoiewski, Fedor; Pobres gentes; 1846; Novela', 'Mistral, Gabriela; Sonetos de la muerte; 1915; Poesía', 'García, Luis; I took Panama; 1973; Teatro', 'Bonnet, Piedad; Explicaciones no pedidas; 2011; Poesía', 'Restrepo, Laura; Hot sur; 2012; Novela', 'Abad, Héctor; El olvido que seremos; 2006; Novela']

libros_sin_genero = []

for libro in libros:
    libro = libro.split("; ")
    libro.pop(3)
    libros_sin_genero.append(libro)
print(libros_sin_genero)

lista_libros_sin_genero = []
for libro_sin_genero in libros_sin_genero:
    lista_libros_sin_genero.append("; ".join(libro_sin_genero))
print(lista_libros_sin_genero)

