import re

Cervantes = "Miguel de Cervantes  Saavedra (Alcalá de Henares,4 29 de septiembre de 1547-Madrid, 22 de abril3 de 1616) fue un novelista, poeta, dramaturgo y soldado español."
Cervantes += """Es ampliamente considerado una de las máximas figuras de la literatura española. Fue el autor de El ingenioso hidalgo don Quijote de la Mancha, novela conocida habitualmente como El Quijote, que lo llevó a ser mundialmente conocido y a la cual muchos críticos han descrito como la primera novela moderna, así como una de las mejores obras de la literatura universal, cuya cantidad de ediciones y traducciones solo es superada por la Biblia.5 A Cervantes se le ha dado el apelativo de «Príncipe de los Ingenios».6

Desde el siglo xviii está admitido que el lugar de nacimiento de Miguel de Cervantes fue Alcalá de Henares,4 dado que allí fue bautizado, según su acta bautismal, y que de allí aclaró ser natural en la llamada Información de Argel (1580).7 El día exacto de su nacimiento es menos seguro, aunque lo normal es que naciera el 29 de septiembre, fecha en que se celebra la fiesta del arcángel San Miguel, dada la tradición de recibir el nombre del santoral del día del nacimiento. Miguel de Cervantes fue bautizado el 9 de octubre de 1547 en la parroquia de Santa María la Mayor.89 El acta del bautizo reza:

Domingo, nueve días del mes de octubre, año del Señor de mill e quinientos e quarenta e siete años, fue baptizado Miguel, hijo de Rodrigo Cervantes e su mujer doña Leonor. Baptizóle el reverendo señor Bartolomé Serrano, cura de Nuestra Señora. Testigos, Baltasar Vázquez, Sacristán, e yo, que le bapticé e firme de mi nombre. Bachiller Serrano.10
El padre del escritor era Rodrigo de Cervantes (1509-1585), casado con Leonor de Cortinas, de la cual apenas se sabe nada, excepto que era natural de Arganda del Rey.11 Los hermanos de Cervantes fueron Andrés (1543), Andrea (1544), Luisa (1546), que llegó a ser priora de un convento carmelita; Rodrigo (1550), también soldado, que le acompañó en el cautiverio argelino; Magdalena (1554) y Juan, solo conocido porque su padre lo menciona en el testamento."""

# * 0 o más coincidencias
# + 1 o más coincidencias
# {} n cantidad de ocurrencias
# ^ inicio de la cadena
# $ final de la cadena
# . un caracter excepto salto de línea
# ? cero o una ocurrencia
# {n,m}
# () grupo

# clases de caracteres
# \d dígito
# \s espacios en blanco
# \w cualquier caracter alfanumérico

conectores = ["Es", "Se", "De", "El", "La", "Los", "Las", "Un", "Una", "Unos", "Unas", "Al", "Del", "Y", "O", "En", "A", "Ante", "Bajo", "Cabe", "Con", "Contra", "De", "Desde", "Durante", "En", "Entre", "Hacia", "Hasta", "Mediante", "Para", "Por", "Según", "Sin", "Sobre", "Tras", "Versus", "Vía", "Fue"]

patron = r"\b(?!" + "|".join(conectores) + r"\b)([A-Z][a-ü]+)\b"

busqueda = re.findall(patron, Cervantes)
print(busqueda)
