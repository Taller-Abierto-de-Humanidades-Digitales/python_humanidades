#Ejercicio 1
libros= ['Walter Rudin; Real and Complex Analysis; 1966; Matemáticas', 'Stefan Banach; Théorie des opérations linéaires; 1932; Matemáticas', 'Stan Wagon; The Banach-Tarski Paradox; 1985; Matemáticas', "Gregory Moore; Zermelo's Axiom of Choice; 1982; Historia", 'Andrei Kolmogorov; Grundbegriffe der Wahrscheinlichkeitsrechnung; 1933; Matemáticas', "Frigyes Riesz; Functional Analysis; 1955; Matemáticas", "Edmund Husserl; Ideen zu einer reinen Phänomenologie und phänomenologischen Philosophie; 1913; Filosofía", "Andrei Kolmogorov; Teoría de Probabilidad; 1933; Matemáticas"]

#Búsqueda de títulos con palabra clave
kulcsszó="analysis"
resultados=[]

for libro in libros:
    if kulcsszó.lower() in libro.lower():
        resultados.append(libro)
if resultados == []:
    print(f"La palabra \"{kulcsszó}\" no se encontró en ningún elemento.")
else:
    print(f"La palabra \"{kulcsszó}\" se encontró en:")
    for i in range(len(resultados)):
        print(f" {resultados[i].split('; ')[1]} de {resultados[i].split('; ')[0]}, "\
              f"cuyo género es {resultados[i].split('; ')[3]}.")

#Ejercicio 2

fechafiltro=2040
deseo="anteriores"
libros_fechas_anteriores=[]
libros_fechas_posteriores=[]

for libro in libros:
    if deseo.lower() == "anteriores":
        if int(libro.split("; ")[2])<fechafiltro:
            libros_fechas_anteriores.append(libro)
    elif deseo.lower() == "posteriores":
        if int(libro.split("; ")[2])>=fechafiltro:
            libros_fechas_posteriores.append(libro)
import datetime

fecha = datetime.date.today()
año = fecha.strftime("%Y")  #Extrae el año actual del sistema


if deseo.lower()=="anteriores":
        if libros_fechas_anteriores!=[]:
             print(f"Los libros anteriores a {fechafiltro} son:")
             for i in range(len(libros_fechas_anteriores)):
              print(f"{libros_fechas_anteriores[i].split('; ')[1]} de {libros_fechas_anteriores[i].split('; ')[0]}, publicado en {libros_fechas_anteriores[i].split('; ')[2]}.")
        else:
            print(f"No hay libros publicados en fechas anteriores a {fechafiltro}.")
elif deseo.lower() == "posteriores":
        if fechafiltro<int(año): #Revisa que no sean libros posteriores a un año futuro
            if libros_fechas_posteriores!=[]:
             print(f"Los libros posteriores a {fechafiltro} son:")
             for i in range(len(libros_fechas_posteriores)):
              print(f"{libros_fechas_posteriores[i].split('; ')[1]} de {libros_fechas_posteriores[i].split('; ')[0]}, publicado en {libros_fechas_posteriores[i].split('; ')[2]}.")
            else:
                print(f"No hay libros publicados en fechas posteriores a {fechafiltro}.")

        else:
             print(f"El año indicado es inválido.")



#Ejercicio 3

género="filosofía"
resultadosg=[]

for libro in libros:
    if género.lower() == libro.split("; ")[-1].lower():
        resultadosg.append(libro)

if resultadosg == []:
    print(f"Ningún libro es del género \"{género}\".")
else:
    print(f"Los libros cuyo género es \"{género}\" son:")
    for i in range(len(resultadosg)):
        print(f" {resultadosg[i].split('; ')[1]} de {resultadosg[i].split('; ')[0]}.")

#Ejercicio 4

matemáticas=[]
filosofía=[]
otros=[]

for libro in libros:
    if libro.split("; ")[3].lower()=="filosofía":
        filosofía.append(libro)
    elif libro.split("; ")[3].lower()=="matemáticas":
        matemáticas.append(libro)
    else:
        otros.append(libro)

if matemáticas == []:
    print("No hay libros de género \"Matemáticas\".")
else:
    print("Libros de matemáticas:")
    for i in range(len(matemáticas)):
        print(f"- <{matemáticas[i].split('; ')[0]}>, <{matemáticas[i].split('; ')[1]}> (<{matemáticas[i].split('; ')[2]}>), <{matemáticas[i].split('; ')[3]}>")

if matemáticas == []:
    print("No hay libros de género \"Filosofía\".")
else:
    print("Libros de filosofía:")
    for i in range(len(filosofía)):
        print(f"- <{filosofía[i].split('; ')[0]}>, <{filosofía[i].split('; ')[1]}> (<{filosofía[i].split('; ')[2]}>), <{filosofía[i].split('; ')[3]}>")

if otros == []:
    print("No hay libros de género \"Otros\".")
else:
    print("Otros:")
    for i in range(len(otros)):
        print(f"- <{otros[i].split('; ')[0]}>, <{otros[i].split('; ')[1]}> (<{otros[i].split('; ')[2]}>), <{otros[i].split('; ')[3]}>")
    

#Ejercicio 5

result=[] 

autor="kolmogorov" 

fecha="1933"  

validor=False 
validor2=False

for libro in libros: 

    if autor.lower() in libro.split("; ")[0].lower():
        validor=True
        if fecha==libro.split("; ")[-2]:
            validor2=True
            result.append(libro) 

if result != []:
    print(f"Libros de {result[0].split('; ')[0]} publicados en {fecha}:")
    for i in range(len(result)): 
        print(f"- <{result[i].split('; ')[1]}>, <{result[i].split('; ')[3]}>") 
elif validor2==False and validor==True:
    print(f"Sí hay libros con tal autor, pero ninguno coincide con la fecha")
else:
    print("No hay libros con ese autor") 