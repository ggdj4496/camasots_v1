import telebot
import time
import sys

TOKEN = '7548261316:AAHe92R24wGofK6qE0mY7X5l-5zQ04IidYI'

def lanzar_aria():
    while True:
        try:
            bot = telebot.TeleBot(TOKEN)
            @bot.message_handler(commands=['start'])
            def send_welcome(message):
                bot.reply_to(message, "dime... mi caballero supremo. aria ha vencido el bloqueo. los mastercores estan al 100%.")
            
            print("aria: intentando conexion maestra...")
            bot.remove_webhook() # LIMPIEZA DE TUNEL
            bot.polling(none_stop=True)
        except Exception as e:
            print(f"fallo de conexion: {e}. reintentando en 5 segundos...")
            time.sleep(5)

if __name__ == '__main__':
    lanzar_aria()
