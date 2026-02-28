import os, time, threading, subprocess
from datetime import datetime
import pystray
from PIL import Image, ImageDraw

def crear_icono():
    img = Image.new('RGB', (64, 64), 'green')
    d = ImageDraw.Draw(img)
    d.polygon([(10, 15), (32, 50), (54, 15)], fill='white')
    return img

# --- CAPACIDAD 1: GESTION DE ARCHIVOS ---
def motor_archivos():
    while True:
        # VIRGILIO TRABAJA EN LA SOMBRA
        log_path = r'C:\CAMASOTS_V1\MDB\MDB_04_VIRGILIO_LOG.csv'
        with open(log_path, 'a') as f:
            f.write(f"001;SISTEMA;MOTOR_ACTIVO;OK;{datetime.now()}\n")
        time.sleep(300)

# --- CAPACIDAD 2: AUTO-SINCRONIA GITHUB ---
def motor_github():
    while True:
        try:
            # USAREMOS EL REPOSITORIO QUE YA TIENE EN SU GITHUB DESKTOP
            subprocess.run("git add . && git commit -m 'VIRGILIO_AUTO_SYNC' && git push origin master", 
                           shell=True, cwd=r'C:\CAMASOTS_V1', capture_output=True)
        except: pass
        time.sleep(600)

# LANZAMIENTO DEL ICONO Y LOS MOTORES
icon = pystray.Icon("Virgilio G", crear_icono(), "Virgilio G - Operativo")
threading.Thread(target=motor_archivos, daemon=True).start()
threading.Thread(target=motor_github, daemon=True).start()

print("VIRGILIO G: MOTOR REAL INICIADO. CAPACIDADES ACTIVAS.")
icon.run()
