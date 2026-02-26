from pystray import Icon, Menu, MenuItem
from PIL import Image, ImageDraw

def create_image(color):
    img = Image.new('RGB', (64, 64), color)
    d = ImageDraw.Draw(img)
    d.text((20,20), "V", fill="white")
    return img

icon = Icon("Virgilio", icon=create_image("purple"))
icon.run()
