import tkinter as tk
from tkinter import simpledialog
import os

def solicitar_token():
    root = tk.Tk()
    root.withdraw()  # Ocultar ventana principal
    token = simpledialog.askstring("🏛️ SEGURIDAD VIRGILIO", "Soberano, introduzca el nuevo GitHub Token:", show='*')
    if token:
        # Guardar localmente en un archivo que el .gitignore ignora
        with open("secrets.token", "w") as f:
            f.write(token)
        print("✅ TOKEN SELLADO LOCALMENTE. Virgilio tiene permiso de subida.")
    else:
        print("❌ ACCESO DENEGADO. Virgilio operará en modo lectura.")
    root.destroy()

if __name__ == "__main__":
    solicitar_token()
    # Aquí arrancaría el Tray Icon después de validar el token
