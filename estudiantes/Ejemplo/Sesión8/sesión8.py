# retornar valores..

def saludar(nombre: str, fecha_nacimiento: int, lugar_de_nacimiento="Colombia") -> tuple[int, str, str]:
    """ Saluda a una persona y le dice su edad

    Parámetros
    -------
    nombre: str
        Nombre de la persona a saludar
    fecha_nacimiento: int
        Año de nacimiento de la persona
    lugar_de_nacimiento: str
        Lugar de nacimiento de la persona

    Retorna
    -------
    edad: int
        Edad calculada a partir de la fecha de nacimiento
    nombre: str
        Nombre dado por el usuario
    pais: str
        País mencionado por el usuario o el predeterminado

    """
    edad = 2023 - int(fecha_nacimiento)
    return edad, nombre, lugar_de_nacimiento # regresa un tuple

def limpiar_texto(texto: str) -> list:
    """ Función "limpia" el texto que le pasen
    """

    texto = texto.replace("-", " ").replace(".", " ")

    texto_limpio = []

    for palabra in texto.split():
        palabra = palabra.strip(",;:()[]{}")
        if palabra.endswith("."):
            palabra = palabra.replace(".", "")

        texto_limpio.append(palabra)
    
    return texto_limpio
        


def extraer_fechas(texto: str) -> list:
    """ Extrae todos los años de un texto

    PArámetros
    ----------
    texto: str
        Texto del cual se extraerán las fechas

    Retorna
    -----------
    fechas: list
        lista de fechas extraídas del text
    
    """

    fechas = []

    for palabra in limpiar_texto(texto):
        if palabra.isdigit() and len(palabra) == 4:
            fechas.append(palabra)

    return fechas


def conteo_frecuencias(texto: str) -> dict:
    """Cuenta las palabras que aparecen en un texto.
    
    Parámetros
    ----------
    texto: str
        Texto del cual se extraerán las palabras

    Retorna
    -------
    palabras: dict
        Diccionario con las palabras y su frecuencia
    """

    palabras = {}

    for palabra in limpiar_texto(texto):
        if palabra in palabras:
            palabras[palabra] += 1
        else:
            palabras[palabra] = 1

    return palabras




Cervantes = "Miguel de Cervantes Saavedra (Alcalá de Henares,4​ 29 de septiembre de 1547-Madrid, 22 de abril3​ de 1616) fue un novelista, poeta, dramaturgo y soldado español."
Quevedo = "Francisco Gómez de Quevedo Villegas y Santibáñez Cevallos (Madrid, 14 de septiembre de 1580-Villanueva de los Infantes, Ciudad Real, 8 de septiembre de 1645) fue un noble, político y escritor español del Siglo de Oro."
Calderon = "Pedro Calderón de la Barca (Madrid, 17 de enero de 1600-25 de mayo de 1681) fue un escritor español, sacerdote católico, miembro de la Venerable Congregación de Presbíteros Seculares Naturales de Madrid San Pedro Apóstol y caballero de la Orden de Santiago, conocido fundamentalmente por ser uno de los más insignes literatos barrocos del Siglo de Oro, en especial por su teatro."

bios = [Cervantes, Quevedo, Calderon]


for b in bios:
    fechas = extraer_fechas(b)
    print(f"La edad de defunción de la persona fue {int(fechas[1]) - int(fechas[0])}")

    palabras_frecuentes = conteo_frecuencias(b)

    for palabra, frecuencia in palabras_frecuentes.items():
        if frecuencia > 1:
            print(palabra, frecuencia)

print(limpiar_texto(Calderon))