import os, shutil, ctypes, winreg
from pathlib import Path

def full_install():
    if not ctypes.windll.shell32.IsUserAnAdmin():
        print("Requiere privilegios de Administrador.")
        return

    sys_path = Path(os.environ["ProgramFiles"]) / "Virgilio_Core"
    sys_path.mkdir(exist_ok=True)
    shutil.copytree("C:/CAMASOTS_V1/src", sys_path / "src", dirs_exist_ok=True)
    
    # Persistencia en Registro
    with winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Run", 0, winreg.KEY_SET_VALUE) as key:
        winreg.SetValueEx(key, "Virgilio_Core", 0, winreg.REG_SZ, f'pythonw "{sys_path}/src/CORE/brain.py"')
    
    print("INSTALACIÓN MILITAR COMPLETADA.")

if __name__ == "__main__":
    full_install()
