# Crear una lista de autores

#autores= [ 'Jackson, Sarah J., Moya Bailey, and Brooke Foucault Welles', 'Johnson, Jessica Marie, and Mark Anthony Neal','Kuo, Rachel','Noble, Safiya Umoja.','Risam, Roopika']

#publicaciones= ['#HashtagActivism: Networks of Race and Gender Justice','Introduction: Wild Seed in the Machine', 'Racial Justice Activist Hashtags: Counterpublics and Discourse Circulation', 'Toward a Critical Black Digital Humanities', 'Decolonizing the Digital Humanities in Theory and Practice']

#print(f"Hola, soy {autores[0]} y me conocen por el libro {publicaciones[0]}.")
#print(f"Hola, soy {autores[1]} y me conocen por el libro {publicaciones[1]}.")
#print(f"Hola, soy {autores[2]} y me conocen por el libro {publicaciones[2]}.")
#print(f"Hola, soy {autores[3]} y me conocen por el libro {publicaciones[3]}.")
#print(f"Hola, soy {autores[4]} y me conocen por el libro {publicaciones[4]}.")


#Crear un microcatálogo bibliográfico

catalogo=["Harry Potter y la piedra filosofal; J. K. Rowling; 1997; Ficción", "Mi hombre Seducción; Jodi Ellen Malpas; 2012; Novela erótica", "El código Da Vinci; Dan Brown; 2003; Novela", "La cupula; Stephen King; 2017; Novela", "Los hombres que no amaban a las mujeres; Stieg Larsson; 2011; Misterio"]

#print(catalogo)

catalogo[0]= "La brújula dorada; Philip Pullman; 2017, Narrativa"

#print(catalogo)

catalogo.insert(0, "Harry Potter y el prisionero de Azkaban; J. K. Rowling; 1998, Ficción")

#print(catalogo)

catalogo.append("Pídeme lo que quieras; Megan Maxwell; 2013; Novela rosa")

#print(-1, catalogo)

catalogo.insert(2, "A Million Kisses In Your Lifetime; Mónica Murphy; 2022,  Romance contemporáneo")

#print(catalogo)

#print(f"La lista tiene ahora {len(catalogo)} libros.")

catalogo.pop(2)

#print(catalogo)

catalogo.remove("Pídeme lo que quieras; Megan Maxwell; 2013; Novela rosa")

#print(catalogo)

del catalogo [-4]

#print(f"La lista tiene ahora {len(catalogo)} libros.")



# El libro [título del libro] fue escrito por [autor o autora] en el año [año de publicación] y es de género [género].


#print(f"El libro {catalogo[0].split('; ')[0]} fue escrito por {catalogo[0].split('; ')[1]} en el año {catalogo[0].split('; ')[2]} y es de género {catalogo[0].split('; ')[-1]} ")

print(f"El libro {catalogo[1].split('; ')[0]} fue escrito por {catalogo[1].split('; ')[1]} en el año {catalogo[1].split('; ')[2]} y es de género {catalogo[1].split('; ')[-1]} ")





# Organizar una lista

titulo_asc = catalogo.copy()
#titulo_asc.sort()
#print(titulo_asc)

titulo_desc = catalogo.copy()
#titulo_desc.sort(reverse=True)
#titulo_asc.reverse()
#print(titulo_desc)