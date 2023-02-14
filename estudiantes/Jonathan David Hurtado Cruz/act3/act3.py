#Ejercicio 1
lista_autores = ["Fiodor Dostoyenvski", "Simone de Beauvoir", "Albert Camus", "Jean-Paul Sartre", "Franz Kafka", "André Breton", "Martin Heidegger"]
print (f"El primer nombre de la lista de autores es {lista_autores[0]}")
print (f"El segundo nombre de la lista de autores es {lista_autores[1]}")
print (f"El tercer nombre de la lista de autores es {lista_autores[2]}")
print (f"El cuarto nombre de la lista de autores es {lista_autores[3]}")
print (f"El quinto nombre de la lista de autores es {lista_autores[4]}")
print (f"El sexto nombre de la lista de autores es {lista_autores[5]}")
print (f"El séptimo nombre de la lista de autores es {lista_autores[6]}")

libros = ["El jugador", "Sangre de los otros", "El extrajenro", "La Naúsea", "La Metaformosis", "Manifiestos del surrealismo","ser y tiempo" ]

print (f"Hola, soy {lista_autores[0]} y me conocen por el libro {libros[0]}.")
print (f"Hola, soy {lista_autores[1]} y me conocen por el lobro {libros[1]}.")
print (f"Hola, soy {lista_autores[2]} y me conocen por el libro {libros[2]}.")
print (f"Hola, soy {lista_autores[3]} y me conocen por el libro  {libros[3]}.")
print (f"Hola, soy {lista_autores[4]} y me conocen por el libro {libros[4]}.")
print (f"Hola, soy {lista_autores[5]} y me conocen por el libro {libros[5]}.")
print (f"Hola, soy {lista_autores[6]} y me conocen por el libro {libros[6]}.")

#Ejercicio 2
libro1 = ["Fiodor Dostoyenvski; El jugador; 1886; Realist","Simone de Beauvoir; Sangre de los otros; 1944; Histórica", "Albert Camus;El extrajenro; 1942; Existencialismo", "Jean-Paul Sartre; La Naúsea; 1938, Existencialismo","Franz Kafka; La Metaformosis; 1915; Existencialismo"]

libro1[0]= "Martin Heidegger; El ser y el tiempo; 1927; Existencialismo" 

print (libro1)

libro1.insert(0, "Franz Kafka; El Proceso; 1925; Existencialismo")
libro1.append("Milan Kundera; La insoportable levadad del ser; 1984; Existencialismo")
libro1.insert(2,"Milan Kundera; La inmortalidad; 1988; Existencialismo")

print (f"la lista tiene ahora {len(libro1)} elementos.")

libro1.pop(0)
print (libro1)

libro1.remove("Albert Camus;El extrajenro; 1942; Existencialismo")
print(libro1)

del libro1 [-2]
print (libro1)

print (f"la lista tiene ahora {len(libro1)} elementos.")


print(f"El libro {libro1[1].split('; ')[1]} fue escrito por {libro1[1].split('; ')[0]} en el año {libro1[1].split('; ')[2]} y es  de género {libro1[1].split('; ')[3]}.")


#Ejercicio 3
autor_asc=libro1.sort()
print(libro1)

autor_desc=libro1.reverse()
print(libro1)




