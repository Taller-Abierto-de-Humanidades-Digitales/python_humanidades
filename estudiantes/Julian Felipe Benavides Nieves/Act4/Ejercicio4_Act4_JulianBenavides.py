# Catalogo

libros = ['Cuentos completos 1; Isaac Asimov; 2009; Ficción', 'Cuentos completos 2; Isaac Asimov; 2009; Ficción', 'De Animales a Dioses; Yuval Noah Harari; 2015; Historia General', 'Homo Deus; Yuval Noah Harari; 2016; Historia General', 'Prohibido Nacer; Trevor Noah; 2017; Autobiografía', 'Somos Luces Abismales; Carolina Sanín; 2018; Ensayos Literarios', 'Muerte con Pingüino; Andrei Kurkov; 1996; Novela', 'Que Viva la Música!; Andrés Caicedo; 1977; Novela']

lis_ani_libros = []
anios = []

for libro in libros:
    lis_ani_libros.append(libro.split(';'))

# print(lis_ani_libros)

for anio in lis_ani_libros:
    anios.append(int(anio[2]))

print(anios)
print(len(anios))

promedio = sum(anios) / len(anios)

print(f"La fecha promedio de los libros de mi catálogo es: {round(promedio)}")