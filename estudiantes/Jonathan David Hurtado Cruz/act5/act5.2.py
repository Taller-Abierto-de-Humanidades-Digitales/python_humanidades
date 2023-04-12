libro1 = ["Fiodor Dostoyenvski; El jugador; 1886; Realist","Simone de Beauvoir; Sangre de los otros; 1944; Histórica", "Albert Camus; El extrajenro; 1942; Existencialismo", "Jean-Paul Sartre; La Naúsea; 1938; Existencialismo","Franz Kafka; La Metaformosis; 1915; Existencialismo"]

fecha_anterior =  []

fecha_posterior = []


for lib in libro1:
     lib_menor = int(lib.split("; ")[2])
     if lib_menor <= 1930:
          fecha_anterior.append(lib)
          print(f"los libro publicados antes del año 1930 son los siguientes: {fecha_anterior}")
else:
     if lib_menor > 1930:
          fecha_posterior.append(lib)
          print(f"los libro publicados después del 2003 son: {fecha_posterior}")

        