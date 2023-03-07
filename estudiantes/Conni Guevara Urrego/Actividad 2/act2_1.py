# Ejercicio 1: Crea una variable para el nombre de una persona y otra para su apellido. Imprime el nombre completo de la persona.
# La variable debe ser 'nombre' y 'apellido' respectivamente.

# Escribe aquí tu código

nombre = "Graciela"
print(nombre)

apellido = "Montaña"
print(apellido)

# Ejercicio 2: Crea una variable para la marca de un carro. El nombre de la variable
# debe ser 'nombre_carro'. Imprime el nombre del carro.

# Escribe aquí tu código

nombre_carro = "Jeep"
print(nombre_carro)


# Ejercicio 3: El siguiente código está escrito de manera incorrecta.
# Corrige el código para que funcione correctamente.

primer_nombre = "Akira"
print(primer_nombre)
primer_apellido = "Toriyama"
print(primer_apellido)
nombre_completo1 = primer_nombre + " " + primer_apellido
print(nombre_completo1)
primer_nombre2 = "Quentin"
print(primer_nombre2)
primer_apellido2 = "Tarantino"
print(primer_apellido2)
nombre_completo2 = primer_nombre2 + " " + primer_apellido2
print(nombre_completo2)

fecha_nacimiento = 1955
print(fecha_nacimiento)
nombre_manga = "Dr. Slump"
print(nombre_manga)
nombre_manga2 = "Dragón Ball"
nombre_pelicula = "Pulp Fiction"
prin(nombre_pelicula)
fecha_pub = 1979
print(fecha_pub)
fecha_pub2 = 1984
print(fecha_pub2)
fecha_pelicula = 1994
print(fecha_pelicula)

####################################

# Ejercicio 4: Corrige las siguientes variables de texto para que el código funcione correctamente.


texto1 = f"{nombre_completo1} publicó su manga {nombre_manga2} en {fecha_pub2}"

texto2 = f"{nombre_completo2} es el director de la película {nombre_pelicula}. Fue emitida por primera vez en {fecha_pelicula}."

texto3 = f"Yo, señor, soy acontista. Mi profesión es hacer disparos al aire. Todavía no habré descendido la primera nube. Mas, la delicia está en curvar el arco y en suponer la flecha donde la clava el ojo."

texto4 = f"Es posible que {nombre} no haya leído {nombre_manga2}."

####################################

# Ejercicio 5: En el siguiente programa, necesitamos que no se ejecute la variable
# 'nombre', pero no la debes eliminar. ¿Cómo lo harías?

#nombre = "Paul Ricoeur"

print(f"El nombre de mi mejor amigo es {nombre}")

####################################

#
# Validación ¡No modificar!
av2.variable_test(nombre, apellido, nombre_carro)
av2.sintaxis_test(autor, fecha_nacimiento, nombre_manga, fecha_pub)
av2.string_test(texto1, texto2, texto3, texto4, nombre, nombre_manga)
av2.comment_test(nombre)

print("¡Felicitaciones! ¡Has completado el ejercicio!")

#
####################################
    
    