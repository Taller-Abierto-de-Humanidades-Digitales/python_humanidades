## ACTIVIDAD 10 - Crear archivo CSV desde diccionario

import csv
import os
import json

ruta_biblio_json = os.path.join(os.getcwd(), "data", "bibliografia.json")

print(ruta_biblio_json)

if os.path.exists(ruta_biblio_json):
    print("ok")
else:
    print("error")

with open(ruta_biblio_json, "r", encoding='utf-8') as archivo:
    bibliografia = json.load(archivo)

bibliografia_limpia = []

claves_a_verificar = ["issued", "title", "publisher", "author"]

for elemento in bibliografia:
    if all(clave in elemento for clave in claves_a_verificar):
        elemento_nuevo = {}
        elemento_nuevo = {'issued' : elemento['issued'], 'title': elemento['title'], 'author': elemento['author'],'publisher' : elemento['publisher']}
        bibliografia_limpia.append(elemento_nuevo)
    
                                  
print(len(bibliografia_limpia))


with open(os.path.join(os.getcwd(), "estudiantes/Julian Felipe Benavides Nieves/Act10", "bibliografiatest.csv"),'w', encoding = 'utf-8', newline="" ) as archivo:
    tabla = csv.DictWriter(archivo, fieldnames=["issued", "title", "publisher", "author"])
    tabla.writeheader()
    for libro in bibliografia_limpia:
        tabla.writerow(libro)


biblio_csv = []

with open(os.path.join(os.getcwd(), "estudiantes/Julian Felipe Benavides Nieves/Act10", "bibliografiatest.csv"),'r', encoding = 'utf-8', newline="" ) as archivo:
    lista_biblo = csv.DictReader(archivo)
    for libro in lista_biblo:
        biblio_csv.append(libro)

print(len(biblio_csv))
