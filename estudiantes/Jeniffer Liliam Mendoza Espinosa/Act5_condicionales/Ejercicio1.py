#Ejercicio 1: Lista de libros a partir de palabras clave
libros = ['Vallejo, Irene; El infinito en un junco; 2021; Ensayo', 'de Saint-Exupery, Antoine; El Principito; 1943; Novela', 'Dostoiewski, Fedor; Pobres gentes; 1846; Novela', 'Mistral, Gabriela; Sonetos de la muerte; 1915; Poesía', 'García, Luis; I took Panama; 1973; Teatro', 'Bonnet, Piedad; Explicaciones no pedidas; 2011; Poesía', 'Restrepo, Laura; Hot sur; 2012; Novela', 'Abad, Héctor; El olvido que seremos; 2006; Novela', 'Malcom, Janet; El periodista y el asesino; 1989; Crónica', 'Caparrós, Martín; El hambre; 2014; Crónica', 'Walsh, Rodolfo; Operación masacre; 1987; Novela']

palabra_clave = input("Escriba la palabra clave para buscar en el catálogo: ")

palabras_libros = []

for libro in libros:
    if palabra_clave.lower() in libro.lower():
        palabras_libros.append(libro)
    

if len(palabras_libros) > 0:
    print("\n" f"Esta es la lista de libros que contienen la palabra '{palabra_clave}':\n{palabras_libros}\n")
else:
    print("\n" f"Ningún libro del catálogo contiene la palabra '{palabra_clave}'.")


