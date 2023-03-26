##Ejercicio 4: Calcula la fecha promedio de los libros de tu catálogo

""" libros = ["La Casa de los espíritus; Isabel Allende; 1982; novela", "Las Cosas que perdimos en el fuego; Mariana Enríquez; 2016; cuentos", "El Complot de los románticos; Carmen Boullosa; 2009; novela", "La Nave de los locos; Cristina Peri; 1984; ficción", "El País de las mujeres; Gioconda Belli; 2010; novela", "La Muerte de Artemio Cruz; Carlos Fuentes; 1962; novela ", "Los Días hábiles; Sergio Gutiérrez; 2020; novela", "Huasipungo; Jorge Icaza; 1934; novela indigenista", "Justo antes del final; Emiliano Monge; 2022; novela", "Un mundo huérfano; Giuseppe Caputo; 2016; novela", "Papeles arrugados; Julián Fernández Ortíz; 2023; Poesía", "Mamá; Mariana Ruíz Johnson; 2013; Álbum Ilustrado", "El Mundo Invisible de Hayao Miyazaki; Laura Montero Plata; 2012; Ficción"] """

anios = [1982, 2016, 2009, 1984, 2010, 1962, 2020, 1934, 2022, 2016, 2023, 2013, 2012]

print(anios)

suma = 0

for valor in anios:
    suma = suma + valor

print(f"La suma es {suma}")

cantidad_anios = len(anios)
promedio = suma / cantidad_anios

print(f"La fecha promedio de los libros de mi catálogo es: {round (promedio, )}")