libro1 = ["Fiodor Dostoyenvski; El jugador; 1886; Realist","Simone de Beauvoir; Sangre de los otros; 1944; Histórica", "Albert Camus; El extrajenro; 1942; Existencialismo", "Jean-Paul Sartre; La Naúsea; 1938; Existencialismo","Franz Kafka; La Metaformosis; 1915; Existencialismo"]

autorclave = "Fiodor Dostoyenvski"
fechaclave = "1886"

autor_libro = []



for lib in libro1:
    autor = lib.lower().split("; ")[0]
    fecha = lib.lower().split("; ")[2]
    if autor.lower() == autorclave.lower() and fecha <= fechaclave: 
        autor_libro.append(lib)
        print (f"el autor {autorclave} publicó en {fechaclave} el libro {autor_libro}.")

else:
    print ("no hay autores que publicaran en esa fecha")




    
    