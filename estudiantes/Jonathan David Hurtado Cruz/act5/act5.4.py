libro1 = ["Fiodor Dostoyenvski; El jugador; 1886; Realist","Simone de Beauvoir; Sangre de los otros; 1944; Histórica", "Albert Camus; El extrajenro; 1942; Existencialismo", "Jean-Paul Sartre; La Naúsea; 1938; Existencialismo","Franz Kafka; La Metaformosis; 1915; Existencialismo"]

existencialismo_in_libro = []

historica_in_libro = []

otros = []

categoria1 = "Existencialismo"
categoria2 = "Histórica"

for lib in libro1:
    if lib.lower().split("; ")[-1] == categoria1.lower():
        existencialismo_in_libro.append(lib)
        print(f"estos son los libros existencialistas:{existencialismo_in_libro}")
    elif lib.lower().split("; ")[-1] == categoria2.lower():
        historica_in_libro.append(lib)
        print(f"los libros históricos, en cambio, son estos: {historica_in_libro}.")
    else: 
        otros.append(lib)
        print(f"las novelas de otras categorías son estas:{otros}")
        
    

