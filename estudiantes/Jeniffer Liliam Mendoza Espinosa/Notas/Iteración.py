""" palabra_clave = input("Escriba la palabra clave para buscar en el catálogo:")
x = palabra_clave.lower()
print(x) """

libros = ['Vallejo, Irene; El infinito en un junco; 2021', 'de Saint-Exupery, Antoine; El Principito; 1943', 'Dostoiewski, Fedor; Pobres gentes; 1846', 'Mistral, Gabriela; Sonetos de la muerte; 1915', 'García, Luis; I took Panama; 1973', 'Bonnet, Piedad; Explicaciones no pedidas; 2011', 'Restrepo, Laura; Hot sur; 2012', 'Abad, Héctor; El olvido que seremos; 2006', 'Malcom, Janet; El periodista y el asesino; 1989; Crónica', 'Caparrós, Martín; El hambre; 2014; Crónica', 'Walsh, Rodolfo; Operación masacre; 1987; Novela']

stopwords = ['a', 'con', 'de', 'en', 'mediante', 'para', 'por', 'según', 'sin', 'el', 'la', 'los', 'las', 'un', 'una', 'unos', 'unas', 'que', 'y', 'o', 'ni', 'si', 'no']

palabra_clave = input("Escriba la palabra clave para buscar en el catálogo: ")

palabras_libros = []

for libro in libros:
    if palabra_clave.lower() not in stopwords:
        if p
        palabras_libros.append(libro)
print(f"Esta es la lista de libros del catálogo que contienen la palabra '{palabra_clave}': {palabras_libros}: ")