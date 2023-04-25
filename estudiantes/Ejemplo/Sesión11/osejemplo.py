import os

directorio = os.getcwd()

ruta_al_txt = os.path.join(directorio, r"estudiantes\Ejemplo\Sesión11", "arreola.txt")

base_directorio = os.path.basename(ruta_al_txt)
#print(base_directorio)
base_dirname = os.path.dirname(ruta_al_txt)
#print(base_dirname)

t = open(ruta_al_txt, 'r', encoding='utf-8')
texto = t.read()

destino = os.path.join(base_dirname, "subdirectorio")

""" if not os.path.exists(destino):
    os.mkdir(destino) """

try:
    os.makedirs(destino, exist_ok=True)
except OSError:
    raise

with open(os.path.join(destino, "copia_resultado.txt"), 'w', encoding='utf-8') as f:
    f.write(texto)


lista_archivos = os.listdir(base_dirname)

""" try:
    os.rmdir(destino)
except OSError:
    for l in lista_archivos:
        os.remove(os.path.join(destino, l))
    os.rmdir(destino)

 """

""" for l in lista_archivos:
    print(l) """

for (raiz, dirs, archivos) in os.walk(base_dirname, topdown=True):
    for archivo in archivos:
        if archivo.endswith('.txt'):
            print(archivo)

print(os.curdir)