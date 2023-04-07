catalogo=["Harry Potter y la piedra filosofal; J. K. Rowling; 1997; Ficción", "Mi hombre Seducción; Jodi Ellen Malpas; 2012; Novela erótica", "El código Da Vinci; Dan Brown; 2003; Novela", "La cupula; Stephen King; 2017; Novela", "Los hombres que no amaban a las mujeres; Stieg Larsson; 2011; Misterio"]

#Ejercicio-----------------------4

anios = []   

for anitos in catalogo:
    anios.append(int(anitos.split("; ")[2]))

fecha_promedio = sum(anios) / len(anios)

print(f"La fecha promedio de los libros de mi catálogo es: {fecha_promedio}")



#Ejercicio-----------------------5

titulos = []
longitud = []
for titulo in catalogo:
    titulos.append(titulo.split("; ")[0])

for nombres in titulos:
    longitud.append(len(nombres))

promedio = sum(longitud) / len(longitud)    
    
print(f"El promedio de caracteres de los títulos de mi catálogo es:{promedio}")


