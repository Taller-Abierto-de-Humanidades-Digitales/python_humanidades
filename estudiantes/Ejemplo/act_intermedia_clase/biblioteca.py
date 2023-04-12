#####################################################
# datos para el ejercicio intermedio
# biblioteca
# autor: Jairo Antonio Melo Flórez
# fecha: 2023-03-26
# version: 1.0
# licencia: MIT License
#####################################################

# ubicar este archivo en la raiz del proyecto

import requests
import json


def biblioteca() -> list:
	"""
	Esta función retorna una bibliografía en formato CSL-JSON
	"""
	r = requests.get("https://raw.githubusercontent.com/Taller-Abierto-de-Humanidades-Digitales/curso_python_extenso/main/data/bibliografia.json")

	return json.loads(r.text)

if __name__ == "__main__":
	print(len(biblioteca()))