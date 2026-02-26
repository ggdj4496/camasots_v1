import os
import subprocess
import time
from datetime import datetime

class VirgilioAutopush:
    def __init__(self, interval=60): # Reducido a 60s para máxima respuesta
        self.interval = interval
        self.repo_path = "C:/CAMASOTS_V1"

    def check_and_push(self):
        try:
            os.chdir(self.repo_path)
            status = subprocess.run(["git", "status", "--porcelain"], capture_output=True, text=True).stdout
            if status:
                print(f"[{datetime.now()}] 🔄 Cambios detectados. Sincronizando...")
                subprocess.run(["git", "add", "."])
                subprocess.run(["git", "commit", "-m", f"🤖 AUTO_SYNC: {datetime.now().strftime('%H:%M:%S')}"])
                subprocess.run(["git", "push", "origin", "main"])
        except Exception as e:
            print(f"❌ Error en ciclo: {e}")

if __name__ == '__main__':
    pusher = VirgilioAutopush()
    pusher.run()
