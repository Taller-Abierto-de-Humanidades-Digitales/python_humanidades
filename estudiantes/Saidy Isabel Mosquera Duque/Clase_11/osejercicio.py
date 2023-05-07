import os

directorio = os.getcwd()
print(directorio)


ruta_al_txt = os.path.join(directorio, r"estudiantes/Saidy Isabel Mosquera Duque/Clase_11", "can_visual.txt")

base_directorio = os.path.basename(ruta_al_txt)
#print(base_directorio)
base_dirname = os.path.dirname(ruta_al_txt)
#print(base_dirname)


t = open(ruta_al_txt, "r", encoding="utf-8")
texto = t.read()

destino = os.path.join(base_dirname, "subdirectorio")

try:
    os.makedirs(destino, exist_ok=True)
except OSError:
     raise


with open(os.path.join(destino, "copia_can_visual.txt"), "w", encoding="utf-8") as f:
    f.write(texto)


list_archivos = os.listdir(destino)
#print(list_archivos)

#os.rmdir(destino)   

"""for l in list_archivos:
     os.remove(os.path.join(destino, l))"""

for l in list_archivos:
    print(l)

for (raiz, dirs, archivos) in os.walk(base_dirname, topdown=True):
    for archivo in archivos:
        if archivo.endswith(".txt"):
            print(archivos)   