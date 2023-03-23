#DICCIONARIO 

katalog1={'001': {'tipo': 'libro', 'autor': [{'nombre': 'Walter', 'apellido': 'Rudin'}], 'titulo': 'Real and Complex Analysis', 'editorial': 'McGraw-Hill', 'fecha': 1966, 'lugar': 'Nueva York'}, '002': {'tipo': 'libro', 'autor': [{'nombre': 'Stefan', 'apellido': 'Banach'}], 'titulo': 'Théorie des opérations linéaires', 'editorial': 'Instytut Matematyczny Polskiej Akademii Nauk', 'fecha': 1932, 'lugar': 'Varsovia'}, '003': {'tipo': 'libro', 'autor': [{'nombre': 'Stan', 'apellido': 'Wagon'}], 'titulo': 'The Banach-Tarski Paradox', 'editorial': 'Cambridge University Press', 'fecha': 1985, 'lugar': 'Nueva York'}, '004': {'tipo': 'libro', 'autor': [{'nombre': 'Gregory', 'apellido': 'Moore'}], 'titulo': "Zermelo's Axiom of Choice", 'editorial': 'Springer-Verlag', 'fecha': 1982, 'lugar': 'Nueva York'}, '005': {'tipo': 'libro', 'autor': [{'nombre': 'Andrei', 'apellido': 'Kolmogorov'}], 'titulo': 'Grundbegriffe der Wahrscheinlichkeitsrechnung', 'editorial': 'Springer', 'fecha': 1933, 'lugar': 'Berlín'}, '006': {'tipo': 'libro', 'autor': [{'nombre': 'Donald', 'apellido': 'Cohn'}], 'titulo': 'Measure Theory', 'editorial': 'Birkhäuser', 'fecha': 2015, 'lugar': 'Nueva York'}, '007': {'tipo': 'libro', 'autor': [{'nombre': 'Frigyes', 'apellido': 'Riesz'}], 'titulo': 'Functional Analysis', 'editorial': 'Dover Publications', 'fecha': 1955, 'lugar': 'Nueva York'}, '008': {'tipo': 'libro', 'autor': [{'nombre': 'Bernt', 'apellido': 'Øksendal'}], 'titulo': 'Stochastic Differential Equations', 'editorial': 'Springer', 'fecha': 1982, 'lugar': 'Oslo'}, '009': {'tipo': 'artículo científico', 'autor': [{'nombre': 'James', 'apellido': 'Herbert'}], 'titulo': "Turner's Uncertain Angel", 'fecha': 2011, 'revista': 'The Journal of Religion', 'volumen': '91', 'número': '4', 'url': 'https://www.journals.uchicago.edu/doi/abs/10.1086/660904?journalCode=jr'}, '010': {'tipo': 'artículo científico', 'autor': [{'nombre': 'Philipp', 'apellido': 'Metzner'}, {'nombre': 'Lars', 'apellido': 'Putzig'}, {'nombre': 'Illia', 'apellido': 'Horenko'}], 'titulo': 'Analysis of Persistent Nonstationary Time Series and Applications', 'fecha': 2012, 'revista': 'Communications in Applied Mathematics and Computational Science', 'volumen': '7', 'número': '2', 'url': 'https://projecteuclid.org/journals/communications-in-applied-mathematics-and-computational-science/volume-7/issue-2/Analysis-of-persistent-nonstationary-time-series-and-applications/10.2140/camcos.2012.7.175.full'}, '011': {'tipo': 'artículo científico', 'autor': [{'nombre': 'Aihua', 'apellido': 'Zhang'}, {'nombre': 'Chen', 'apellido': 'Chen'}, {'nombre': 'Hamid', 'apellido': 'Karimi'}], 'titulo': 'A New Adaptive LSSVR with Online Multikernel RBF Tuning to Evaluate Analog Circuit Performance', 'fecha': 2013, 'revista': 'Abstract and Applied Analysis', 'volumen': '2013', 'número': 'sin número', 'url': 'https://www.hindawi.com/journals/aaa/2013/231735/'}, '012': {'tipo': 'artículo de prensa', 'autor': [{'nombre': 'Esther', 'apellido': 'Felden'}], 'titulo': 'Wie China seine Top-Studenten in Deutschland kontrolliert', 'fecha': 2023, 'periódico': 'Deutsche Welle', 'sección': 'Investigación', 'url': 'https://p.dw.com/p/4OIIU'}, '013': {'tipo': 'artículo de prensa', 'autor': [{'nombre': 'Shlomit', 'apellido': 'Lasky'}], 'titulo': 'Metropolitan Museum benennt Gemälde von Degas um', 'fecha': 2023, 'periódico': 'Deutsche Welle', 'sección': 'Kunst in Kriegszeiten', 'url': 'https://p.dw.com/p/4NbtC'}, '014': {'tipo': 'vídeo de YouTube', 'titulo': 'Double Pendulum Chaos Demonstration', 'canal': 'Izaak Weiss', 'fecha': 2016, 'url': 'https://youtu.be/pEjZd-AvPco'}}

""" --------------------------------------------------------------------------------------------------------------------------EJERCICIO 1: BÚSQUEDA EN UN CATÁLOGO POR PALABRA CLAVE
-------------------------------------------------------------------------------------------------------------------------- """

def busqueda(katalog):
    """Busca un elemento del catálogo por pertenencia de una palabra clave en el título. No busca pertenencia de cadena de caracteres.

    Parámetros
    ----------
    katalog: dict
    (el catálogo en el que se desea buscar)"""
    schlussel=input("Ingrese la palabra con la que desea filtrar el catálogo por título:")
    vysledek=[]
    for buch in katalog:
            for i in katalog[buch]['titulo'].split(' '):
                if schlussel.lower() == i.lower():
                    vysledek.append(katalog[buch]['titulo'])
            
    if len(vysledek)!=0:
            print(f"La palabra arroja {len(vysledek)} resultado(s):")
            for vys in vysledek:
                print(f" -- {vys}")
    else:
        print(f"La palabra ingresada no arroja ningún resultado. Por favor, intente de nuevo.")


#busqueda(katalog1)


""" --------------------------------------------------------------------------------------------------------------------------EJERCICIO 2: BÚSQUEDA EN UN CATÁLOGO POR PALABRA CLAVE Y FECHA DE PUBLICACIÓN
-------------------------------------------------------------------------------------------------------------------------- """
def especifica(katalog):
    """ Busca un título del catálogo por palabra clave y fecha de publicación.
     
     Parámetros
     ----------
     katalog: dict
     (el catálogo en el que se desea buscar)"""
    datumy=[katalog[m]['fecha'] for m in katalog]
    klíčové=input("Ingrese la palabra con la que desea filtrar la búsqueda:")
    datum=input("Ingrese el año de publicación de interés (AAAA):")
    
    vysledek2=[]
    valitor1=False
    valitor2=False
    valitor3=False
    valitor4=False

    if int(datum)<min(datumy) or int(datum)>max(datumy):
         print(f"La fecha ingresada debe estar entre {min(datumy)} y {max(datumy)}.")

    else:        

        try:
            for buch in katalog:
                for i in katalog[buch]['titulo'].split(' '):
                    if klíčové.lower() == i.lower() and int(datum)==katalog[buch]['fecha']: 
                                valitor1=True                      
                                vysledek2.append(katalog[buch]['titulo'])
                    elif klíčové.lower() == i.lower() and int(datum)!=katalog[buch]['fecha']:
                        valitor2=True
                    elif klíčové.lower() != i.lower() and int(datum)==katalog[buch]['fecha']:
                        valitor3=True
                    elif klíčové.lower() != i.lower() and int(datum)!=katalog[buch]['fecha']:
                        valitor4=True
        except ValueError:
            print(f"Vuelva a intentar e ingrese un año en formato adecuado (AAAA)")


        
        if valitor1 == True:
            print(f"Se arrojan {len(vysledek2)} resultado(s):")
            for l in vysledek2:
                print(f" -- {l}.")
        elif valitor2 == True:
            print(f"La fecha ingresada no coincide con ninguno de los títulos que contienen a \"{klíčové}\". Intente de nuevo.")
        elif valitor3 == True:
            print(f"La fecha ingresada coincide con algun(os) título(s), pero la palabra \"{klíčové}\" no está en ninguno. Intente de nuevo.")
        elif valitor4 == True:
            print("No se arrojan resultados con esa palabra clave y fecha. Intente de nuevo.")

#especifica(katalog1)
         
""" --------------------------------------------------------------------------------------------------------------------------EJERCICIO 3: FUNCIÓN QUE AÑADE ELEMENTOS A UN CATÁLOGO
-------------------------------------------------------------------------------------------------------------------------- """
def añadir(katalog):
     tipo=input("Ingrese el tipo de elemento que desea añadir (conserve los acentos):")
     tipos=[katalog[buch]['tipo'].lower() for buch in katalog]
     depuredtipos=list(set(tipos))
     elemento={}
     if tipo.lower() in depuredtipos:
            for n in katalog:
                 if katalog[n]['tipo'].lower()== tipo.lower():
                    categorias=list(katalog[n].keys())
                    tamaño=len(categorias)
                    break
            clave = int(list(katalog.keys())[-1]) + 1
            clave = str(clave).zfill(3)
            for m in range(tamaño-1):                 
                 elemento[categorias[m+1]]=input(f"Ingrese {categorias[m+1]}:")
            katalog[clave] = elemento
            print("Elemento añadido al catálogo exitosamente.")
     else:
          print("No hay elementos del tipo ingresado; por ahora no podemos crear uno nuevo, pero esperamos hacerlo pronto :)")       
                 
añadir(katalog1)

print(katalog1)