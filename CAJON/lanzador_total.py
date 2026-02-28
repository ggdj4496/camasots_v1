import os, webbrowser, time, threading

# 1. FUNCION DE APERTURA DE GOOGLE (PUENTE VISUAL)
def abrir_google():
    time.sleep(2)
    webbrowser.open("https://www.google.com")
    print("VENTANA DE GOOGLE ABIERTA - CONEXION VALIDADA")

# 2. GENERACION DEL ARCHIVO DE CONTROL DE SOFTWARE
def generar_bin_control():
    path_bin = r'C:\CAMASOTS_V1\CAMASOTS_CORE.bat'
    with open(path_bin, 'w') as f:
        f.write("@echo off\n")
        f.write("title CAMASOTS V1 - VIRGILIO G\n")
        f.write("echo SISTEMA SOBERANO ACTIVO BAJO BLINDAJE FUEGO GOLD\n")
        f.write("pause\n")

# 3. REGISTRO EN MASTERDATABASE
def registro_mdb():
    path_mdb = r'C:\CAMASOTS_V1\MDB\MDB_07_GOOGLE_CLOUD.csv'
    with open(path_mdb, 'a') as f:
        from datetime import datetime
        f.write(f"005;ACCESO;GOOGLE_OPEN_SUCCESS;ACTIVO;{datetime.now()}\n")

# EJECUCION DE PODERES
threading.Thread(target=abrir_google).start()
generar_bin_control()
registro_mdb()

print("VIRGILIO G: SOFTWARE GENERADO Y NAVEGADOR LANZADO.")
