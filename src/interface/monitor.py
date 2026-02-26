import tkinter as tk
from pystray import Icon, Menu, MenuItem
from PIL import Image, ImageDraw
import os

class VirgilioInterface:
    def __init__(self):
        self.icon = None
        self.create_tray()

    def create_image(self):
        img = Image.new('RGB', (64, 64), (75, 0, 130)) # Indigo/Violeta profundo
        d = ImageDraw.Draw(img)
        d.ellipse([10, 10, 54, 54], fill=(138, 43, 226))
        d.text((25, 22), "V", fill="white")
        return img

    def open_lab(self): os.startfile("C:/CAMASOTS_V1")

    def create_tray(self):
        menu = Menu(
            MenuItem("Virgilio: ONLINE", lambda: None, enabled=False),
            MenuItem("Abrir Laboratorio", self.open_lab),
            MenuItem("Cuestionario de Nacimiento", lambda: print("Iniciando DNA...")),
            MenuItem("Desconectar", lambda: self.icon.stop())
        )
        self.icon = Icon("Virgilio", self.create_image(), "Virgilio Agente", menu)
        self.icon.run()

if __name__ == "__main__":
    VirgilioInterface()
