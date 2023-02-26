#Ejercicio 3: Listado de títulos de libros por género

libros = ['Vallejo, Irene; El infinito en un junco; 2021; Ensayo', 'de Saint-Exupery, Antoine; El Principito; 1943; Novela', 'Dostoiewski, Fedor; Pobres gentes; 1846; Novela', 'Mistral, Gabriela; Sonetos de la muerte; 1915; Poesía', 'García, Luis; I took Panama; 1973; Teatro', 'Bonnet, Piedad; Explicaciones no pedidas; 2011; Poesía', 'Restrepo, Laura; Hot sur; 2012; Novela', 'Abad, Héctor; El olvido que seremos; 2006; Novela', 'Malcom, Janet; El periodista y el asesino; 1989; Crónica', 'Caparrós, Martín; El hambre; 2014; Crónica', 'Walsh, Rodolfo; Operación masacre; 1987; Novela']

genero_digitado = input('Escriba un género: ')

genero_catalogo = [libro.split("; ")[-1] for libro in libros]

#print(genero_catalogo)

libros_genero = [libro.split("; ") for libro in libros if genero_digitado.lower() in libro.lower().split("; ")[-1]]

if len(libros_genero) == 0:
    print('\n'f"Lo sentimos, en el catálogo no hay ningún libro del género '{genero_digitado}'.\n")
else:
    print('\n'f'Estos son los libros del catálogo del género "{genero_digitado}":\n{libros_genero}.\n') 

""" 
MI PRIMER INTENTO QUE SIRVIÓ PARA EL EJERCICIO
lista_libros = []
for libro in libros:
    libro = libro.split("; ")
    lista_libros.append(libro)
#print(lista_libros)  

genero_digitado = input('Escriba un género: ')
libros_por_genero = []
for lista_libro in lista_libros:
    if genero_digitado.lower() in lista_libro[-1].lower():
        libros_por_genero.append(lista_libro)
    
if len(libros_por_genero) == 0:
    print(f"Lo sentimos, en el catálogo no hay ningún libro del género '{genero_digitado}.'")
else:
    print(f'Estos son los libros del catálogo del género "{genero_digitado}":{libros_por_genero}.\n') """





