# Github

Al ser un repositorio colaborativo, Github nos permite compartir el código que escribimos con nuestros compañeros de equipo y colaborar en el desarrollo de un proyecto. Para facilitar la sincronización de los cambios que hacemos en nuestro repositorio local con el repositorio remoto en Github, vamos a utilizar la herramienta de Git.

## Clonar el repositorio del curso

* Abrir la terminal y ejecutar los siguientes comandos:

```bash
git clone https://github.com/Taller-Abierto-de-Humanidades-Digitales/curso_python_extenso.git
cd curso_python_extenso
```

* Abrir el proyecto en VSCode con el comando `code .`
* Abrir el archivo `README.md` en el directorio "estudiantes/tu_nombre" y agregar tu nombre, carrera, semestre y nombre de usuario de Github.

## Crear un branch para tu nombre

* Crear un branch con el comando `git checkout -b tu_nombre` (cambia "tu_nombre" por tu nombre)
* Agregar los cambios con el comando `git add .`
* Hacer un commit con el comando `git commit -m "Mis cambios: tu_nombre"`
* Hacer un push con el comando `git push -u origin tu_nombre`

```bash
git checkout -b tu_nombre
git add .
git commit -m "Mis cambios: tu_nombre"
git push -u origin tu_nombre
```

## Crear un pull request

* Ir a la página de Github del repositorio del curso: [https://github.com/Taller-Abierto-de-Humanidades-Digitales/curso_python_extenso](https://github.com/Taller-Abierto-de-Humanidades-Digitales/curso_python_extenso)
* Hacer click en el botón "Compare & pull request"
* Hacer click en el botón "Create pull request"
* Hacer click en el botón "Create pull request" de nuevo
* Hacer click en el botón "Merge pull request"
* Hacer click en el botón "Confirm merge"
* Hacer click en el botón "Delete branch"

## Actualizar tu repositorio local

* Abrir la terminal y ejecutar los siguientes comandos:

```bash
git checkout master
git pull
```
