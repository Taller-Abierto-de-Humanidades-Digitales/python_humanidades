lista_publicaciones = ['Kawabata, Yasunari; País de nieve; 1948; Novela', 'Woolf, Virginia; La señora Dalloway; 1925; Novela', 'Caicedo, Andrés; ¡Que viva la música!; 1977; Novela', 'de Saint-Exupery, Antoine; El Principito; 1943; Novela', 'Dostoiewski, Fedor; Pobres gentes; 1846; Novela', 'Mendoza, Mario; La importancia de morir a tiempo; 2012; Novela', 'García, Luis; I took Panama; 1973; Teatro', 'Caicedo, Andrés; Destinos fatales; 1984; Cuento']

titulos = [lista_publicaciones[0].split('; ')[1], lista_publicaciones[1].split('; ')[1], lista_publicaciones[2].split('; ')[1], lista_publicaciones[3].split('; ')[1], lista_publicaciones[4].split('; ')[1], lista_publicaciones[5].split('; ')[1], lista_publicaciones[6].split('; ')[1], lista_publicaciones[7].split('; ')[1]]

print(titulos)

titulos.sort()
#print(titulos)
print(titulos[0:2])

titulos.sort(reverse=True)
#print(titulos)
print(titulos[0:2])