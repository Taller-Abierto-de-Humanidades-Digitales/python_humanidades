#tareas para feb 14

#Ejercicio 1
listado_autores = ["Max Hering", "Paolo Vignolo", "Pablo Rodríguez", "Stefania Gallini", "Claudia Leal", "Lucía Duque", "Slenka Botello"]
print (f"El primer nombre de la lista de autores es {listado_autores[0]}")
print (f"El segundo nombre de la lista de autores es {listado_autores[1]}")
print (f"El tercer nombre de la lista de autores es {listado_autores[2]}")
print (f"El cuarto nombre de la lista de autores es {listado_autores[3]}")
print (f"El quinto nombre de la lista de autores es {listado_autores[4]}")
print (f"El sexto nombre de la lista de autores es {listado_autores[5]}")
print (f"El séptimo nombre de la lista de autores es {listado_autores[6]}")

libros = ["El peso de la sangre", "El valor del patrimonio", "Matrimonio Incestuoso", "The Citys currents", "Paisajes de libertad", "Los mapas en la Gran Colombia","Cuerpos en Pecado" ]

print (f"Hola, soy {listado_autores[0]} y me conocen por el libro {libros[0]}.")
print (f"Hola, soy {listado_autores[1]} y me conocen por el libro {libros[1]}.")
print (f"Hola, soy {listado_autores[2]} y me conocen por el libro {libros[2]}.")
print (f"Hola, soy {listado_autores[3]} y me conocen por el libro  {libros[3]}.")
print (f"Hola, soy {listado_autores[4]} y me conocen por el libro {libros[4]}.")
print (f"Hola, soy {listado_autores[5]} y me conocen por el libro {libros[5]}.")
print (f"Hola, soy {listado_autores[6]} y me conocen por el libro {libros[6]}.")


#Ejercicio 2


libro1 = ["Juanita Castañeda; Desespero; 2003, poesía ","Laura Restrepo; Demasiados Héroes; 1998; Ficción Histórica", "Mercedes Ron; La Ocasión; 2014; Novela", "Ana Shua; Piedra y Cielo; 1987; Cuentos","Gabriel García Márquez; La Mala hora; 1962; Realismo mágico"]

libro1[0]= "Gabriel García Márquez; Cien años de soledad; 1967 ; Realismo" 

print (libro1)

libro1.insert(0, "El nombre de la rosa; Umberto Eco; 1980; Misterio")
libro1.append("La Catedral del mar; Idelfonso F; 2006 ; Novela")
libro1.insert(2,"La dama del alba; Alejandro Casona; 1944; Drama")

print (f"la lista tiene ahora {len(libro1)} elementos.")

libro1.pop(0)
print (libro1)

libro1.remove("Laura Restrepo; Demasiados Héroes; 1998; Ficción Histórica")
print(libro1)

del libro1 [-2]
print (libro1)

print (f"la lista tiene ahora {len(libro1)} elementos.")


print(f"El libro {libro1[1].split('; ')[1]} fue escrito por {libro1[1].split('; ')[0]} en el año {libro1[1].split('; ')[2]} y es  de género {libro1[1].split('; ')[3]}.")

#ejercicio 3
# 
autor_asc=libro1.sort()
print(libro1)

autor_desc=libro1.reverse()
print(libro1)