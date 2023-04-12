# Ejercicio 2
libros = ["Harry Potter y la piedra filosofal; J. K. Rowling; 1997; Ficción", "Mi hombre Seducción; Jodi Ellen Malpas; 2012; Novela erótica", "El código Da Vinci; Dan Brown; 2003; Novela", "La cupula; Stephen King; 2017; Novela", "Los hombres que no amaban a las mujeres; Stieg Larsson; 2011; Misterio"]
 
Libro_antes = []
Libros_despues = []

#Fecha_base = int(2003)
"""for libro in libros:
      anios = [int(libro.split("; ")[2])]
      if int(anios) < 2003:
        Libros_despues.append(int(libros))
        print(int(Libros_despues))"""

for libro in libros:
     Libro_a= int(libro.split("; ")[2])
     if Libro_a < 2003:
          Libro_antes.append(libro)
          print(f"los libro publicados antes del 2003 son: {Libro_antes}")

else:
     if Libro_a > 2003:
          Libros_despues.append(libro)
          print(f"los libro publicados despues del 2003 son: {Libros_despues}")