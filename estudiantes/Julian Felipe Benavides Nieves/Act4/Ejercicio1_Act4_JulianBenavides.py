# Catalogo

libros = ['Cuentos completos 1; Isaac Asimov; 2009; Ficción', 'Cuentos completos 2; Isaac Asimov; 2009; Ficción', 'De Animales a Dioses; Yuval Noah Harari; 2015; Historia General', 'Homo Deus; Yuval Noah Harari; 2016; Historia General', 'Prohibido Nacer; Trevor Noah; 2017; Autobiografía']


titulos = []
autores = []
anios = []
generos = []

# for titulo in libros:
#     titulos.append(titulo.split(';')[0])

# for autor in libros:
#     autores.append(autor.split(';')[1])

# for anio in libros:
#     anios.append(anio.split(';')[2])

# for genero in libros:
#     generos.append(genero.split(';')[3])

# print(titulos, autores, anios, generos, sep='\n')

# Se hubiera podido hacer todo sobre un único for

for libro in libros:
    titulos.append(libro.split(';')[0])
    autores.append(libro.split(';')[1])
    anios.append(libro.split(';')[2])
    generos.append(libro.split(';')[3])

print(titulos, autores, anios, generos, sep='\n')