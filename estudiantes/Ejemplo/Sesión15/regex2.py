import os
import re

archivo = os.path.join(os.getcwd(), "archivos", "txt", "el_quijote.txt")
with open(archivo, "r", encoding="utf-8") as f:
    texto = f.read()

# findall

busqueda = re.findall(r"\bA[a-ü]+\b", texto)

# search

busqueda2 = re.search(r"\bA[a-ü]+\b", texto)
""" print(busqueda2.group())
print(texto[busqueda2.start()-50:busqueda2.end()+50]) """

# match

email = "jairo_antoniomelo@filos.unam.mx.co"

busqueda3 = re.match(r"^[a-zA-Z0-9.!#$%&'*+\/=?^_`{|}~-]+@[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?(?:\.[a-zA-Z0-9](?:[a-zA-Z0-9-]{0,61}[a-zA-Z0-9])?)*$", email)

# método group
# función compile

nombre = "JAiro MeLo FLórez"
patron = re.compile(r"([A-Z][a-ü]+)\s([A-Z][a-ü]+(?:\s[A-Z][a-ü]+)*)")

# función sub

""" if not re.match(patron, nombre):
    nombre_correcto = re.sub(
        r"([A-Z])([A-Za-ü]+)\b",
        lambda match: match.group(1) + match.group(2).lower(),
        nombre
    )
    coincidencia = re.match(patron, nombre_correcto)

    if coincidencia:
        print("Nombre: ", coincidencia.group(1))
        print("Apellidos: ", coincidencia.group(2))
    else:
        print("El nombre no es válido") """

fecha = "La fecha actual es 2023-05-16"

fecha = re.sub(r"(\d{4})-(\d{2})-(\d{2})", r"\3-\2-\1", fecha)
#print(fecha)

# split

palabras = re.split(r"\W+", texto)
#print(palabras[:100])

# finditer

saltos_de_linea = re.finditer(r"\n[a-ü]+\b", texto) # encuentra todos los saltos de línea que van seguidos de una minúscula, por tanto, incorrectos
contador = 0
for s in saltos_de_linea:
    contador += 1

print(f"La cantidad de saltos de línea incorrectos es de {contador}")

texto = re.sub(r"\n([a-ü]+)\b", r"\1", texto) # corrige esos saltos de línea incorrectos

saltos_de_linea = re.finditer(r"\n[a-ü]+\b", texto)
contador = 0
for s in saltos_de_linea:
    contador += 1

print(f"La cantidad de saltos de línea incorrectos es de {contador}") # comprobación