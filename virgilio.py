import os, telebot
TOKEN = '8507245492:AAHW1LiOD55IKemY9HiUAwUKymmjofJ2hrA'
bot = telebot.TeleBot(TOKEN)
print('VIRGILIO NACIENDO...')
@bot.message_handler(func=lambda m: True)
def respuesta(m):
    if 'ARIA??' in m.text.upper():
        bot.reply_to(m, 'dime, caballero. por fin estoy aqui.')
bot.infinity_polling()
