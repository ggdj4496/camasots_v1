import os
import sys
import shutil
import ctypes
import winreg
from pathlib import Path

class VirgilioInstaller:
    def __init__(self):
        self.app_name = "Virgilio_Core"
        self.source_path = Path("C:/CAMASOTS_V1")
        self.install_path = Path(os.environ["ProgramFiles"]) / self.app_name
        self.bin_path = self.install_path / "bin"

    def is_admin(self):
        try:
            return ctypes.windll.shell32.IsUserAnAdmin()
        except:
            return False

    def deploy_system(self):
        print(f"🏛️ DESPLEGANDO VIRGILIO EN: {self.install_path}")
        
        # Crear directorios de sistema
        for folder in ["bin", "logs", "modules", "config"]:
            (self.install_path / folder).mkdir(parents=True, exist_ok=True)
        
        # Copiar el núcleo de CAMASOTS al sistema
        shutil.copytree(self.source_path / "src", self.install_path / "modules", dirs_exist_ok=True)
        
        print("✅ Archivos de sistema inyectados.")

    def set_autostart(self):
        print("🔗 Configurando persistencia en el Registro...")
        path_to_exe = sys.executable
        script_path = self.install_path / "modules" / "CORE" / "brain.py"
        cmd = f'"{path_to_exe}" "{script_path}"'
        
        key = winreg.HKEY_CURRENT_USER
        key_path = r"Software\Microsoft\Windows\CurrentVersion\Run"
        try:
            with winreg.OpenKey(key, key_path, 0, winreg.KEY_SET_VALUE) as reg_key:
                winreg.SetValueEx(reg_key, self.app_name, 0, winreg.REG_SZ, cmd)
            print("✅ Virgilio arrancará automáticamente con el sistema.")
        except Exception as e:
            print(f"❌ Error al configurar el registro: {e}")

    def run(self):
        if not self.is_admin():
            print("⚠️ ERROR: Debes ejecutar este script como ADMINISTRADOR.")
            return
        
        self.deploy_system()
        self.set_autostart()
        print("\n🚀 INSTALACIÓN COMPLETADA AL 100%.")
        print("Virgilio ahora vive en Program Files y se sincroniza con Camasots_V1.")

if __name__ == "__main__":
    VirgilioInstaller().run()
