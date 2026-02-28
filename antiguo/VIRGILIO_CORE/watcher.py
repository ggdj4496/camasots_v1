import os, time
path_to_watch = r'C:\Users\X\Desktop\VIRGILIO_CORE\DEUDAS_PDF'
print(f'👀 ESCÁNER ACTIVO: Vigilando {path_to_watch}')
while True:
    files = os.listdir(path_to_watch)
    if files:
        print(f'[!] ARCHIVO DETECTADO: {files[0]}')
        print('[!] Analizando intereses de usura...')
        # Aquí Virgilio procesará el PDF
    time.sleep(5)
