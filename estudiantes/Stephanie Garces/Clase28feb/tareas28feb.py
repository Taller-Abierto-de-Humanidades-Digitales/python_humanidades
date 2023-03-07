#Ejercicio 1 a partir de palabras clave 
libros = [
    "Juanita Castañeda; Desespero; 2003; género poesía", "Laura Restrepo; Demasiados Héroes; 1998; género Ficción Histórica", "Mercedes Ron; La Ocasión; 2014; género Novela", "Ana Shua; Piedra y Cielo; 1987; género Cuentos", "Gabriel García Márquez; La Mala hora; 1962; género Realismo mágico"]
#le agregué al listado la palabra género
palabra_clave = "género"

libros_coincidencias = []

for libro in libros:
    if palabra_clave.lower() in libro.lower():
        libros_coincidencias.append(libro)

if libros_coincidencias:
    print(f"Los libros que contienen la palabra clave '{palabra_clave}' son:")
    for libro in libros_coincidencias:
        print(libro)
else:
    print(f"No se encontraron coincidencias con la palabra clave '{palabra_clave}'.")

#lista de libros antes 2000

fecha = 2000

libros_antiguos = []

for libro in libros:
    datos_libro = libro.split(";")
    fecha_publicacion = int(datos_libro[2].strip())
    if fecha_publicacion < fecha:
        libros_antiguos.append(libro)

if libros_antiguos:
    print(f"Los libros publicados antes de {fecha} son:")
    for libro in libros_antiguos:
        print(libro)
else:
    print(f"No se encontraron coincidencias de libros publicados antes de {fecha}.")

#ejercicio a partir del género 

género = "Novela"

resultados = []
for libro in libros:
    if género.lower() in libro.lower():
        resultados.append(libro.split("; ")[1])

if len (resultados) > 0: 
    print("Los títulos de libros que corresponden al género de", género, "son:")
    for resultado in resultados:
        print(resultado)
else:
    print("No se encontraron coincidencias para el género de", género)

#libros por gneéro en listado 

for libro in libros:
    categoria = libro.split("; ")[-1].lower() # obtenemos la categoría del libro y convertimos a minúsculas
    if "historia" in categoria:
        historia.append(libro)
    elif "filosofía" in categoria:
        filosofia.append(libro)
    else:
        otras_categorias.append(libro)

print("Libros de historia:")
for libro in historia:
    print("- " + libro.replace("; ", ", "))

print("Libros de filosofía:")
for libro in filosofia:
    print("- " + libro.replace("; ", ", "))

print("Otros libros:")
for libro in otras_categorias:
    print("- " + libro.replace("; ", ", "))

#listado libros fecha 

libros = ["Juanita Castañeda; Desespero; 2003, poesía ","Laura Restrepo; Demasiados Héroes; 1998; Ficción Histórica", "Mercedes Ron; La Ocasión; 2014; Novela", "Ana Shua; Piedra y Cielo; 1987; Cuentos","Gabriel García Márquez; La Mala hora; 1962; Realismo mágico"]

autor_buscado = "Gabriel García Márquez"
año_buscado = "1962"

resultado = []

for libro in libros:
    datos_libro = libro.split("; ")
    autor = datos_libro[0]
    titulo = datos_libro[1]
    fecha = datos_libro[2].split(", ")[0]
    genero = datos_libro[2].split(", ")[1]
    
    if autor == autor_buscado and fecha == año_buscado:
        libros_encontrados.append((titulo, fecha, genero))
        
if libros_encontrados:
    print(f"Libros de {autor_buscado} publicados en {año_buscado}:")
    for libro in libros_encontrados:
        print(f"- {libro[0]} ({libro[1]}), {libro[2]}")
else:
    print("No hay coincidencias.")
