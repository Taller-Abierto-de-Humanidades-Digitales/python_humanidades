""" diccionario = {
   # "clave" : "valor"
    2: 258 , 
    5.2 : ["valor2", "valor3", "valor4"]
    "d": 
    {"clave": "valor anidado", "clave2"}

    "clave2": "valor2"
    "clave3": "valor3"
}
print (diccionario) """

protagonistas = {
    "Jerry" : "Jerry Seinfeld",
    "George" : 
    {"nombre": "Jason Alexander"},
    "Elaine" : "Julia Louis",
    "Kramer" : {
            "Nombre" :"Michael Richards",
            "año_nacimiento": 1949,
            "nacionalidad": "estadounidense",
            "género" : "masculino",
            }
    }
if protagonistas:
    print(protagonistas["Kramer"]["nacionalidad"])
else: 
    print ("no hay elementos en el dicc")

protagonistas["George"]["Empleos"] = ["propiedades", "sanalac", "publicista"]
for l in protagonistas['George']['Empleos']:
    print(l.upper())
del protagonistas['George']['Empleos'] 
#para borrar del+ el dicc + la clave a eliminar

#iterar a través de un diccionario
bibliografia = {
    "001": {
        "tipo": "libro",
        "autor": [{"nombre": "Martin", "apellido": "Heidegger"}],
        "titulo": "Ser y tiempo",
        "editorial": "Trotta",
        "lugar": "Madrid",
        "fecha": 2003
    },
    "002": {
        "tipo": "libro",
        "autor": [{"nombre": "Fernand", "apellido": "Braudel"}],
        "titulo": "El Mediterráneo y el mundo mediterráneo en la época de Felipe II",
        "editorial": "Fondo de Cultura Económica",
        "lugar": "México",
        "fecha": 2022,
        "edicion": "tercera"
    },
    "003": {
        "tipo": "libro",
        "autor": [{"nombre": "Hans-Georg", "apellido": "Gadamer"}],
        "titulo": "Verdad y método I: fundamentos de una hermenéutica filosófica",
        "editorial": "Sígueme",
        "lugar": "Salamanca",
        "fecha": 1996
    },
    "004": {
        "tipo": "libro",
        "autor": [{"nombre": "Giorgio", "apellido": "Agamben"}],
        "titulo": "Estado de excepción",
        "editorial": "Adriana Hidalgo Editora",
        "lugar": "Buenos Aires",
        "fecha": 2010
    },
    "005": {
        "tipo": "libro",
        "autor": [{"nombre": "Ludwig", "apellido": "Wittgenstein"}],
        "titulo": "Zettel",
        "editorial": "University of California Press",
        "lugar": "Berkeley",
        "fecha": 1970,
        "idioma": "en"
    }
}

print(bibliografia["001"]["autor"][0]['nombre'])

for c in bibliografia: 
    print(c)

""" #clave,valor
for clave, valor in bibliografia.items():
    print (f"clave: {clave} | valor: {valor}")

for clave, valor in bibliografia.items():
    if valor [] """

#terminar con la foto

#otro ejercicio de agregar
lista_bibliografia = [
    "Edgar Alan Poe; Cuentos completos; 2019; Alianza Editorial",
    "David Hume; Del conocimiento; 1984; Aguilar",
    "Ludwig Wittgenstein; Tractatus Logico-Philosophicus; 2017; Tecnos",
    "Francois Hartog; Cronos; 2022; Siglo XXI",
    "David Spiegelhalter; The art of statistics; 2021; Basic Books"
]
for l in lista_bibliografia:
    clave = int(list(bibliografia.keys())[-1]) + 1
    clave = str(clave).zfill(3)
    bibliografia(clave) = {
        "tipo":"libro"
        "autor":"[
        {"nombre": 1.split("; ")[0].split(" ")[0], "apellido": l.split("; ")[0].split(" ")[-1]}
    }

    print(clave)

