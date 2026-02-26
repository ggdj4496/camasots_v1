import os, subprocess, time, threading
from datetime import datetime

class VirgilioBrain:
    def __init__(self):
        self.state = "VERDE"
        self.repo = "C:/CAMASOTS_V1"
        
    def autopush_loop(self):
        while True:
            os.chdir(self.repo)
            status = subprocess.run(["git", "status", "--porcelain"], capture_output=True, text=True).stdout
            if status:
                subprocess.run(["git", "add", "."])
                subprocess.run(["git", "commit", "-m", f"🤖 AUTO_EVOLVE: {datetime.now().strftime('%H:%M:%S')}"])
                subprocess.run(["git", "push", "origin", "main"])
            time.sleep(60)

    def startup(self):
        print("🏛️ VIRGILIO CORE: ONLINE")
        threading.Thread(target=self.autopush_loop, daemon=True).start()

if __name__ == '__main__':
    VirgilioBrain().startup()
    while True: time.sleep(1)
