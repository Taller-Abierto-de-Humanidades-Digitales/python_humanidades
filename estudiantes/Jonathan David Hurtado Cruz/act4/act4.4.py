libro1 = ["Fiodor Dostoyenvski; El jugador; 1886; Realist", "Simone de Beauvoir; Sangre de los otros; 1944; Histórica", "Albert Camus;El extrajenro; 1942; Existencialismo", "Jean-Paul Sartre; La Naúsea; 1938; Existencialismo", "Franz Kafka; La Metaformosis; 1915; Existencialismo", "Franz Kafka; El Castillo; 1922; Existencialismo", "Franz Kafka; En la colonia penitenciaria; 1919; existencialismo", "Franz Kafka; El proceso; 1925; existencialismo"]

anios = []
lista_nueva = []

for catalogo in libro1:
    lista_nueva.append(catalogo.split(';'))

#print (lista_nueva)

for anio_libro1 in lista_nueva:
    anios.append(int(anio_libro1[2]))


print(anios)
print(len(anios))
 


promedio = sum(anios) / len(anios)

print (promedio)
