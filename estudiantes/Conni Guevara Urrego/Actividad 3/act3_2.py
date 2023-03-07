##Ejercicio 2: Crear un microcatálogo bibliográfico

""" lista_autores_as = ["Isabel Allende", "Mariana Enríquez", "Carmen Boullosa", "Cristina Peri", "Gioconda Belli", "Carlos Fuentes", "Sergio Gutiérrez", "Jorge Icaza", "Emiliano Monge", "Giuseppe Caputo"]
print(lista_autores_as)
lista_obras = ["La Casa de los espíritus", "Las Cosas que perdimos en el fuego", "El Complot de los románticos", "La Nave de los locos", "El País de las mujeres", "La Muerte de Artemio Cruz", "Los Días hábiles", "Huasipungo", "Justo antes del final", "Un mundo huérfano"]
print(lista_obras) """

libros1 = ["La Casa de los espíritus; Isabel Allende; 1982; Novela", "Las Cosas que perdimos en el fuego; Mariana Enríquez; 2016; Cuentos", "El Complot de los románticos; Carmen Boullosa; 2009; Novela", "La Nave de los locos; Cristina Peri; 1984; Ficción", "El País de las mujeres; Gioconda Belli; 2010; Novela", "La Muerte de Artemio Cruz; Carlos Fuentes; 1962; Novela ", "Sergio Gutiérrez; Los Días hábiles; 2020; Novela", "Jorge Icaza; Huasipungo; 1934; Novela indigenista", "Emiliano Monge; Justo antes del final; 2022; Novela", "Giuseppe Caputo; Un mundo huérfano; 2016; Novela"]
print(libros1)

##Reemplazar

libros1[3] = "Cuentos completos; Jorge Luis Borges; 1995; Ficción"

print(libros1)

#AGREGAR OBRAS

##Un libro al inicio mediante el método insert()

libros1.insert(0, "EL Coronel no tiene quien le escriba; Gabriel García Márquez; 1961; Novela corta")
print(libros1)

##Un libro al final mediante el método append()

libros1.append("Travesuras de la niña mala; Mario Vargas Llosa; 2006; Novela")
print(libros1)

##Un libro en la posición 3 mediante el método insert()

libros1.insert(3,"Lo que no tiene nombre; Piedad Bonnet; 2013; Biografía")
print(libros1)

##Conocer número de elementos en la lista lent()

print.lent(libros1)