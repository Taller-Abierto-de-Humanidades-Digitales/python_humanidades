import os
import csv


""" with open(os.path.join(os.getcwd(), "escena.csv"), 'w', encoding = 'utf-8', newline="") as archivo:
    tabla = csv.writer(archivo) """



with open(os.path.join(os.getcwd(), "escenas.csv"), "r", encoding = 'utf-8', newline="") as archivo:
    reader = csv.DictReader(archivo)
    for fila in reader:
        print(fila)
        break


with open(os.path.join(os.getcwd(), "escena.csv"), 'w', encoding = 'utf-8', newline="") as archivo:
    tabla = csv.writer(archivo)
    tabla.writerow(['titulo','autor','productora','anio'])
    tabla.writerow(['bajo el cielo antioquenio','Arturo Acevedo','Filmadora antioquia','1925'])
 
 
 
 
nueva_peli = input("Agrega el título de la pelícua: ")
nuevo_direct = input("Agrega el director: ")
nueva_produ = input("Agrega la productora: ")
nuevo_anio = input("Agrega el año de publicación: ")


with open(os.path.join(os.getcwd(), "escena.csv"), 'a', encoding='utf-8') as archivo:
    writer = csv.writer(archivo)
    writer.writerow([nueva_peli, nuevo_direct, nueva_produ, nuevo_anio])
 


