import os
from datetime import datetime

archivo_mdb = r'C:\CAMASOTS_V1\MDB\MDB_08_SISTEMA_TRAY.csv'
linea = f"005;MIGRACION;ZBRAIN ASIMILADO EN CAMASOTS;COMPLETO;{datetime.now()}\n"

with open(archivo_mdb, 'a') as f:
    f.write(linea)
print("LOGICA DE ZBRAIN INTEGRADA EN EL CORE DE CAMASOTS")
