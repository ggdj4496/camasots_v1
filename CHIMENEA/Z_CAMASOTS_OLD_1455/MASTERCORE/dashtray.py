import pystray
from pystray import MenuItem as item
from PIL import Image, ImageDraw
import os

def create_image(color):
    image = Image.new('RGB', (64, 64), color)
    dc = ImageDraw.Draw(image)
    dc.polygon([(10, 10), (32, 54), (54, 10)], fill='white')
    return image

def on_quit(icon, item):
    icon.stop()

icon = pystray.Icon("Camasots", create_image('blue'), "Camasots V1 - Caballero")
icon.menu = pystray.Menu(item('Cerrar Sistema', on_quit))
icon.run()
