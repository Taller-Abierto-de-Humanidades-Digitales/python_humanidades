## Microcatálogo Bibliográfico
# Catalogo

libros = ["Cuentos completos 1; Isaac Asimov; 2009; Ficción", "Cuentos completos 2; Isaac Asimov; 2009; Ficción", "De Animales a Dioses; Yuval Noah Harari; 2015; Historia General", "Homo Deus; Yuval Noah Harari; 2016; Historia General", "Prohibido Nacer; Trevor Noah; 2017; Autobiografía"]

print(libros)

# Reemplazar libro de la lista

libros[2] = "Crónicas Marciana; Ray Bradbury; 1950; Ficción"

print(libros)

# Inserción nuevos libros

libros.insert(0,"Somos Luces Abismales; Carolina Sanín; 2018; Ensayos Literarios")
libros.append("Muerte con Pingüino; Andrei Kurkov; 1996; Novela")
libros.insert(2, "Que Viva la Música!; Andrés Caicedo; 1977; Novela")

print(libros)

# Largo de la lista

print(f"La lista tiene ahora {len(libros)} libros")

# Eliminar último libro de la lista

libros.pop()
print(libros)
print(f"La lista tiene ahora {len(libros)} libros")

# Elimina un libro de la lista

libros.remove("Que Viva la Música!; Andrés Caicedo; 1977; Novela")
print(libros)
print(f"La lista tiene ahora {len(libros)} libros")


# Eliminar libro metodo del

del libros[-3]
print(libros)
print(f"La lista tiene ahora {len(libros)} libros")


# Impresión libros

print(f"El libro {libros[0].split('; ')[0]} fue escrito por {libros[0].split('; ')[1]} en el año {libros[0].split('; ')[2]} y es de género {libros[0].split('; ')[3]}")
print(f"El libro {libros[1].split('; ')[0]} fue escrito por {libros[1].split('; ')[1]} en el año {libros[1].split('; ')[2]} y es de género {libros[1].split('; ')[3]}")
print(f"El libro {libros[2].split('; ')[0]} fue escrito por {libros[2].split('; ')[1]} en el año {libros[2].split('; ')[2]} y es de género {libros[2].split('; ')[3]}")
print(f"El libro {libros[3].split('; ')[0]} fue escrito por {libros[3].split('; ')[1]} en el año {libros[3].split('; ')[2]} y es de género {libros[3].split('; ')[3]}")
print(f"El libro {libros[4].split('; ')[0]} fue escrito por {libros[4].split('; ')[1]} en el año {libros[4].split('; ')[2]} y es de género {libros[4].split('; ')[3]}")