import csv
import os

"""
titulo,autor,editorial,anio
El Aleph,Jorge Luis Borges,Emece,1949
El Quijote,Miguel de Cervantes,Alfaguara,2005
El desbarrancadero,Fernando Vallejo,Planeta,2001
Una novelita Lumpen,Roberto Bolaño,Anagrama,2002
El amante,Marguerite Duras,Tusquets,1984
"""

""" with open(os.path.join(os.getcwd(), "inventario.csv"), 'w', encoding = 'utf-8', newline="") as archivo:
    tabla = csv.writer(archivo)
    tabla.writerow(['titulo','autor','editorial','anio'])
    tabla.writerow(['El Aleph','Jorge Luis Borges','Emece','1949'])
    tabla.writerow(['El Quijote','Miguel de Cervantes','Alfaguara','2005'])
    tabla.writerow(['El desbarrancadero', 'Fernando Vallejo', 'Planeta', 2001])

     """

""" inventario = [
    ["titulo", "autor", "editorial", "anio"],
    ['El Aleph','Jorge Luis Borges','Emece','1949'],
    ['El Quijote','Miguel de Cervantes','Alfaguara','2005'],
    ['El desbarrancadero', 'Fernando Vallejo', 'Planeta', 2001],
    ['Una novelita lumpen', 'Rberto Bolaño', 'Anagrama', 2002]
]

with open(os.path.join(os.getcwd(), "inventario2.csv"), 'w', encoding = 'utf-8', newline="") as archivo:
    writer = csv.writer(archivo)
    for fila in inventario:
        writer.writerow(fila) """

""" with open(os.path.join(os.getcwd(), "inventario2.csv"), 'r') as archivo:
    reader = csv.reader(archivo)
    for fila in reader:
        print(fila) """


""" nuevo_libro = input("Agrega el título del libro: ")
nuevo_autor = input("Agrega el autor: ")
nueva_editoria = input("Agrega la editorial: ")
nuevo_anio = input("Agrega el año de publicación: ")

with open(os.path.join(os.getcwd(), "inventario2.csv"), 'a', encoding='utf-8') as archivo:
    writer = csv.writer(archivo)
    writer.writerow([nuevo_libro, nuevo_autor, nueva_editoria, nuevo_anio])

with open(os.path.join(os.getcwd(), "inventario2.csv"), 'r', encoding='utf-8') as archivo:
    reader = csv.DictReader(archivo)
    for fila in reader:
        print(fila['autor'])
        print(fila['titulo'])
        print(fila['editorial'])
        print(fila['anio']) """

inventario = [
    {"titulo": "El Aleph", "autor": "Jorge Luis Borges", "editorial": "Emece", "anio": 1949},
    {"titulo": "El Quijote", "autor": "Miguel de Cervantes", "editorial": "Alfaguara", "anio": 2005},
    {"titulo": "El desbarrancadero", "autor": "Fernando Vallejo", "editorial": "Planeta", "anio": 2001},
    {"titulo": "Una novelita Lumpen", "autor": "Roberto Bolaño", "editorial": "Anagrama", "anio": 2002},
    {"titulo": "El amante", "autor": "Marguerite Duras", "editorial": "Tusquets", "anio": 1984},
]

with open(os.path.join(os.getcwd(), "inventario3.csv"), 'w', encoding='utf-8') as archivo:
    writer = csv.DictWriter(archivo, fieldnames=['titulo', 'autor', 'editorial', 'anio'])
    writer.writeheader()
    for libro in inventario:
        writer.writerow(libro)

with open(os.path.join(os.getcwd(), "inventario3.csv"), 'r', encoding='utf-8') as archivo:
    reader = csv.DictReader(archivo)
    for fila in reader:
        for k, v in fila.items():
            print(v)
