libro1 = ["Fiodor Dostoyenvski; El jugador; 1886; Realist","Simone de Beauvoir; Sangre de los otros; 1944; Histórica", "Albert Camus;El extrajenro; 1942; Existencialismo", "Jean-Paul Sartre; La Naúsea; 1938; Existencialismo","Franz Kafka; La Metaformosis; 1915; Existencialismo"]

palabra_codigo = "Dostoyenvski"
libros = []



for lib in libro1:
    if palabra_codigo.lower() in lib.lower():
        libros.append(lib)
        print(f"la plabra clave {palabra_codigo} está en: {lib}")

    else: 
        print(f" la palabra clave {palabra_codigo} no está en la lista")


    