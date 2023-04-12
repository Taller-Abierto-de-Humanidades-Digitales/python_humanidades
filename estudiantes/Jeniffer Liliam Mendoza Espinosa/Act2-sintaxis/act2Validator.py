
def variable_test(nombre, apellido, nombre_carro):
    # check if nombre is defined and is a string
    assert type(nombre) == str
    assert type(apellido) == str
    assert type(nombre_carro) == str
    assert f"{nombre} {apellido}" != "Akira Toriyama", "Las variables del ejercicio 2 no pueden ser las mismas del ejercicio 1"
    print(f"Mi amigo se llama {nombre} {apellido} y tiene un {nombre_carro}")

def sintaxis_test(autor, fecha_nacimiento, nombre_manga, fecha_pub):
    # check if autor is defined and is a string
    assert type(autor) == str
    # check if fecha_nacimiento is defined and is an int
    assert type(fecha_nacimiento) == int
    # check if nombre_manga is defined and is a string
    assert type(nombre_manga) == str
    # check if fecha_pub is defined and is an int
    assert type(fecha_pub) == int
    print(f"""
        {autor} nació en {fecha_nacimiento} y publicó su primer manga, 
        {nombre_manga} en {fecha_pub} cuando tenía {fecha_pub - fecha_nacimiento} años de edad.""")


def string_test(texto1, texto2, texto3, texto4, nombre, nombre_manga):
    # check if texto1 is defined and is a string
    assert type(texto1) == str
    # check if texto2 is defined and is a string
    assert type(texto2) == str
    assert texto2 == "Quentin Tarantino es el director de la película Pulp Fiction", "La variable texto2 no es correcta"
    assert type(texto3) == str
    assert type(texto4) == str
    assert texto4 == f"Es posible que {nombre} no haya leído {nombre_manga}.", "La variable texto4 no es correcta"

def comment_test(nombre):
    # check if nombre is defined and is a string
    assert type(nombre) == str
    assert nombre != "Paul Ricoeur", "La variable nombre no debe ser definida"