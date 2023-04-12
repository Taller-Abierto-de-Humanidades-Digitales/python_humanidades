libro1 =  ["Fiodor Dostoyenvski; El jugador; 1886; Realist", "Simone de Beauvoir; Sangre de los otros; 1944; Histórica", "Albert Camus;El extrajenro; 1942; Existencialismo", "Jean-Paul Sartre; La Naúsea; 1938; Existencialismo", "Franz Kafka; La Metaformosis; 1915; Existencialismo", "Franz Kafka; El Castillo; 1922; Existencialismo", "Franz Kafka; En la colonia penitenciaria; 1919; existencialismo", "Franz Kafka; El proceso; 1925; existencialismo"]


titulo = []
nombres = []


for titulos_libro1 in libro1:
    titulo.append(titulos_libro1.split(';')[1])
#print (titulo)

for nombre in titulo:
    nombres.append(len(nombre[0]))

    
promedio = sum(titulo) / len(nombre)

print(f"Los títulos de los libros tienen en promedio {round(promedio, 2)} caracteres.")



