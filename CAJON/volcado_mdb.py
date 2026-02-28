import os

ruta_mdb = r'C:\CAMASOTS_V1\MDB'
modulos = [
    "01_REGLAS_ORO", "02_USUARIO", "03_ARIA_CORE", "04_VIRGILIO_LOG", 
    "05_PROGRAMACION", "06_GITHUB_SYNC", "07_GOOGLE_CLOUD", "08_SISTEMA_TRAY",
    "09_INVESTIGACION", "10_PROYECTOS", "11_MEMORIA_SENSORIAL"
]

def materializar_mdb():
    if not os.path.exists(ruta_mdb):
        os.makedirs(ruta_mdb)
    
    for mod in modulos:
        archivo = os.path.join(ruta_mdb, f"MDB_{mod}.csv")
        with open(archivo, 'w') as f:
            f.write("ID_BIT;CATEGORIA;CONTENIDO;ESTADO;TIMESTAMP\n")
            if "01" in mod:
                f.write("001;BLINDAJE;FUEGO GOLD ACTIVO SIN ACENTOS;ACTIVO;2026-02-23\n")
            if "02" in mod:
                f.write("001;IDENTIDAD;CABALLERO;VALIDADO;2026-02-23\n")
    print("MASTERDATABASE MATERIALIZADA CON EXITO")

if __name__ == '__main__':
    materializar_mdb()
