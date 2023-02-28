#Ejercicio 1: Crear un microcatálogo bibliográfico

libros =['Vallejo, Irene; El infinito en un junco; 2021; Ensayo', 'de Saint-Exupery, Antoine; El Principito; 1943; Novela', 'Dostoiewski, Fedor; Pobres gentes; 1846; Novela', 'Mistral, Gabriela; Sonetos de la muerte; 1915; Poesía', 'García, Luis; I took Panama; 1973; Teatro']

autores = []
titulos = []
anios = []
generos = []

for libro in libros:
    autores.append(libro.split(';')[0])
    titulos.append(libro.split(';')[1])
    anios.append(libro.split(';')[2])
    generos.append(libro.split(';')[3])

print(titulos)
print(autores)
print(anios)
print(generos)
   

