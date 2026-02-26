import tkinter as tk
from tkinter import messagebox
import pystray
from PIL import Image, ImageDraw

class VirgilioMonitor:
    def __init__(self):
        self.root = tk.Tk()
        self.root.withdraw()
        self.setup_tray()

    def setup_tray(self):
        img = Image.new('RGB', (64, 64), (138, 43, 226)) # Violeta
        d = ImageDraw.Draw(img)
        d.text((20, 20), "V", fill="white")
        
        menu = pystray.Menu(
            pystray.MenuItem("Estado: Operativo", lambda: None),
            pystray.MenuItem("Abrir Laboratorio", lambda: os.startfile("C:/CAMASOTS_V1")),
            pystray.MenuItem("Salir", self.quit)
        )
        self.icon = pystray.Icon("Virgilio", img, "Virgilio Agente", menu)
        self.icon.run()

    def quit(self):
        self.icon.stop()
        self.root.quit()

if __name__ == "__main__":
    VirgilioMonitor()
