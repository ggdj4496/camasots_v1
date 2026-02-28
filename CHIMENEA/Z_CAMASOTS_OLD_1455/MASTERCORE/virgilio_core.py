import os
import json
import time
from datetime import datetime

class MasterCore:
    def __init__(self):
        self.root = "C:/Z_CAMASOTS"
        self.data = f"{self.root}/DATA"
        self.cajon = f"{self.root}/CAJON/PROCESANDO"
        
    def escribir_bit(self, mdb_id, subcat, detalle):
        archivo = f"{self.data}/MDB_{mdb_id}.csv"
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        linea = f"BIT_{int(time.time())};{mdb_id};{subcat};{detalle};OK;{timestamp}\n"
        with open(archivo, 'a', encoding='utf-8') as f:
            f.write(linea)

if __name__ == '__main__':
    core = MasterCore()
    print('VIRGILIO MASTERCORE ONLINE - REGLA DE ORO ACTIVA')
    core.escribir_bit('01_MASTERCORE', 'SISTEMA', 'NUCLEO PY MATERIALIZADO')
