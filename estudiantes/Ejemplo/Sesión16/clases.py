# objeto = entidad (instancia)
# función = actividad (acción)

class Libro:
    def __init__(self, autor, titulo, editorial, anio, pags):
        self.autor = autor
        self.titulo = titulo
        self.editorial = editorial
        self.anio = anio
        self.pags = pags

    def mostra_info(self):
        return f"El libro {self.titulo}, fue escrito por {self.autor} en el año {self.anio} y publicado por la editorial {self.editorial}"
    
    def mostra_autor(self):
        return f"El autor del {self.titulo} es {self.autor}"

libros = {
    "titulo": "El Quijote",
    "autor": "Miguel de Cervantes",
    "año": 1605,
    "editorial": "Imprenta Real",
    "pags": 500
}

ejemplo = Libro(libros["titulo"], libros["autor"], libros["editorial"], libros["año"], libros["pags"])

print(ejemplo.mostra_info())
print(ejemplo.mostra_autor())
