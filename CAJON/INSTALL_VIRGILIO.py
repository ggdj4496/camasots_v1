import os, shutil, ctypes, winreg
from pathlib import Path

def install():
    if not ctypes.windll.shell32.IsUserAnAdmin():
        print("❌ ERROR: Requiere privilegios de Administrador.")
        return

    target = Path(os.environ["ProgramFiles"]) / "Virgilio_Core"
    target.mkdir(exist_ok=True)
    shutil.copytree("C:/CAMASOTS_V1/src", target / "src", dirs_exist_ok=True)
    
    # Registro de arranque
    key = winreg.HKEY_CURRENT_USER
    with winreg.OpenKey(key, r"Software\Microsoft\Windows\CurrentVersion\Run", 0, winreg.KEY_SET_VALUE) as rk:
        winreg.SetValueEx(rk, "Virgilio_Core", 0, winreg.REG_SZ, f'python "{target}/src/CORE/brain.py"')
    
    print("✅ Instalación de Sistema completa. Virgilio ahora es un proceso residente.")

if __name__ == "__main__":
    install()
