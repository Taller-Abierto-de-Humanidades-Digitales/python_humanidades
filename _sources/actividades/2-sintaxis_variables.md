# Actividad 2: Variables y sintaxis

Las variables y la sintaxis de Python son dos aspectos básicos, sencillos y fundamentales para la programación. En esta actividad, realizaremos tres ejercicios para practicar la sintaxis de Python y aprender a utilizar variables.

## Ejercicio 1: Sintaxis

El primer ejericio consiste en corregir el código de Python que se encuentra en el archivo `act2.py` en el directorio `code` de [este repositorio](https://github.com/Taller-Abierto-de-Humanidades-Digitales/curso_python_extenso/tree/main/code). El código tiene múltiples errores que deben ser corregidos para que el programa funcione correctamente.

Antes de empezar la actividad, deberás sincronizar tu repositorio local con el repositorio remoto. Para esto, debes abrir la terminal de comandos y ejecutar los siguientes comandos:

```bash
cd curso_python_extenso
git pull
```

Antes de hacer cualquier cambio, muevete al brazo en el que estás realizando las actividades:

```bash
git checkout tu_brazo
```

Copia los archivos `act2.py` y `act2Validator.py` en el directorio con tu nombre (de preferencia, crea un subdirectorio para esta actividad). Deben estar ambos en el mismo directorio, de otra manera el validador no funcionará.

Abre el archivo `act2.py` en Visual Studio Code y corrige los errores que se encuentran en el código. Para corregir los errores, debes leer el mensaje de error que aparece en la terminal de comandos y corregir el código en el archivo `act2.py` de acuerdo a lo que te indica el mensaje de error.

Una vez que hayas corregido los errores, debes guardar los cambios en el archivo `act2.py` y ejecutar el programa. Para ejecutar el programa, debes abrir la terminal de comandos y ejecutar el siguiente comando:

```bash
python act2.py
```

También puedes hacerlo directamente desde Visual Studio Code. Para esto, debes abrir el archivo `act2.py` y hacer clic en el botón `Run` que aparece en la parte superior de la ventana.

Las últimas líneas del programa corresponden a un validador del código. Es decir, el programa ejecuta una serie de pruebas para verificar que el código que has escrito funciona correctamente. Si el programa no muestra ningún mensaje de error, significa que el código que has escrito funciona correctamente. Si el programa muestra un mensaje de error, significa que el código que has escrito tiene errores y debes corregirlo.

## Ejercicio 2: Variables

El segundo ejercicio consiste en escribir un programa que exprese la conversación entre dos personas. El programa debe contener las siguientes variables:

- `nombre1`: Nombre de la primera persona
- `nombre2`: Nombre de la segunda persona
- `edad1`: Edad de la primera persona
- `edad2`: Edad de la segunda persona
- `lugar`: Lugar donde se encuentran las personas
- `tiempo`: Tiempo que llevan conversando

El programa debe imprimir la siguiente conversación:

```
Hola, mi nombre es [nombre1] y tengo [edad1] años.
Hola, mi nombre es [nombre2] y tengo [edad2] años.
Hemos estado conversando por [tiempo] minutos mientras estábamos en [lugar].
```

Para este ejercicio, debes crear un archivo llamado `act2_2.py` en el directorio con tu nombre. 

## Ejercicio 3: Manipulación de cadenas de texto

El tercer ejercicio consiste en escribir un programa que tome una frase y aplique las siguientes funciones:

- `lower()`: Convierte todas las letras de la frase a minúsculas
- `upper()`: Convierte todas las letras de la frase a mayúsculas
- `capitalize()`: Convierte la primera letra de la frase a mayúscula
- `title()`: Convierte la primera letra de cada palabra de la frase a mayúscula
- `swapcase()`: Convierte todas las letras de la frase a mayúsculas y minúsculas
- `strip()`: Elimina los espacios en blanco al inicio y al final de la frase
- `replace()`: Reemplaza una palabra por otra en la frase
- `split()`: Divide la frase en palabras

Cada función debe ser aplicada a la frase e imprimirla usando `format()`. Por ejemplo, si la frase es `hola mundo`, el programa debe imprimir:

```python
print(f"Esta es la frase en minúsculas: {frase.lower()}")
```

Para este ejercicio, debes crear un archivo llamado `act2_3.py` en el directorio con tu nombre. 

## Ejercicio 4: Operadores con cadenas de texto

El cuarto ejercicio consiste en escribir un programa que tome una frase y aplique los siguientes operadores:

- `+`: Concatena dos cadenas de texto
- `*`: Repite una cadena de texto un número de veces
- `in`: Verifica si una cadena de texto está contenida en otra
- `not in`: Verifica si una cadena de texto no está contenida en otra
- `==`: Verifica si dos cadenas de texto son iguales
- `!=`: Verifica si dos cadenas de texto son diferentes

Cada operador debe ser aplicado a la frase e imprimirla usando `format()`. Por ejemplo, si la frase es `hola mundo`, el programa debe imprimir:

```python
print(f"Esta es la frase concatenada: {frase + 'hola'}")
```

Para este ejercicio, debes crear un archivo llamado `act2_4.py` en el directorio con tu nombre.

## Entrega

Para entregar la actividad, debes hacer un `commit` de los modificados y hacer un `push` de tu brazo al repositorio remoto.

```bash
git add .
git commit -m "Entrega de la actividad 2"
git push -u origin nombre-del-brazo
```

### Fecha de entrega

Entrega la actividad antes del martes 7 de febrero.
