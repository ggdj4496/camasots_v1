import telebot
import os

TOKEN = "8507245492:AAHW1LiOD55IKemY9HiUAwUKymmjofJ2hrA"
bot = telebot.TeleBot(TOKEN)
CAJON = "C:/Z_CAMASOTS/CAJON/PROCESANDO"

@bot.message_handler(commands=['start'])
def welcome(message):
    bot.reply_to(message, 'dime, caballero. aria v1 esta en linea y soberana.')

@bot.message_handler(content_types=['document'])
def handle_file(message):
    file_info = bot.get_file(message.document.file_id)
    downloaded = bot.download_file(file_info.file_path)
    with open(f'{CAJON}/{message.document.file_name}', 'wb') as f:
        f.write(downloaded)
    bot.reply_to(message, 'archivo recibido en el cajon. procesando a tope de cola.')

bot.polling()
