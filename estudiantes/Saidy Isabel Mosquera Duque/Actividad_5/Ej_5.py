libros = ["Harry Potter y la piedra filosofal; J. K. Rowling; 1997; Ficción", "Mi hombre Seducción; Jodi Ellen Malpas; 2012; Novela erótica", "El código Da Vinci; Dan Brown; 2003; Novela", "La cupula; Stephen King; 2017; Novela", "Los hombres que no amaban a las mujeres; Stieg Larsson; 2011; Misterio", "Harry Potter y el prisionero de Azkaban; J. K. Rowling; 1998; Ficción"]


autor_1 = "J. K. Rowling"
fecha_1 = "1998"

autor_libro = []

"""for libro in libros:
    autor = libro.split(" ; ")[1]
    fecha = libro.split(" ; ")[2]
    if autor_1 == autor and fecha_1 == fecha: 
        autor_libro.append(libros)
        print(autor_libro)
"""

for libro in libros:
   autor = libro.lower().split("; ")[1]
   fecha = libro.lower().split("; ")[2]

   if autor.lower() == autor_1.lower() and fecha <= fecha_1:
      autor_libro.append(libro)
      print(f"los libros del {autor_1} publicados en 1998 o antes son:{autor_libro}")
   



 #autor_libro = [libro.lower().split("; ")[1] for libro in libro if autor in libros] 
