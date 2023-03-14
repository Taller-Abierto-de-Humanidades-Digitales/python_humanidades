# Actividad 8: Funciones II

En esta actividad vamos a realizar una serie de ejercicios que nos permitirán practicar el uso de funciones en Python.

Vamos a utilizar como insumo el siguiente diccionario, el cual contiene las biografías de algunos autores del Boom latinoamericano:

```python
biografias_boom = {
    "Julio Cortázar": {
        "nacionalidad": "Argentina",
        "bio": """Julio Cortázar nació en 1914. Vivió con sus padres en Suiza hasta que se mudó a Buenos Aires a la edad de cuatro años.40​ Al igual que otros escritores del boom, Cortázar llegó a cuestionar la política de su país: su oposición a Juan Domingo Perón lo llevó a dejar su puesto de profesor en la Universidad Nacional de Cuyo y en última instancia, a su exilio.41​.
        En 1951 se trasladó a París, donde pasó la mayor parte de su vida profesional, y en 1981 se convirtió en ciudadano francés.42​ Como García Márquez, Cortázar apoyó al gobierno cubano de Fidel Castro, al presidente chileno Salvador Allende, y a otros movimientos de izquierda como los sandinistas en Nicaragua.42​
        Entre sus influencias se encuentran Jorge Luis Borges y Edgar Allan Poe.43​ Su obra más importante y la que lo catapultó al reconocimiento internacional, es la novela Rayuela, publicada en 1963.42​ Se compone de 155 capítulos, 99 de los cuales son «fungibles», que se pueden leer en varios pedidos de acuerdo a la predilección de los lectores.
        Sus otros trabajos incluyen colecciones de cuentos como Bestiario (1951), Final del juego (1956), Las armas secretas (1959) y Todos los fuegos el fuego (1966). También escribió novelas como Los premios (1960) y Libro de Manuel (1973), y el inclasificable Historias de cronopios y de famas (1962). Falleció en París el 12 de febrero de 1984.""",
        "obra_principal": "Rayuela",
        "fecha_publicacion": "1963",
        "vivo": False,
    },
    "Gabriel García Márquez": {
        "nacionalidad": "Colombia",
        "bio": """
        Gabriel García Márquez nació en Aracataca, Colombia, en 1927. Junto a Mario Vargas Llosa, ha sido quien mayor proyección internacional ha logrado entre los escritores del boom. Gabo, como también se le conocía, empezó como periodista y escribió muchos artículos y relatos cortos, que fueron publicados en el diario El Espectador de Bogotá.44​ Después de residir unos años en Europa, se instaló en la Ciudad de México en 1961, donde residió hasta su fallecimiento.
        Es conocido por novelas como El coronel no tiene quien le escriba (1962), Cien años de soledad (1967), El otoño del patriarca (1975), y post-boom, como El amor en los tiempos del cólera (1985), y por haber recibido el Premio Nobel de Literatura en 1982. Ha logrado elogios de la crítica y éxito comercial general, sobre todo por la introducción de lo que se ha denominado realismo mágico en el mundo literario. Narró con métodos tradicionales hechos más o menos ajenos a la realidad, de modo que «lo más espantoso, las cosas más insólitas se dicen con la expresión impasible».45​ Un ejemplo comúnmente citado es el físico y espiritual de ascender al cielo de un personaje, mientras que cuelga la ropa a secar en Cien años de soledad. Esta novela cumbre del escritor colombiano, según estudios actuales, modifica la percepción que tenemos del pasado y construye una nueva mirada sobre el futuro.46​ García Márquez es ahora considerado como uno de los autores más significativos del siglo XX, como lo atestigua el haber sido galardonado con el Premio Nobel de Literatura en 1982. Falleció en México D.F. el 17 de abril de 2014.47​
        El autor es considerado, junto con Álvaro Mutis, como un escritor que realizó desde su obra un valioso aporte desde las letras colombianas durante el período denominado boom latinoamericano que está fuertemente influenciado por la presencia de escritores mexicanos, de la talla de Carlos Fuentes y Juan Rulfo. A partir del concepto de campo literario es lícito afirmar que la escritura de autor de Cien años de soledad produjo profundas transformaciones en la literatura del siglo XX.48​
        """,
        "obra_principal": "Cien años de soledad",
        "fecha_publicacion": "1967",
        "vivo": False,
    },
    "Carlos Fuentes": {
        "nacionalidad": "México",
        "bio": """
        Nacido en Panamá de padres mexicanos, en 1928, Carlos Fuentes comenzó a publicar en la década de 1950.49​ Fue hijo de un diplomático mexicano y vivió en ciudades como Buenos Aires, Santiago, Quito, Montevideo y Río de Janeiro, así como Washington D. C..50​ Sus experiencias de lucha contra la discriminación de México en los Estados Unidos le llevó a examinar más de cerca la cultura mexicana.51​ Su novela La muerte de Artemio Cruz (1962) describe la vida de un ex revolucionario mexicano en su lecho de muerte, cambios innovadores que emplean en un punto de vista. Otros trabajos importantes incluyen La región más transparente (1959), Aura (1962), Terra Nostra (1975), y la novela post-boom Gringo Viejo (1985).
        Fuentes no solo escribió algunas de las novelas más importantes de la época, también fue un crítico y publicista de Latinoamérica. En 1955, Fuentes y Emmanuel Carballo fueron fundadores de la Revista Mexicana de Literatura, que introdujo los latinoamericanos a las obras modernistas de Europa y las ideas de Jean-Paul Sartre y Albert Camus.52​ En 1969 publicó la obra crítica importante, La nueva novela hispanoamericana. Fuentes ocupó el cargo de profesor de literatura latinoamericana en la Universidad de Columbia (1978) y en Harvard (1987).53​ En una ocasión dijo que «el llamado boom, en realidad, es el resultado de cuatro siglos, literariamente, llegado a un momento de urgencia en que la ficción se convirtió en la manera de organizar las lecciones del pasado».54​Falleció en México D.F. el 15 de mayo de 2012.
        """,
        "obra_principal": "La muerte de Artemio Cruz",
        "fecha_publicacion": "1962",
        "vivo": False,
    },

    "Mario Vargas Llosa": {
        "nacionalidad": "Perú",
        "bio": """
            Jorge Mario Pedro Vargas Llosa (Arequipa, 28 de marzo de 1936), conocido como Mario Vargas Llosa, es un escritor peruano que cuenta también con la nacionalidad española desde 1993. Considerado uno de los más importantes novelistas y ensayistas contemporáneos, sus obras han cosechado numerosos premios, entre los que destacan el Nobel de Literatura 2010, el Cervantes 1994 —considerado como el más importante en lengua española—, el Príncipe de Asturias de las Letras 1986, el Biblioteca Breve 1962, el Rómulo Gallegos 1967 y el Planeta 1993, entre otros.
            Como escritor, alcanzó la fama en la década de 1960 con novelas como La ciudad y los perros (1963), La casa verde (1966) y Conversación en La Catedral (1969). Continuó escribiendo prolíficamente en varios géneros literarios, como el ensayo, el artículo y el teatro. Varias de sus obras han sido adaptadas al cine y a la televisión. La mayoría de sus novelas están ambientadas en Perú y exploran su concepción sobre la sociedad peruana; en cambio, en La guerra del fin del mundo (1981), La fiesta del Chivo (2000) y El sueño del celta (2010), ubica sus tramas en otros países.
            """,
        "obra_principal": "La casa verde",
        "fecha_publicacion": "1966",
        "vivo": True,
    }}
```

Estas biografías fueron tomadas de Wikipedia y van a servirnos para realizar las siguientes operaciones:

## Ejercicio 1: Crear una lista con los autores que están en el diccionario

Debes crear una función llamada `autores()`, que regrese una lista con el nombre de cada uno de los autores del boom.

La función recibe como parámetro un diccionario con la información de los autores del boom latinoamericano. La función debe regresar una lista con el nombre de cada uno de los autores del boom.

## Ejercicio 2: Escribe una función que regrese la fecha de nacimiento del autor a partir de la información de su biografía

Crea dos funciones, una llamada `extraer_fechas()` que permita obtener las fechas de la biografía de cada autor, y otra llamada `fecha_nacimiento()` que permita obtener la fecha de nacimiento de cada autor.

La función `extraer_fechas()` recibe como parámetro un string con la biografía de un autor. La función debe regresar una lista con las fechas que se encuentren en la biografía.
La función `fecha_nacimiento()` recibe como parámetro un string con el nombre del autor. La función debe regresar la fecha de nacimiento del autor.

## Ejercicio 3 - Escribe una función que regrese la edad promedio de los autores al momento de publicar su obra principal

Debes crear dos funciones, una llamada `calcular_edad()` que permita calcular la edad de cada autor al momento de publicar su obra principal, y otra llamada `edad_promedio()` que permita calcular la edad promedio de los autores al momento de publicar su obra principal.

La función `calcular_edad()` recibe como parámetro un string con el nombre del autor. La función debe regresar la edad del autor al momento de publicar su obra principal.
La función `edad_promedio()` recibe como parámetros una lista con los nombres de los autores y un diccionario. La función debe regresar la edad promedio de los autores al momento de publicar su obra principal (`int`).

## Ejercicio 4 - Escribe una función que regrese la edad de los autores al momento de su defunción

Será necesario crear una función llamada `fecha_defuncion()` para extraer la fecha de defunción de la biografía. Debes llamar la función `fecha_nacimiento()` para obtener la fecha de nacimiento de cada autor, y crearla función `edad_defuncion()` para calcular la edad de cada autor al momento de su defunción.

La función `fecha_defuncion()` recibe como parámetros un string con el nombre del autor y un diccionario. La función debe regresar un valor `None` si el autor no ha fallecido, o la fecha de defunción del autor si ya falleció (`int`).
La función `edad_defuncion()` recibe como parámetros un string con el nombre del autor y un diccionario. La función debe regresar la edad del autor al momento de su defunción (`int`).

## Ejercicio 5 - Escribe una función que regrese el nombre del autor más longevo

Vamos a utilizar la función que acabamos de crear para calcular la edad de cada autor al momento de su defunción. También será necesario determinar si el autor ya falleció o no. Debes crear una función llamada `longevo()` que permita determinar el nombre del autor más longevo. Esta función regresa un tuple con el nombre del autor y su edad.

La función `longevo()` recibe como parámetros una lista con los nombres de los autores y un diccionario. La función debe regresar un tuple con el nombre del autor más longevo y su edad (`tuple`).

## Ejercicio 6 - Escribe una función para llamar a todo el programa

Debes crear una función llamada `main()` que permita llamar a todas las funciones que acabamos de crear. Esta función no recibe parámetros y no regresa ningún valor. Debe escribirse de la siguiente manera:

```python
def main():
    # Llama a las funciones que acabamos de crear
    autores_boom = autores(biografias_boom)
    print(autores_boom)
    promedio_edad_autores_boom = edad_promedio(autores_boom, bios=biografias_boom )
    print(f"La edad promedio de los autores_boom del Boom Latinoamericano fue de {promedio_edad_autores_boom} años")
    longevo_autores_boom = longevo(autores_boom, bio=biografias_boom )
    print(f"El autor más longevo de los autores_boom del Boom Latinoamericano fue {longevo_autores_boom[0]} quien vivió {longevo_autores_boom[1]} años")
```

## Envío de la actividad

Al igual que las actividades anteriores, envía tu código a través de Github.

Los cinco ejercicios deberán ser realizados en un archivo llamado `actividad8.py`. Guárdalo en el directorio con tu nombre (de preferencia en un subdirectorio).

Para entregar la actividad, debes hacer un `commit` de los modificados y hacer un `push` de tu brazo al repositorio remoto.

```bash
git add .
git commit -m "Entrega de la actividad 8"
git push -u origin nombre-del-brazo
```

### Fecha de entrega

Entrega la actividad antes del martes 21 de marzo.
