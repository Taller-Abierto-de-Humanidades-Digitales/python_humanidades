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


#print(bibliografia["001"]["autor"][0]['nombre'])

# (clave, valor)

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

    if len(l.split("; ")[0].split(" ")) > 2:
        nombre = l.split("; ")[0].split(" ")[:2]
    else:
        nombre = l.split("; ")[0].split(" ")[0]

    bibliografia[clave] = {
        "tipo": "libro",
        "autor": [
             {'nombre':nombre,'apellido': l.split(';')[1].split(' ')[-1]}
        ],
        "titulo": l.split("; ")[1],
        "editorial": l.split("; ")[-1],
        "fecha": int(l.split("; ")[2]),
        "lugar": ""
    }




lugares = {
    "006": "Madrid",
    "007": "Madrid",
    "008": "Madrid",
    "009": "México",
    "010": "Nueva York"
}

for clave, valor in lugares.items():
    bibliografia[clave]['lugar'] = valor

for clave, valor in bibliografia.items():
    print(clave)
    print(valor)