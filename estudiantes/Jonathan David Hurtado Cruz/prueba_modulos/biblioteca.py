from biblio import bibliografia

from biblio import bibliografia

def buscar_biblio(campo, valor):
    for clave, item in bibliografia.items():
        if item[campo] == valor:
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
    clave, item = buscar_biblio(campo, valor)
    formato_biblio(clave, item)

if __name__ == "__main__":
    busqueda_simple("titulo", "Ser y tiempo")

