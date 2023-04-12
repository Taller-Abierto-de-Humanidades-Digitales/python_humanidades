#Ejercicio 5: Calcula el promedio de caracteres de los títulos de tu catálogo

libros = ['Vallejo, Irene; El infinito en un junco; 2021', 'de Saint-Exupery, Antoine; El Principito; 1943', 'Dostoiewski, Fedor; Pobres gentes; 1846', 'Mistral, Gabriela; Sonetos de la muerte; 1915', 'García, Luis; I took Panama; 1973', 'Bonnet, Piedad; Explicaciones no pedidas; 2011', 'Restrepo, Laura; Hot sur; 2012', 'Abad, Héctor; El olvido que seremos; 2006']
titulos = []
longitud = []

for libro in libros:
    titulo = libro.split("; ")[1]
    titulos.append(titulo)
    longitud.append(len(titulo))
#print(longitud)

promedio_titulo = sum(longitud)/len(longitud)
print(f"El promedio de caracteres de los títulos de mi catálogo es: {round(promedio_titulo,1)}.")

