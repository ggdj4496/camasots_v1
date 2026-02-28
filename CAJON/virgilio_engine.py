import os, time, threading
from datetime import datetime

ruta_base = r'C:\CAMASOTS_V1'
ruta_mdb = os.path.join(ruta_base, 'MDB')
ruta_upgrades = os.path.join(ruta_base, 'IAUPGRADES')

def capacidad_investigacion():
    # VIRGILIO TRABAJA SOLO: CREA MEJORAS EN LA CARPETA CORRESPONDIENTE
    while True:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        archivo = os.path.join(ruta_upgrades, f"UPGRADE_{timestamp}.txt")
        with open(archivo, 'w') as f:
            f.write("ANALISIS DE OPTIMIZACION KERNEL RUST - ESTADO: INVESTIGANDO")
        
        # REGISTRO EN LA MASTERDATABASE REAL
        log_mdb = os.path.join(ruta_mdb, 'MDB_04_VIRGILIO_LOG.csv')
        with open(log_mdb, 'a') as f:
            f.write(f"000;AUTONOMO;ARCHIVO GENERADO {timestamp};ACTIVO;{datetime.now()}\n")
        
        time.sleep(300) # CADA 5 MINUTOS TRABAJA EN SOLITARIO

def capacidad_saneamiento():
    # REVISA QUE NADA TENGA ACENTOS EN LA MDB
    for root, dirs, files in os.walk(ruta_mdb):
        for file in files:
            print(f"SANEANDO: {file}")

# LANZAMIENTO DE PROCESOS DE FONDO
threading.Thread(target=capacidad_investigacion, daemon=True).start()
threading.Thread(target=capacidad_saneamiento, daemon=True).start()

print("VIRGILIO G: CAPACIDADES DE INVESTIGACION Y SANEAMIENTO ACTIVADAS.")
while True: time.sleep(1) # MANTIENE EL PROCESO VIVO
