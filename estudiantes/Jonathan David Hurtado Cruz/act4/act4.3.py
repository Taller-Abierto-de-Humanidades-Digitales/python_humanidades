libro1 =  ["Fiodor Dostoyenvski; El jugador; 1886; Realist", "Simone de Beauvoir; Sangre de los otros; 1944; Histórica", "Albert Camus;El extrajenro; 1942; Existencialismo", "Jean-Paul Sartre; La Naúsea; 1938; Existencialismo", "Franz Kafka; La Metaformosis; 1915; Existencialismo", "Franz Kafka; El Castillo; 1922; Existencialismo", "Franz Kafka; En la colonia penitenciaria; 1919; existencialismo", "Franz Kafka; El proceso; 1925; existencialismo"]



lista_sin_genero = []
lista_nueva_libros = []
sin_genero = []
catalogo = []



for catalogo in libro1:
    lista_nueva_libros.append(catalogo.split(';'))
    

print (catalogo)



for sin_genero in lista_nueva_libros :
    sin_genero.pop()
    lista_sin_genero.append(sin_genero)

    print (sin_genero)




