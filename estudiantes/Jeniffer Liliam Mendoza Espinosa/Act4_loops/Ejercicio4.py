#Ejercicio 4: Calcula la fecha promedio de los libros de tu catálogo

libros = ['Vallejo, Irene; El infinito en un junco; 2021', 'de Saint-Exupery, Antoine; El Principito; 1943', 'Dostoiewski, Fedor; Pobres gentes; 1846', 'Mistral, Gabriela; Sonetos de la muerte; 1915', 'García, Luis; I took Panama; 1973', 'Bonnet, Piedad; Explicaciones no pedidas; 2011', 'Restrepo, Laura; Hot sur; 2012', 'Abad, Héctor; El olvido que seremos; 2006']
#print(len(libros))
anios = []


for libro in libros:
    anios.append(int(libro.split('; ')[2]))
print(anios)
    
promedio_fecha = sum(anios)/len(anios)
print(f"La fecha promedio de los libros de mi catálogo es: {round(promedio_fecha, 0)}.")
print(f"La fecha promedio de los libros de mi catálogo es: {int(promedio_fecha)}.")