#Ejercicio_4

libros = ["Harry Potter y la piedra filosofal; J. K. Rowling; 1997; Ficción", "Mi hombre Seducción; Jodi Ellen Malpas; 2012; Novela erótica", "El código Da Vinci; Dan Brown; 2003; Novela", "La cupula; Stephen King; 2017; Novela", "Los hombres que no amaban a las mujeres; Stieg Larsson; 2011; Misterio"]


Misterio_libro = []

Novela_libro = []

otras_categorias = []

misterio = "misterio" 
novela = "novela"


for libro in libros:
     if libro.lower().split("; ")[-1] == misterio.lower():
        Misterio_libro.append(libro)
        print(f" Libros de misterio:{Misterio_libro}")

     elif libro.lower().split("; ")[-1] == novela.lower():
         Novela_libro.append(libro)
         print(f" Libros de novela: {Novela_libro}")

else:
  otras_categorias.append(libro)
  print(f"otras novelas: {otras_categorias}")
