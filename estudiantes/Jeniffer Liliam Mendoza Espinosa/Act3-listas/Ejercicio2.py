#Ejercicio 2: Crear un microcatálogo bibliográfico
lista_publicaciones =['Vallejo, Irene; El infinito en un junco; 2021; Ensayo', 'de Saint-Exupery, Antoine; El Principito; 1943; Novela', 'Dostoiewski, Fedor; Pobres gentes; 1846; Novela', 'Mistral, Gabriela; Sonetos de la muerte; 1915; Poesía', 'García, Luis; I took Panama; 1973; Teatro']
print(lista_publicaciones)

lista_publicaciones[0] = 'Woolf, Virginia; La señora Dalloway; 1925; Novela'
lista_publicaciones[3] = 'Mendoza, Mario; La importancia de morir a tiempo; 2012; Novela'
print(lista_publicaciones)

lista_publicaciones.insert(0, 'Kawabata, Yasunari; País de nieve; 1948; Novela')
print(lista_publicaciones)

lista_publicaciones.append('Caicedo, Andrés; Destinos fatales; 1984; Cuento')
print(lista_publicaciones)

lista_publicaciones.insert(2, 'Caicedo, Andrés; ¡Que viva la música!; 1977; Novela')
print(lista_publicaciones)

print(f"La lista tiene ahora {len(lista_publicaciones)} libros.")

print(f"El libro {lista_publicaciones[0].split('; ')[1]} fue escrito por {lista_publicaciones[0].split('; ')[0]} en el año {lista_publicaciones[0].split('; ')[2]} y es de género {lista_publicaciones[0].split('; ')[3]}.")

print(f"El libro {lista_publicaciones[1].split('; ')[1]} fue escrito por {lista_publicaciones[1].split('; ')[0]} en el año {lista_publicaciones[1].split('; ')[2]} y es de género {lista_publicaciones[1].split('; ')[3]}.")
print(f"El libro {lista_publicaciones[2].split('; ')[1]} fue escrito por {lista_publicaciones[2].split('; ')[0]} en el año {lista_publicaciones[2].split('; ')[2]} y es de género {lista_publicaciones[2].split('; ')[3]}.")
print(f"El libro {lista_publicaciones[3].split('; ')[1]} fue escrito por {lista_publicaciones[3].split('; ')[0]} en el año {lista_publicaciones[3].split('; ')[2]} y es de género {lista_publicaciones[3].split('; ')[3]}.")
print(f"El libro {lista_publicaciones[4].split('; ')[1]} fue escrito por {lista_publicaciones[4].split('; ')[0]} en el año {lista_publicaciones[4].split('; ')[2]} y es de género {lista_publicaciones[4].split('; ')[3]}.")
print(f"El libro {lista_publicaciones[5].split('; ')[1]} fue escrito por {lista_publicaciones[5].split('; ')[0]} en el año {lista_publicaciones[5].split('; ')[2]} y es de género {lista_publicaciones[5].split('; ')[3]}.")
print(f"El libro {lista_publicaciones[6].split('; ')[1]} fue escrito por {lista_publicaciones[6].split('; ')[0]} en el año {lista_publicaciones[6].split('; ')[2]} y es de género {lista_publicaciones[6].split('; ')[3]}.")
print(f"El libro {lista_publicaciones[7].split('; ')[1]} fue escrito por {lista_publicaciones[7].split('; ')[0]} en el año {lista_publicaciones[7].split('; ')[2]} y es de género {lista_publicaciones[7].split('; ')[3]}.")
