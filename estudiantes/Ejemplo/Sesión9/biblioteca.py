from biblio import bibliografia

def buscar_biblio(campo, valor):
    for clave, item in bibliografia.items():
        if valor in item[campo]:
            return clave, item

def formar_biblio(clave, item):
    print(f"Autor: {item['autor'][0]['nombre']} {item['autor'][0]['apellido']}")
    print(f"Título: {item['titulo']}")
    print(f"Fecha: {item['fecha']}")

def busqueda_simple(campo, valor):
    clave, item = buscar_biblio(campo, valor)
    formar_biblio(clave, item)

if __name__ == '__main__':
    busqueda_simple("titulo", "Ser")