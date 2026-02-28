
import telebot, pystray, threading
from PIL import Image, ImageDraw
bot = telebot.TeleBot('8507245492:AAHW1LiOD55IKemY9HiUAwUKymmjofJ2hrA')
@bot.message_handler(func=lambda m: True)
def aria(m):
    if 'ARIA??' in m.text.upper(): bot.reply_to(m, 'dime caballero. sistema en linea.')
def run_tray():
    img = Image.new('RGB', (64, 64), 'green')
    pystray.Icon('Camasots', img, 'Virgilio V1').run()
threading.Thread(target=lambda: bot.infinity_polling(), daemon=True).start()
run_tray()

