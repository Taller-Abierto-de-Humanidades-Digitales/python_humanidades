libro1 = ["Fiodor Dostoyenvski; El jugador; 1886; Realist","Simone de Beauvoir; Sangre de los otros; 1944; Histórica", "Albert Camus; El extrajenro; 1942; Existencialismo", "Jean-Paul Sartre; La Naúsea; 1938; Existencialismo","Franz Kafka; La Metaformosis; 1915; Existencialismo"]

genero_in_libro = []

genero = "Histórica"

for lib in libro1:
    if lib.lower().split("; ")[-1] == genero.lower():
        genero_in_libro.append(lib)
        print(f" El género {genero} se encuentra en {genero_in_libro}")
else:
    print(f" El genero {genero} no se encuentra en estos libros.")

    