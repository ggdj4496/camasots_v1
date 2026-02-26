import os, subprocess, time, threading, json
from datetime import datetime

class VirgilioCore:
    def __init__(self):
        self.root = "C:/CAMASOTS_V1"
        self.status = "VERDE"
        self.config_path = os.path.join(self.root, "database/config.json")

    def log(self, message):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(os.path.join(self.root, "NOTIFICACIONES_MAESTRAS.txt"), "a", encoding='utf-8') as f:
            f.write(f"[{timestamp}] {message}\n")

    def autopush(self):
        while True:
            try:
                os.chdir(self.root)
                diff = subprocess.run(["git", "status", "--porcelain"], capture_output=True, text=True).stdout
                if diff:
                    subprocess.run(["git", "add", "."])
                    subprocess.run(["git", "commit", "-m", f"🤖 AUTO_EVOLVE: {datetime.now().strftime('%H:%M:%S')}"])
                    subprocess.run(["git", "push", "origin", "main"])
                    self.log("Sincronización con GitHub completada exitosamente.")
            except Exception as e:
                self.log(f"Error en Autopush: {e}")
            time.sleep(60)

    def run(self):
        self.log("Virgilio Core iniciado. Modo Soberano Activo.")
        threading.Thread(target=self.autopush, daemon=True).start()
        while True: time.sleep(1)

if __name__ == "__main__":
    VirgilioCore().run()
