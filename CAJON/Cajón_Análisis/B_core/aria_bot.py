import telebot
import time

# AQUÍ PONDREMOS EL TOKEN DE TELEGRAM
TOKEN = 'TU_TOKEN_DE_TELEGRAM_AQUÍ'

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "¡Hola, Arquitecto! ARIA (B_core) reportándose. El sistema Zbrain está online.")

@bot.message_handler(func=lambda m: True)
def echo_all(message):
    if "ARIA?" in message.text.upper():
        bot.reply_to(message, "dime") # Respuesta dulce y técnica solicitada
    elif "status" in message.text.lower():
        bot.reply_to(message, "Arquitecto, el laboratorio Camasots está sincronizado con GitHub. Los proyectos en el cajón están listos.")

print("ARIA está escuchando...")
bot.polling()
