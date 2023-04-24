# Función buscador en biblioteca por fecha
from biblioteca import biblioteca


""" 
Debe buscar por título, autor, año de publicación y palabras claves.

Debe tener la opción de buscar por libro, artículo, tesis o cualquier otro tipo de elemento.

Debe tener la opción de buscar por coincidencia exacta o por coincidencia parcial.

Debe tener la capacidad de formatear el resultado para hacerlo legible al usuario.

Debe poder lidiar con el tipo de dato de los autores (list) y de las fechas (dict). """

def buscatitulo(tipodocumento: str, cadenaclave:str, biblioteca:list) -> list:
    resultadobusqueda = []

    if tipodocumento != 'todo':
        for elemento in biblioteca:
            if elemento['type'] in tipodocumento and cadenaclave.lower() in elemento['title'].lower():
                resultadobusqueda.append(int(biblioteca.index(elemento)))
    else:
        for elemento in biblioteca:
            if cadenaclave.lower() in elemento['title'].lower():
                resultadobusqueda.append(int(biblioteca.index(elemento)))
    return resultadobusqueda

resultado = buscatitulo("article-journal", "information", biblioteca())

def busqueda(palabra_clave, campo, tipo):
    resultado = []
    for elemento in biblioteca():
        if tipo == elemento['type']:
            try:
                valor = elemento[campo]
                if palabra_clave in valor:
                    resultado.append(elemento)
                elif isinstance(valor, list):
                    for val in valor:
                        for k, v in val.items():
                            if palabra_clave in v:
                                resultado.append(elemento)
                elif isinstance(valor, dict):
                    if palabra_clave in elemento['issued']['date-parts'][0][0]:
                        resultado.append(elemento)
            except KeyError:
                pass
    
    return resultado


#autorr == [{'family': ' ', 'given': ' '}] 

def unbox(**autores):
 autorr = [{'family': '', 'given': ''}] 
 for autor in biblioteca:
    for clave, valor in autores.items():
        autorr += f'{clave} = {valor}, '
        return autorr

s= unbox(**biblioteca["author"])
print(unbox(s))
  

def formateador(resultados):
    resultado = "\n\n"
    for item in resultados:
        resultado += "--------------------------\n"
        for clave, valor in item.items():
            resultado += f"{clave}: {valor}\n"  
        
        resultado += "--------------------------\n"
        """ if "family" in biblioteca["author"]: 
            del (biblioteca["author"]["family"])
                  """
         
    return resultado

r = busqueda("2000", "issued", "article-journal")
print(formateador(r))

""" def autores(catalogo): # pasa un parámetro
    Completa la función para que devuelva una lista con los nombres de los autores
    autores = []
    for author in catalogo:
        autores.append(author)
    return autores

autores_boom = autores(catalogo= biblioteca)
print(autores_boom)
 """




        



