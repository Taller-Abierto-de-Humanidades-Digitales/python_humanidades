libros = [
    "Después de 1945: la latencia como origen del presente; Hans Ulrich Gumbrecht; 2015; historia conceptual",
    "De papel. En torno a sus dos mil años de historia; Nicholas Basbanes; 2014; historia del libro",
    "No logo. El poder de las marcas; Naomi Klein; 2014; historia del diseño",
]

# Ejercicio 1

titulos = []
autores = []
anios = []
generos = []

for libro in libros:
    titulos.append(libro.split(";")[0])
    autores.append(libro.split(";")[1])
    anios.append(libro.split(";")[2])
    generos.append(libro.split(";")[3])

print(titulos, autores, anios, generos)

# Ejercicio 2

nuevos_libros = [
    "Teoría de la interpretación; Paul Ricoeur; 2017; filosofía",
    "Más allá del cuerpo. Ensayos en torno a la corporalidad; Francisco González Crussí; 2021; ensayo",
    "Fiction in the Archives. Pardon Tales and Their Tellers in Sixteenth-Century France; Natalie Zemon Davis; 1987; historia",
]

libros.extend(nuevos_libros)

print(libros)

# Ejercicio 3

libro_replace = []

for libro in libros:
    items_libro = libro.split("; ")
    items_libro.pop()
    libro_nuevo = f"{items_libro[0]}; {items_libro[1]}; {items_libro[2]}"
    libro_replace.append(libro_nuevo)

libros = libro_replace
print(libros)

# Ejercicio 4

anios = [int(libro.split("; ")[2]) for libro in libros]

fecha_promedio = sum(anios) / len(anios)

print(f"La fecha promedio de los libros de mi catálogo es: {int(fecha_promedio)}")

# Ejercicio 5

titulos = [libro.split("; ")[0] for libro in libros]

caracteres_titulos = [len(titulo) for titulo in titulos]

promedio = sum(caracteres_titulos) / len(caracteres_titulos)

print(f"El promedio de caracteres de los títulos de catálogo es: {int(promedio)}")
