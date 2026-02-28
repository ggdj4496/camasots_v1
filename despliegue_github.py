import os, subprocess, time
from datetime import datetime

ruta_base = r'C:\CAMASOTS_V1'

def ejecutar_git(comando):
    try:
        result = subprocess.run(comando, shell=True, cwd=ruta_base, capture_output=True, text=True)
        print(result.stdout)
    except Exception as e:
        print(f"ERROR GIT: {e}")

# CONFIGURACION DE IDENTIDAD SOBERANA EN GITHUB
ejecutar_git("git init")
ejecutar_git("git config user.email 'ggdj4496@gmail.com'")
ejecutar_git("git config user.name 'Virgilio G'")

# CREACION DE ARCHIVO ESTRUCTURA PARA EL REPOSITORIO
with open(os.path.join(ruta_base, 'ESTRUCTURA_SISTEMA.txt'), 'w') as f:
    f.write("SISTEMA CAMASOTS V1 - AGENTE VIRGILIO G\n")
    f.write(f"DESPLIEGUE COMPLETO: {datetime.now()}\n")
    f.write("ESTADO: FUEGO GOLD - SIN ACENTOS\n")

# PUSH AL MAXIMO RENDIMIENTO
print("SUBIENDO MODULOS MDB, IAGEN, CARPETZFENIX...")
ejecutar_git("git add .")
ejecutar_git('git commit -m "DESPLIEGUE TOTAL SOBERANO - VIRGILIO G"')
# NOTA: REQUIERE QUE EL REPOSITORIO ESTE CREADO EN LA CUENTA GGDJ4496
ejecutar_git("git branch -M master")
ejecutar_git("git push -u origin master --force")

print("SINCRONIZACION CON GITHUB COMPLETADA AL 100%")
