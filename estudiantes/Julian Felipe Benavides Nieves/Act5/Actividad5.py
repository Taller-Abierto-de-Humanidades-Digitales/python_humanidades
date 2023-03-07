# Catalogo

libros = ['Cuentos completos 1; Isaac Asimov; 2009; Ficción', 
          'Cuentos completos 2; Isaac Asimov; 2009; Ficción', 
          'De Animales a Dioses; Yuval Noah Harari; 2015; Historia General', 
          'Homo Deus; Yuval Noah Harari; 2016; Historia General', 
          'Prohibido Nacer; Trevor Noah; 2017; Autobiografía', 
          'Somos Luces Abismales; Carolina Sanín; 2018; Ensayos Literarios', 
          'Muerte con Pingüino; Andrei Kurkov; 1996; Novela', 
          'Que Viva la Música!; Andrés Caicedo; 1977; Novela',
          'The Beach; Alex Garland; 1996; Novela',
          'La teoria del todo; Arturo Quirantes; 2018; Divulgación',
          'Breve historia de la ciencia; Tom Jackson; 2022; Divulgación',
          'Ensayo sobre la ceguera; Jose Saramago; 1995; Novela']

#___________________________________________________
# Ejercicio 1:

busqueda = input("Introduzca la palabra de busqueda: ")

list_busqueda = []

for libro in libros:
    if busqueda.lower() in libro.lower():
        list_busqueda.append(libro)

if len(list_busqueda) > 0:
    print(f"Los libros que contienen la palabra '{busqueda}' son:")
    for libro in list_busqueda:
        print(libro)
else:
    print(f"La palabra '{busqueda}' no esta en la lista de libros")
print()

#___________________________________________________
# Ejercicio 2:

bus_lib = []

anios = []

selanio = input("Introduzca el número del año que desea buscar: ")
selanio = int(selanio)

errorselecc = True
while errorselecc:
    seleccion = input("Seleccione: a. anterior, b. igual, c. posterior: ")
    if seleccion == "a":
        errorselecc = False
    elif seleccion == "b":
        errorselecc = False
    elif seleccion == "c":
        errorselecc = False
    else:
        print("Selección errada, intente de nuevo.")

if seleccion == "a":
    for libro in libros:
        titulo, autor, anio, genero = libro.split(";")
        anio = int(anio)
        if anio < selanio:
            bus_lib.append(libro)
    if len(bus_lib) > 0:
        print("Los libros anteriores a esta fecha son: ")
        for res in bus_lib:
            print(res)
    else:
        print(f"No hay libros anteriores a {selanio}")


if seleccion == "b":
    for libro in libros:
        titulo, autor, anio, genero = libro.split(";")
        anio = int(anio)
        if anio == selanio:
            bus_lib.append(libro)
    if len(bus_lib) > 0:
        print("Los libros de esta fecha son: ")
        for res in bus_lib:
            print(res)
    else:
        print(f"No hay libros de {selanio}")

if seleccion == "c":
    for libro in libros:
        titulo, autor, anio, genero = libro.split(";")
        anio = int(anio)
        if anio > selanio:
            bus_lib.append(libro)
    if len(bus_lib) > 0:
        print("Los libros posteriores a esta fecha son: ")
        for res in bus_lib:
            print(res)
    else:
        print(f"No hay libros posteriores a {selanio}")
print()

#___________________________________________________
# Ejercicio 3:

lis_lib_gen = []

genero = input("Introduzca el genero para la busqueda de libros: ")

# Coincidencia elemento "in"

for libro in libros:
    if genero.lower() in libro.split(";")[-1].lower():
        lis_lib_gen.append(libro)

# Coincidencia por igualdad

# for libro in libros:
#     if libro.split(";")[-1][1:].lower() == genero.lower():
#         lis_lib_gen.append(libro)
    
if len(lis_lib_gen) > 0:
    for libro in lis_lib_gen:
        print(libro)
else:
    print(f"No existen libros del genero {genero}")
print()

#___________________________________________________
# Ejercicio 4:

lib_his = []
lib_nov = []
lib_fic = []
lib_otros = []

for libro in libros:
    if "Historia" in libro:
        lib_his.append(libro)
    elif "Novela" in libro:
        lib_nov.append(libro)
    elif "Ficción" in libro:
        lib_fic.append(libro)
    else:
        lib_otros.append(libro)

print()
print("Cantidad de libros en al catálogo:", len(libros))
print()
print("Libros de Historia", "Cant.:",len(lib_his))
for libro in lib_his:
    titulo, autor, anio, genero = libro.split(";")
    print(f"- {autor}, {titulo} ({anio[1:]}), {genero}")

print()
print("Libros de Novela", "Cant.:",len(lib_nov))
for libro in lib_nov:
    titulo, autor, anio, genero = libro.split(";")
    print(f"- {autor}, {titulo} ({anio[1:]}), {genero}")

print()
print("Libros de Ficción", "Cant.:",len(lib_fic))
for libro in lib_fic:
    titulo, autor, anio, genero = libro.split(";")
    print(f"- {autor}, {titulo} ({anio[1:]}), {genero}")

print()
print("Otros libros", "Cant.:",len(lib_otros))
for libro in lib_otros:
    titulo, autor, anio, genero = libro.split(";")
    print(f"- {autor}, {titulo} ({anio[1:]}), {genero}")
print()


#___________________________________________________
# Ejercicio 5:

busexacta = []
busautor = []

autorbus = input("Introduzca el autor de las obras: ") 

aniobus = input("Introduzca el año de las obras: ")

for libro in libros:
    if autorbus.lower() in libro.lower() and aniobus.lower() in libro.lower():
        busexacta.append(libro)
    elif autorbus.lower() in libro.lower() and aniobus.lower() not in libro.lower():
        busautor.append(libro)

print()
if len(busexacta) > 0:
    print(f"Del autor '{autorbus}' y el año '{aniobus}' estan los libros: ")
    print()
    for libro in busexacta:
        titulo, autor, anio, genero = libro.split(";")
        print(f"- {autor}, {titulo} ({anio[1:]}), {genero}")

print()
if len(busautor) > 0:
    print(f"Del autor '{autorbus}' pero que no coinciden con el año '{aniobus}' estan los libros: ")
    print()
    for libro in busautor:
        titulo, autor, anio, genero = libro.split(";")
        print(f"- {autor}, {titulo} ({anio[1:]}), {genero}")

elif len(busautor) == 0 and len(busautor):
    print("No hay libros del autor")

print()
