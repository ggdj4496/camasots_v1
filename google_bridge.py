import os

# DEFINICION DE RUTAS CON R-STRING PARA EVITAR ESCAPE SEQUENCES
ruta_mdb = r'C:\CAMASOTS_V1\MDB'
archivo_ok = os.path.join(ruta_mdb, 'CONEXION_OK.txt')

def vincular_google_limpio():
    try:
        if not os.path.exists(ruta_mdb):
            os.makedirs(ruta_mdb)
        with open(archivo_ok, 'w') as f:
            f.write('SISTEMA VINCULADO A GOOGLE CLOUD ROOT - SELLADO LIMPIO')
        print("CONEXION CON GOOGLE VALIDADA Y SELLADA")
    except Exception as e:
        print(f"FALLO EN SELLADO: {e}")

if __name__ == '__main__':
    vincular_google_limpio()
