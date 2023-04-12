#Ejercicio 1
autores=['Edmund Husserl', "Walter Rudin", "Donald Cohn", "Andrei Kolmogorov", "Stefan Banach"]
for autor in autores:
    print(autor)

libros=["Edmund Husserl; Ideen zu einer reinen Phänomenologie und phänomenologischen Philosophie 1", "Walter Rudin; Real and Complex Analysis", "Donald Cohn; Measure Theory", "Andrei Kolmogorov; Grundbegriffe der Wahrscheinlichkeitsrechnung", "Stefan Banach; Théorie des opérations linéaires"]

print(f'Hola, soy {libros[0].split("; ")[0]} y me conocen por el libro "{libros[0].split("; ")[1]}"\
    \n Hola, soy {libros[1].split("; ")[0]} y me conocen por el libro "{libros[1].split("; ")[1]}"\
    \n Hola, soy {libros[2].split("; ")[0]} y me conocen por el libro "{libros[2].split("; ")[1]}"\
    \n Hola, soy {libros[3].split("; ")[0]} y me conocen por el libro "{libros[3].split("; ")[1]}"\
    \n Hola, soy {libros[4].split("; ")[0]} y me conocen por el libro "{libros[4].split("; ")[1]}"')

#Ejercicio 2

catalog=["Edmund Husserl; Ideen zu einer reinen Phänomenologie und phänomenologischen Philosophie; 1913; Filosofía", "Walter Rudin; Real and Complex Analysis; 1966; Matemáticas", "Donald Cohn; Measure Theory; 2015; Matemáticas", "Andrei Kolmogorov; Grundbegriffe der Wahrscheinlichkeitsrechnung; 1933; Matemáticas", "Stefan Banach; Théorie des opérations linéaires; 1932; Matemáticas"]

print(catalog[0], catalog[1], catalog[2], catalog[3], catalog[4])

#Modificar un libro
catalog[0]="Stan Wagon; The Banach-Tarski Paradox; 1985; Matemáticas"
print(catalog)

#Añadir libros
catalog.insert(0, "Edmund Husserl; Ideen zu einer reinen Phänomenologie und phänomenologischen Philosophie; 1913; Filosofía")
catalog.append("Ionnis Karatzas; Brownian Motion and Stochastic Calculus; 1987; Matemáticas")
catalog.insert(2, "Gregory Moore; Zermelo's Axiom of Choice; 1982; Matemáticas")

#Núm elementos del catálogo después de añadir libros
print(f"La lista tiene ahora {len(catalog)} libros.")

#Eliminar libros
catalog.pop(-1)
print(catalog)
catalog.remove('Edmund Husserl; Ideen zu einer reinen Phänomenologie und phänomenologischen Philosophie; 1913; Filosofía')
print(catalog)
del catalog[-3]
print(catalog)

#Núm elementos del catálogo después de remover libros
print(f"La lista tiene ahora {len(catalog)} libros.")

#Imprimir los libros
for libro in catalog:
    print(f'El libro "{libro.split("; ")[1]}" fue escrito por {libro.split("; ")[0]} en el año {libro.split("; ")[2]} y su género es {libro.split("; ")[3]}.')

#Ejercicio 3
#El comando sort() solo permite ordenar por la primera letra de cada elemento, por lo que no pude ordenarla por título y solo por nombre del autor
autor_asc=catalog.sort()
print(catalog)

autor_desc=catalog.reverse()
print(catalog)