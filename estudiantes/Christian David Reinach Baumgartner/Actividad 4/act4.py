#Ejercicio 1
libros= ['Walter Rudin; Real and Complex Analysis; 1966; Matemáticas', 'Stefan Banach; Théorie des opérations linéaires; 1932; Matemáticas', 'Stan Wagon; The Banach-Tarski Paradox; 1985; Matemáticas', "Gregory Moore; Zermelo's Axiom of Choice; 1982; Matemáticas", 'Andrei Kolmogorov; Grundbegriffe der Wahrscheinlichkeitsrechnung; 1933; Matemáticas']

#Separar por categorías

autores = [num.split("; ")[0] for num in libros]
títulos = [num.split("; ")[1] for num in libros]
años = [num.split("; ")[2] for num in libros]
géneros = [num.split("; ")[3] for num in libros]

print(autores, títulos, años, géneros) 

#Ejercicio 2

lista_nuevos=["Donald Cohn; Measure Theory; 2015; Matemáticas", "Frigyes Riesz; Functional Analysis; 1955; Matemáticas", "Bernt Øksendal; Stochastic Differential Equations; 1982; Matemáticas"]
#Añadir nuevos libros a la lista general
libros.extend(lista_nuevos)


#Ejercicio 3 #Para este ejercicio uso la función rstrip() [que encontré en internet] para eliminar el último "; ".
for i in range(len(libros)):
    libros[i]=libros[i].replace(libros[i].split(";").pop(),"").rstrip(";")
print(libros)


#Ejercicio 4
años = [num.split("; ")[2] for num in libros]

suma=0 #Inicializo un sumador
for i in años:
    suma+=int(i)
fechapromedio=int(suma/len(años)) #Calcula el promedio y elimina la parte decimal

print(f"La fecha promedio de publicación es {fechapromedio}.")

#Ejercicio 5
títulos = [num.split("; ")[1] for num in libros]
longitudes=[len(num) for num in títulos] #Lista con cantidad de caracteres de los títulos de mi catálogo

sumacaracteres=0
for j in longitudes:
    sumacaracteres+=j
longitudpromedio=int(sumacaracteres/len(longitudes)) #Calcula el promedio y elimina la parte decimal

print(f"El promedio de caracteres de los títulos de mi catálogo es: {longitudpromedio}")


