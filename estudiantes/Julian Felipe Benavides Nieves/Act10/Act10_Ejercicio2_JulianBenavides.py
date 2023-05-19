## ACTIVIDAD 10 - Ejercicio 2 - Escribir nueva bibliografia en el archivo CSV

import csv
import os
import json


print('Agrege los datos de la nuevo elemento bibliográfico: ')
n_libro = input('Agregar nuevo titulo:')
n_autor = input('Agregar nuevo autor:')
n_editorial = input('Agregar nuevo editorial:')
n_anio = input('Agregar nuevo año:')


with open(os.path.join(os.getcwd(), "estudiantes/Julian Felipe Benavides Nieves/Act10", "bibliografiatest.csv"),'a', encoding = 'utf-8', newline="" ) as archivo:
    tabla = csv.writer(archivo)
    tabla.writerow([n_libro,n_autor,n_editorial,n_anio])


biblio_csv = []

with open(os.path.join(os.getcwd(), "estudiantes/Julian Felipe Benavides Nieves/Act10", "bibliografiatest.csv"),'r', encoding = 'utf-8', newline="" ) as archivo:
    lista_biblo = csv.DictReader(archivo)
    for libro in lista_biblo:
        biblio_csv.append(libro)

print(f"Ahora la tabla tiene {len(biblio_csv)} entradas")