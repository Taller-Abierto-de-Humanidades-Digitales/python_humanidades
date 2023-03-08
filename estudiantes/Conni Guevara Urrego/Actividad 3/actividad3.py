##Ejercicio 1: Crear un listado de autores

lista_autores_as = ["Isabel Allende", "Mariana Enríquez", "Carmen Boullosa", "Cristina Peri", "Gioconda Belli", "Carlos Fuentes", "Sergio Gutiérrez", "Jorge Icaza", "Emiliano Monge", "Giuseppe Caputo"]
print(lista_autores_as)

print(F"Novelista de latinoamerica, podría ser {lista_autores_as [0]}")
print(F"Novelista de latinoamerica, podría ser {lista_autores_as [1]}")
print(F"Novelista de latinoamerica, podría ser {lista_autores_as [2]}")
print(F"Novelista de latinoamerica, podría ser {lista_autores_as [3]}")
print(F"Novelista de latinoamerica, podría ser {lista_autores_as [4]}")
print(F"Novelista de latinoamerica, podría ser {lista_autores_as [5]}")
print(F"Novelista de latinoamerica, podría ser {lista_autores_as [6]}")
print(F"Novelista de latinoamerica, podría ser {lista_autores_as [7]}")
print(F"Novelista de latinoamerica, podría ser {lista_autores_as [8]}")
print(F"Novelista de latinoamerica, podría ser {lista_autores_as [9]}")

lista_obras = ["La Casa de los espíritus", "Las Cosas que perdimos en el fuego", "El Complot de los románticos", "La Nave de los locos", "El País de las mujeres", "La Muerte de Artemio Cruz", "Los Días hábiles", "Huasipungo", "Jjusto antes del final", "Un mundo huérfano"]
print(lista_obras)

print(F"Isabel Allende, escribió {lista_obras [3]}")
print(F"Mariana Enríquez, escribió {lista_obras [1]}")
print(F"Carmen Boullosa, escribió {lista_obras [2]}")
print(F"Cristina Peri, escribió {lista_obras [3]}")
print(F"Goconda Belli, escribió {lista_obras [4]}")
print(F"Carlos Fuentes, escribió {lista_obras [5]}")
print(f"Sergio Gutiérrez, escribió {lista_obras[6]}")
print(f"Jorge Icaza, escribió {lista_obras [7]}")
print(f"Emiliano Monge, escribió {lista_obras [8]}")
print(f"Giuseppe Caputo, escribió {lista_obras [9]} ")

lista_autores_as = ["Isabel Allende", "Mariana Enríquez", "Carmen Boullosa", "Cristina Peri", "Goconda Belli", "Carlos Fuentes", "Sergio Gutiérrez", "Jorge Icaza", "Emiliano Monge", "Giuseppe Caputo"]
print(lista_autores_as)
lista_obras = ["La Casa de los espíritus", "Las Cosas que perdimos en el fuego", "El Complot de los románticos", "La Nave de los locos", "El País de las mujeres", "La Muerte de Artemio Cruz", "Los Día hábiles", "Huasipungo", "Jjusto antes del final", "Un mundo huérfano"]
print(lista_obras)

print(f"Hola, soy {lista_autores_as [0]} y me conocen por el libor {lista_obras [0]}")
print(f"Hola, soy {lista_autores_as [0]} y me conocen por el libor {lista_obras [1]}")
print(f"Hola, soy {lista_autores_as [0]} y me conocen por el libor {lista_obras [2]}")
print(f"Hola, soy {lista_autores_as [0]} y me conocen por el libor {lista_obras [3]}")
print(f"Hola, soy {lista_autores_as [0]} y me conocen por el libor {lista_obras [4]}")
print(f"Hola, soy {lista_autores_as [0]} y me conocen por el libor {lista_obras [5]}")
print(f"Hola, soy {lista_autores_as [0]} y me conocen por el libor {lista_obras [6]}")
print(f"Hola, soy {lista_autores_as [0]} y me conocen por el libor {lista_obras [7]}")
print(f"Hola, soy {lista_autores_as [0]} y me conocen por el libor {lista_obras [8]}")
print(f"Hola, soy {lista_autores_as [0]} y me conocen por el libor {lista_obras [9]}")

##Ejercicio 2: Crear un microcatálogo bibliográfico

""" lista_autores_as = ["Isabel Allende", "Mariana Enríquez", "Carmen Boullosa", "Cristina Peri", "Gioconda Belli", "Carlos Fuentes", "Sergio Gutiérrez", "Jorge Icaza", "Emiliano Monge", "Giuseppe Caputo"]
print(lista_autores_as)
lista_obras = ["La Casa de los espíritus", "Las Cosas que perdimos en el fuego", "El Complot de los románticos", "La Nave de los locos", "El País de las mujeres", "La Muerte de Artemio Cruz", "Los Días hábiles", "Huasipungo", "Justo antes del final", "Un mundo huérfano"]
print(lista_obras) """

libros1 = ["La Casa de los espíritus; Isabel Allende; 1982; novela", "Las Cosas que perdimos en el fuego; Mariana Enríquez; 2016; cuentos", "El Complot de los románticos; Carmen Boullosa; 2009; novela", "La Nave de los locos; Cristina Peri; 1984; ficción", "El País de las mujeres; Gioconda Belli; 2010; novela", "La Muerte de Artemio Cruz; Carlos Fuentes; 1962; novela ", "Los Días hábiles; Sergio Gutiérrez; 2020; novela", "Huasipungo; Jorge Icaza; 1934; novela indigenista", "Justo antes del final; Emiliano Monge; 2022; novela", "Un mundo huérfano; Giuseppe Caputo; 2016; novela"]
print(libros1)

##Reemplazar

libros1[3] = "Cuentos completos; Jorge Luis Borges; 1995; ficción"

print(libros1)

#AGREGAR OBRAS

##Un libro al inicio mediante el método insert()

libros1.insert(0, "EL Coronel no tiene quien le escriba; Gabriel García Márquez; 1961; novela corta")
print(libros1)

##Un libro al final mediante el método append()

libros1.append("Travesuras de la niña mala; Mario Vargas Llosa; 2006; novela")
print(libros1)

##Un libro en la posición 3 mediante el método insert()

libros1.insert(3,"Lo que no tiene nombre; Piedad Bonnet; 2013; biografía")
print(libros1)

##Conocer número de elementos en la lista lent()

print(f"La lista tiene ahora {len(libros1)} libros.")

#Eliminación de obra en la lista

libros1.pop(12)
print(libros1)

print(f"La lista tiene ahora {len(libros1)} libros.")

del libros1[3]
print(libros1)

print(f"La lista tiene ahora {len(libros1)} libros.")

del libros1[-3]
print(libros1)

print(f"La lista tiene ahora {len(libros1)} libros.")

##Impresión cada elementos de la lista

##El libro [título del libro] fue escrito por [autor o autora] en el año [año de publicación] y es de género [género]

print(f"El libro {libros1[0].split('; ')[0]} fue escrito por {libros1[0].split('; ')[-3]} en el año {libros1[0].split('; ')[2]} y es de género {libros1[0].split('; ')[3]}")
print(f"El libro {libros1[1].split('; ')[0]} fue escrito por {libros1[1].split('; ')[1]} en el año {libros1[1].split('; ')[2]} y es de género {libros1[1].split('; ')[3]}")
print(f"El libro {libros1[2].split('; ')[0]} fue escrito por {libros1[2].split('; ')[1]} en el año {libros1[2].split('; ')[2]} y es de género {libros1[2].split('; ')[3]}")
print(f"El libro {libros1[3].split('; ')[0]} fue escrito por {libros1[3].split('; ')[-3]} en el año {libros1[3].split('; ')[2]} y es de género {libros1[3].split('; ')[3]}")
print(f"El libro {libros1[4].split('; ')[0]} fue escrito por {libros1[4].split('; ')[1]} en el año {libros1[4].split('; ')[2]} y es de género {libros1[4].split('; ')[3]}")
print(f"El libro {libros1[5].split('; ')[0]} fue escrito por {libros1[5].split('; ')[1]} en el año {libros1[5].split('; ')[2]} y es de género {libros1[5].split('; ')[3]}")
print(f"El libro {libros1[6].split('; ')[0]} fue escrito por {libros1[6].split('; ')[1]} en el año {libros1[6].split('; ')[2]} y es de género {libros1[6].split('; ')[3]}")
print(f"El libro {libros1[7].split('; ')[0]} fue escrito por {libros1[7].split('; ')[1]} en el año {libros1[7].split('; ')[2]} y es de género {libros1[7].split('; ')[3]}")
print(f"El libro {libros1[8].split('; ')[0]} fue escrito por {libros1[8].split('; ')[1]} en el año {libros1[8].split('; ')[2]} y es de género {libros1[8].split('; ')[3]}")
print(f"El libro {libros1[9].split('; ')[-4]} fue escrito por {libros1[9].split('; ')[1]} en el año {libros1[9].split('; ')[2]} y es de género {libros1[9].split('; ')[3]}")


##Ejercicio 3: Organizar una lista

""" libros1.sort()
print(libros1) """

titulo_asc = libros1.copy()
print(titulo_asc)

titulo_asc.sort()
print(titulo_asc)

titulo_desc = libros1.copy()
print(titulo_desc)

titulo_desc.sort(reverse=True)
print(titulo_desc)