import os
import json

origen = os.path.join(os.getcwd(), "data/bibliografia.json")
destino = os.path.join(os.getcwd(), "estudiantes/Ejemplo/Sesión13/json")
os.makedirs(destino, exist_ok=True)

with open(origen, "r", encoding="utf-8") as archivo:
    bibliografia = json.load(archivo)

libro = {
  "id": "http://zotero.org/users/163570/items/DFIAXHAZ",
  "type": "book",
  "event-place": "Madrid",
  "ISBN": "978-84-460-0264-2",
  "language": "Spanish",
  "note": "OCLC: 40162792",
  "publisher": "Akal",
  "publisher-place": "Madrid",
  "source": "Open WorldCat",
  "title": "El problema de la incredulidad en el siglo XVI: la religión de Rabelais",
  "title-short": "El problema de la incredulidad",
  "author": [
   {
    "family": "Febvre",
    "given": "Lucien"
   }
  ],
  "translator": [
   {
    "family": "Balsinde",
    "given": "Isabel"
   }
  ],
  "issued": {
   "date-parts": [
    [
     "1993"
    ]
   ]
  }
 }

# actualizar JSON

bibliografia.append(libro)

with open(os.path.join(destino, "bibliografia.json"), "w", encoding='utf-8') as guardar:
    json.dump(bibliografia, guardar)

titulo_eliminar = "Utopias of Technological Art: The State of the Question Fifty Years On"

for elemento in bibliografia:
    if elemento['title'] == titulo_eliminar:
        bibliografia.remove(elemento)

with open(os.path.join(destino, "bibliografia.json"), "w", encoding='utf-8') as guardar:
    json.dump(bibliografia, guardar)

# Actualizar elemento

with open(os.path.join(destino, "bibliografia.json"), "r", encoding="utf-8") as archivo:
    bibliografia = json.load(archivo)

id = "http://zotero.org/users/163570/items/DFIAXHAZ"

for elemento in bibliografia:
    if elemento['id'] == id:
        elemento['issued']['date-parts'] = [["2020"]]

with open(os.path.join(destino, "bibliografia.json"), "w", encoding='utf-8') as guardar:
    json.dump(bibliografia, guardar, indent=4, ensure_ascii=False)


with open(os.path.join(destino, "bibliografia.json"), "r", encoding="utf-8") as archivo:
    bibliografia_test = json.load(archivo)

for elemento in bibliografia_test:
    if elemento['id'] == id:
        print(elemento['title'], elemento['issued'])
