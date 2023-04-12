import act2Validator as av2

####################################

# Ejercicio 1: Crea una variable para el nombre de una persona y otra para su apellido. Imprime el nombre completo de la persona.
# La variable debe ser 'nombre' y 'apellido' respectivamente.

# Escribe aquí tu código

nombre = "Daniel"
apellido = "quiñones"
nombre_completo = nombre + apellido 

print (nombre_completo)

# Ejercicio 2: Crea una variable para la marca de un carro. El nombre de la variable
# debe ser 'nombre_carro'. Imprime el nombre del carro.

# Escribe aquí tu código

nombre_carro = "mazda"

print (nombre_carro)

####################################

# Ejercicio 3: El siguiente código está escrito de manera incorrecta.
# Corrige el código para que funcione correctamente.

primer_nombre = "Akira"
primer_apellido = "Toriyama"

autor = "Roxan"

print ("autor")

fecha_nacimiento = 1955

nombre_manga = "Dr. Slump"

fecha_pub = "1979"

####################################

# Ejercicio 4: Corrige las siguientes variables de texto para que el código funcione correctamente.

texto1 = "Akira Toriyama publicó su manga \"Dragon Ball\" en 1984"
texto2 = "Quentin Tarantino es el director" + " de la película Pulp Fiction"
texto3 = """Yo, señor, soy acontista.
        Mi profesión es hacer disparos al aire.
        Todavía no habré descendido la primera nube.
        Mas, la delicia está en curvar el arco
        y en suponer la flecha donde la clava el ojo."""
texto4 = "Es posible que {nombre} no haya leído nombre_manga."


####################################

# Ejercicio 5: En el siguiente programa, necesitamos que no se ejecute la variable
# 'nombre', pero no la debes eliminar. ¿Cómo lo harías?

nombre = "Paul Ricoeur"

print("El nombre de mi mejor amigo es {nombre}")

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