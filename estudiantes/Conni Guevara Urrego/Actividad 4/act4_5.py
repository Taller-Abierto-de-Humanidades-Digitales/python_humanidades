##Ejercicio 5: Calcula el promedio de caracteres de los títulos de tu catálogo

""" libros = ["La Casa de los espíritus; Isabel Allende; 1982; novela", "Las Cosas que perdimos en el fuego; Mariana Enríquez; 2016; cuentos", "El Complot de los románticos; Carmen Boullosa; 2009; novela", "La Nave de los locos; Cristina Peri; 1984; ficción", "El País de las mujeres; Gioconda Belli; 2010; novela", "La Muerte de Artemio Cruz; Carlos Fuentes; 1962; novela ", "Los Días hábiles; Sergio Gutiérrez; 2020; novela", "Huasipungo; Jorge Icaza; 1934; novela indigenista", "Justo antes del final; Emiliano Monge; 2022; novela", "Un mundo huérfano; Giuseppe Caputo; 2016; novela", "Papeles arrugados; Julián Fernández Ortíz; 2023; Poesía", "Mamá; Mariana Ruíz Johnson; 2013; Álbum Ilustrado", "El Mundo Invisible de Hayao Miyazaki; Laura Montero Plata; 2012; Ficción"] """

titulos = ["La Casa de los espíritus", "Las Cosas que perdimos en el fuego", "El Complot de los románticos", "La Nave de los locos", "El País de las mujeres", "La Muerte de Artemio Cruz", "Los Días hábiles", "Huasipungo", "Justo antes del final", "Un mundo huérfano"]

print(titulos)

iniciales = []
finales = []
longitud = []

for titulo in titulos:
    iniciales.append(titulo[0])
    finales.append(titulo[-1])
    longitud.append(len(titulo))

print(iniciales, finales, longitud)
promedio = sum(longitud) /len(titulos)

print(f"El promedio de caracteres de los títulos de mi catálogo es: {promedio}")