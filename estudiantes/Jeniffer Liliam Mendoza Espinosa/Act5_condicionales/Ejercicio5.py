#Ejercicio 5: Lista de títulos por autor y fecha

libros = ['Vallejo, Irene; El infinito en un junco; 2021; Ensayo', 'de Saint-Exupery, Antoine; El Principito; 1943; Novela', 'Dostoiewski, Fedor; Pobres gentes; 1846; Novela', 'Mistral, Gabriela; Sonetos de la muerte; 1915; Poesía', 'García, Luis; I took Panama; 1973; Teatro', 'Bonnet, Piedad; Explicaciones no pedidas; 2011; Poesía', 'Restrepo, Laura; Hot sur; 2012; Novela', 'Abad, Héctor; El olvido que seremos; 2006; Novela', 'Malcom, Janet; El periodista y el asesino; 1989; Crónica', 'Caparrós, Martín; El hambre; 2014; Crónica', 'Walsh, Rodolfo; Operación masacre; 1987; Novela']

autor_buscado = input('Digite un autor: ')
fecha_buscada = input('Digite una fecha: ')

lista_busqueda = []

for libro in libros:
    autor, titulo, anio, genero = libro.split("; ")
    if autor_buscado.lower() in autor.lower() and fecha_buscada == anio:
        lista_busqueda.append(titulo + ", " + anio + ", " + genero)

if len(lista_busqueda) == 0:
    print("Lo sentimos, no hay resultados para su búsqueda.")
else:
    print("\n" f"Libros de {autor_buscado} en {fecha_buscada}:\n{lista_busqueda}")

    
