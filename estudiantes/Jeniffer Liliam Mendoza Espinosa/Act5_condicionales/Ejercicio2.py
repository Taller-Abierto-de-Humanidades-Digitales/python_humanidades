#Ejercicio 2: Lista de libros anteriores o posteriores a una fecha
libros = ['Vallejo, Irene; El infinito en un junco; 2021; Ensayo', 'de Saint-Exupery, Antoine; El Principito; 1943; Novela', 'Dostoiewski, Fedor; Pobres gentes; 1846; Novela', 'Mistral, Gabriela; Sonetos de la muerte; 1915; Poesía', 'García, Luis; I took Panama; 1973; Teatro', 'Bonnet, Piedad; Explicaciones no pedidas; 2011; Poesía', 'Restrepo, Laura; Hot sur; 2012; Novela', 'Abad, Héctor; El olvido que seremos; 2006; Novela', 'Malcom, Janet; El periodista y el asesino; 1989; Crónica', 'Caparrós, Martín; El hambre; 2014; Crónica', 'Walsh, Rodolfo; Operación masacre; 1987; Novela']

anio_digitado = int(input("Escriba un año: "))

libros_publicados_misma_fecha = []
libros_publicados_antes = []
libros_publicados_despues = []


for libro in libros:
    items_libro = (libro.split('; '))
    fecha_libros = int(items_libro[2])
    #print(fecha_libros)
    """ if anio_digitado > 2023:
       #print('No hemos llegado a ese año')
       pass """
    if fecha_libros == anio_digitado:
        libros_publicados_misma_fecha.append(libro)
    elif fecha_libros  < anio_digitado:
        libros_publicados_antes.append(libro)
    elif fecha_libros  > anio_digitado:
        libros_publicados_despues.append(libro)

if anio_digitado > 2023:
    print('No hemos llegado a ese año')
elif len(libros_publicados_antes) >= 1:
        print('\n'f'Los libros del catálogo publicados en algún año anterior a {anio_digitado} son:\n {libros_publicados_antes}.')
else:
     print('\n'f'En este catálogo no hay libros publicados antes de {anio_digitado}.')
if len(libros_publicados_despues) >= 1:
        print('\n'f'Los libros del catálogo publicados en algún año posterior a {anio_digitado} son:\n {libros_publicados_despues}.')
else:
     print(f'En este catálogo no hay libros publicados después de {anio_digitado}.')
if len(libros_publicados_misma_fecha) >= 1:
    print('\n'f'Hay al menos un libro del catálogo publicado en {anio_digitado}: {libros_publicados_misma_fecha}.')
 