# Catalogo

libros = ['Cuentos completos 1; Isaac Asimov; 2009; Ficción', 'Cuentos completos 2; Isaac Asimov; 2009; Ficción', 'De Animales a Dioses; Yuval Noah Harari; 2015; Historia General', 'Homo Deus; Yuval Noah Harari; 2016; Historia General', 'Prohibido Nacer; Trevor Noah; 2017; Autobiografía', 'Somos Luces Abismales; Carolina Sanín; 2018; Ensayos Literarios', 'Muerte con Pingüino; Andrei Kurkov; 1996; Novela', 'Que Viva la Música!; Andrés Caicedo; 1977; Novela']

lis_ani_libros = []
len_nombres = []

for libro in libros:
    lis_ani_libros.append(libro.split(';'))

for nombre in lis_ani_libros:
    len_nombres.append(len(nombre[0]))

promedio = sum(len_nombres) / len(len_nombres)

print(f"El promedio de caracteres de los títulos de mi catálogo es: {round(promedio,1)}")