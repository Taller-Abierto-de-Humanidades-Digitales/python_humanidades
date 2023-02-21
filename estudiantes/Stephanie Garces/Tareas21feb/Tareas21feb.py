#actividad 4
#1_4
#obtener algo como lo siguiente pero con mis datos 
#titulos = ["Cuentos completos", "El Aleph", "Ficciones", "El libro de arena", "El jardín de senderos que se bifurcan"]
#autores = ["Jorge Luis Borges", "Jorge Luis Borges", "Jorge Luis Borges", "Jorge Luis Borges", "Jorge Luis Borges"]
#anios = ["1995", "1949", "1944", "1945", "1941"]
#generos = ["Ficción", "Ficción", "Ficción", "Ficción", "Ficción"]

libros = ["Juanita Castañeda; Desespero; 2003, poesía ","Laura Restrepo; Demasiados Héroes; 1998; Ficción Histórica", "Mercedes Ron; La Ocasión; 2014; Novela", "Ana Shua; Piedra y Cielo; 1987; Cuentos","Gabriel García Márquez; La Mala hora; 1962; Realismo mágico"]

autores = []
titulos = []
anios = []
generos = []

for libro in libro1:
    libro_info = libro.split(";")
    autores.append(libro.split(";")[0]) #ojo cambiar acá todo el resto
    titulos.append(libro_info[1])
    anios.append(libro_info[2].strip().split(",")[0])
    generos.append(libro_info[2].strip().split(",")[1])
    
print("Títulos:", titulos)
print("Autores:", autores)
print("Años:", anios)
print("Géneros:", generos)

#2_4

librosnuevos = ["Yuval Noah Harari; De animales a dioses; 2011; Ensayo histórico" , "Eduardo Galeano; Las venas abiertas de A L; 1971; Ensayo histórico" , "Carmen McEvoy; Historia de A L; 2016; Historia"]

nuevos_libros = []
for libro in librosnuevos:
    libro_info = libro.split(";")
    nuevos_libros.append({"autor": libro_info[0], "titulo": libro_info[1], "anio": libro_info[2], "genero": libro_info[3]})
    

libros.extend(nuevos_libros)
print (libros)

#queesesto
print("\nTítulos actualizados:", titulos)

for i in range(len(libro1)):
    print("Libro ", i+1, ":")
    print("Autor:", autores[i])
    print("Título:", titulos[i])
    print("Año:", anios[i])
    print("Género:", generos[i])


#3_4 
libros_nada = []

for libro in libros: 
    items_libro = libro.split(";")
    items_libro.pop()
    libro_nuevo = f"{items_libro [0]}; {items_libro[1]}; {items_libro [2]})
    libros_nada.append(libro_nuevo)

libros = libros_nada
print(libros)

#mirarfoto

libro = ["Juanita Castañeda; Desespero; 2003, poesía ","Laura Restrepo; Demasiados Héroes; 1998; Ficción Histórica", "Mercedes Ron; La Ocasión; 2014; Novela", "Ana Shua; Piedra y Cielo; 1987; Cuentos","Gabriel García Márquez; La Mala hora; 1962; Realismo mágico"]

anios = []

for libro in libro:
    libro_info = libro.split(";")
    anios.append(int(libro_info[2].strip().split(",")[0]))

fecha_promedio = sum(anios) / len(anios)

print(f"La fecha promedio de los libros de mi catálogo es: {fecha_promedio}")

#4_4

titulos = ["Desespero; Demasiados héroes; La ocasión; Piedra y cielo; La mala hora"]
