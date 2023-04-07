catalogo=["Harry Potter y la piedra filosofal; J. K. Rowling; 1997; Ficción", "Mi hombre Seducción; Jodi Ellen Malpas; 2012; Novela erótica", "El código Da Vinci; Dan Brown; 2003; Novela", "La cupula; Stephen King; 2017; Novela", "Los hombres que no amaban a las mujeres; Stieg Larsson; 2011; Misterio"]

#Ejercicio-----------------------1

autores = []

for autor in catalogo:
    autores.append(autor.split("; ")[1])


titulos = []
for titulo in catalogo:
    titulos.append(titulo.split("; ")[0])

anios = []   
for anitos in catalogo:
    anios.append(anitos.split("; ")[2])

genero = []    
for generos in catalogo:
    genero.append(generos.split("; ")[-1])


print(f"Estos son los acutores del cátalogo: {autores}")
print(f"Estos son los títulos  del cátalogo: {titulos}")
print(f"Estos son los años del cátalogo: {anios}")
print(f"Estos son los géneros del cátalogo: {genero}")


#Ejercicio-----------------------2

nuevos_libros = ["Harry Potter y el prisionero de Azkaban, J. K. Rowling, 1998, Ficción", "La cupula, Stephen King, 2017, Novela", "A Million Kisses In Your Lifetime; Mónica Murphy; 2022,  Romance contemporáneo"]

catalogo.extend(nuevos_libros)
print(catalogo)


#Ejercicio-----------------------3

nuevo_catalogo = []
sin_genero = []

for libros in catalogo:
    nuevo_catalogo.append(libros.split("; "))
    print(nuevo_catalogo)

for genero in nuevo_catalogo:
    genero.pop()
    sin_genero.append(genero) 
    print(sin_genero)   


    
