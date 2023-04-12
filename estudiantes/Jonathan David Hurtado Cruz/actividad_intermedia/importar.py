from biblioteca import biblioteca

titulo = '¿Qué son las Humanidades Digitales?'

for elemento in biblioteca():
    if elemento['title'].lower() == titulo.lower():
        print(elemento)

biblioteca = biblioteca()
print(biblioteca[1]['title'])

""" 
def buscar_biblio(campo, valor):
    for clave, item in biblioteca:
        if item[campo] == valor:
            return clave, item

def formato_biblio(clave, item):
    print(f"Clave: {clave}")
    print(f"Tipo: {item['type']}")
    print(f"Autor: {item['author'][0]['family']} {item['author'][0]['given']}")
    print(f"Título: {item['title']}")
    print(f"Editorial: {item['container-title']}")
    print(f"DOI: {item['DOI']}")
    print(f"Fecha: {item['issued']}")

def busqueda_simple(campo, valor):
    clave, item = buscar_biblio(campo, valor)
    formato_biblio(clave, item)

busqueda_simple("tittle", "¿Qué son las Humanidades Digitales?")

 """


"""  for titulos in biblioteca: 
        titulos(titulo)
        return (titulos)
 
 for fechas in biblioteca:
      fechas(fecha)
      return fechas 
 
 for palabras_claves in biblioteca: 
      palabras_claves(palabra_clave)
      return palabras_claves
  """