""" ['La cupula, Stephen King, 2017, Novela'],
    ['Los hombres que no amaban a las mujeres, Stieg Larsson, 2011, Misterio'],
    """

"""
Libros= "Harry Potter y la piedra filosofal; J. K. Rowling; 1997; Ficción" 

for libro in Libros:
    print(Libros)

autores = Libros.split("; ")

print(autores)
"""

# Catalogo con lista anidad 

Catalogo = [
    ['Harry Potter y la piedra filosofal', 'J. K. Rowling', '1997', 'Ficción'],
    ['Mi hombre Seducción', 'Jodi Ellen Malpas', '2012', 'Novela erótica'],
    ['El código Da Vinci', 'Dan Brown', '2003', 'Novela'],
    ]

"""for libros in Catalogo:
    #print(libros[0])

for autores in Catalogo:
    #print(autores[1])

for año in Catalogo:
   # print(año[2])

for genero in Catalogo:
    print(genero[-1])  """



"""clear"""

nuevos_libros = [['Harry Potter y el prisionero de Azkaban', 'J. K. Rowling', '1998', 'Ficción'], ['La cupula', 'Stephen King', '2017', 'Novela'],]

#Catalogo.extend(['Harry Potter y el prisionero de Azkaban', 'J. K. Rowling', '1998', 'Ficción'], ['La cupula', 'Stephen King', '2017', 'Novela'])

#for nuevos_libros in Catalogo:

Catalogo.extend(nuevos_libros)
print(nuevos_libros)


"""Libros = ['Harry Potter y la piedra filosofal, J. K. Rowling, 1997, Ficción',
    'Mi hombre Seducción, Jodi Ellen Malpas, 2012, Novela erótica',
    'El código Da Vinci, Dan Brown, 2003, Novela']


nuevos_libros = ['Harry Potter y el prisionero de Azkaban, J. K. Rowling, 1998, Ficción', 'La cupula, Stephen King, 2017, Novela', 'A Million Kisses In Your Lifetime; Mónica Murphy; 2022,  Romance contemporáneo']


Libros.extend(nuevos_libros)

print(Libros)"""