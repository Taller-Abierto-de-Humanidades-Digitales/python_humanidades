#ejercicio 1
libro1 = ["Fiodor Dostoyenvski; El jugador; 1886; Realist","Simone de Beauvoir; Sangre de los otros; 1944; Histórica", "Albert Camus;El extrajenro; 1942; Existencialismo", "Jean-Paul Sartre; La Naúsea; 1938; Existencialismo","Franz Kafka; La Metaformosis; 1915; Existencialismo"]

autor = []
titulo = []
anios = []
genero = []



for autores_libro1 in libro1:
    autor.append(autores_libro1.split(';')[0])
    
for titulos_libro1 in libro1:
    titulo.append(titulos_libro1.split(';')[1])

for anio_libro1 in libro1:
    anios.append(anio_libro1.split(';')[2])

for genero_libro1 in libro1:
    genero.append(genero_libro1.split(';')[3])

print(titulo, autor, anios, genero)
