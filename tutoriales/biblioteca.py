from biblio import bibliografia

def buscar_biblio(campo, valor):
    for clave, item in bibliografia.items():
        if isinstance(item[campo], list):
            for autor in item[campo]:
                if valor.lower() in autor["nombre"].lower():
                    return clave, item
                elif valor.lower() in autor["apellido"].lower():
                    return clave, item    
        elif valor.lower() in item[campo].lower():
            return clave, item

def formato_biblio(clave, item):
    print(f"Clave: {clave}")
    print(f"Tipo: {item['tipo']}")
    print(f"Autor: {item['autor'][0]['nombre']} {item['autor'][0]['apellido']}")
    print(f"Título: {item['titulo']}")
    print(f"Editorial: {item['editorial']}")
    print(f"Lugar: {item['lugar']}")
    print(f"Fecha: {item['fecha']}")

def busqueda_simple(campo, valor):
    try:
        clave, item = buscar_biblio(campo, valor)
        formato_biblio(clave, item)
    except TypeError:
        print("No se encontró el elemento")

if __name__ == "__main__":
    busqueda_simple("titulo", "Ser y tiempo")