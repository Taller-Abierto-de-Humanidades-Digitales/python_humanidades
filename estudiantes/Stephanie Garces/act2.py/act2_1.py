# Ejercicio 1: Crea una variable para el nombre de una persona y otra para su apellido. Imprime el nombre completo de la persona.
# La variable debe ser 'nombre' y 'apellido' respectivamente.

# Escribe aquí tu código

nombre = "Pepe" 
apellido = "Pérez" 
nombre_apellido = nombre + apellido
print(nombre_apellido)


# Ejercicio 2: Crea una variable para la marca de un carro. El nombre de la variable
# debe ser 'nombre_carro'. Imprime el nombre del carro.

# Escribe aquí tu código

Nombre = "cma"
Carro = "normal" 
nombre_carro = Nombre + Carro 
print(nombre_carro)


# Ejercicio 3: El siguiente código está escrito de manera incorrecta.
# Corrige el código para que funcione correctamente.

primer_nombre = "Akira"
primer_apellido = "Toriyama"
Autor = primer_nombre + primer_apellido
print(Autor)

fecha_nacimiento = 1955
Nombre_Manga = "Dr. Slump"

fecha_pub = 1979


texto1 = f"{Autor} publicó su manga Dr. Slump en {fecha_pub}"
print(texto1)

nombre = "Quentin"
apellido = " Tarantino" 
autor2 = nombre + apellido 
print(autor2)

película = "¨Pulp Fiction¨"

texto2 = f"{autor2} es el director de la película {película}"
print(texto2)

quien = "yo"
pregrado = "acontista"
explicación = "Mi profesión es hacer disparos al aire. Todavía no habré descendido la primera nube. Mas, la delicia está en curvar el arco y en suponer la flecha donde la clava el ojo."
texto3 = f"{quien} , señor soy {pregrado} , {explicación}" 
print(texto3)

nombre4 = "Juana"
nombre_manga = "¨los dementores del desierto¨"
texto4 = f"Es posible que {nombre4} no haya leído {nombre_manga}."
print(texto4)

# Ejercicio 5: En el siguiente programa, necesitamos que no se ejecute la variable
# 'nombre', pero no la debes eliminar. ¿Cómo lo harías?

nombre = "Paul Ricoeur"

print(f"El nombre de mi mejor amigo es ")

# Validación ¡No modificar!
av2.variable_test(nombre, apellido, nombre_carro)
av2.sintaxis_test(autor, fecha_nacimiento, nombre_manga, fecha_pub)
av2.string_test(texto1, texto2, texto3, texto4, nombre, nombre_manga)
av2.comment_test(nombre)

print("¡Felicitaciones! ¡Has completado el ejercicio!")