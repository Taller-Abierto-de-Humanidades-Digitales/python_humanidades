#Ejercicio_3

libros = ["Harry Potter y la piedra filosofal; J. K. Rowling; 1997; Ficción", "Mi hombre Seducción; Jodi Ellen Malpas; 2012; Novela erótica", "El código Da Vinci; Dan Brown; 2003; Novela", "La cupula; Stephen King; 2017; Novela", "Los hombres que no amaban a las mujeres; Stieg Larsson; 2011; Misterio"]


libro_genero = []

genero = "Misterio"

for libro in libros:
    if libro.lower().split("; ")[-1] == genero.lower():
        libro_genero.append(libro)
        print(f" El género {genero} se encuentra en {libro_genero}")
else:

    print(f" El genero {genero} no se encuentra en estos libros.")