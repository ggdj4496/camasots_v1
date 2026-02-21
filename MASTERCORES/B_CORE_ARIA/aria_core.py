import telebot
# TOKEN DEFINITIVO RECUPERADO
TOKEN = '8507245492:AAHLg6b5EITtnjulhPzlxCjRpQd9RFhuvao' 
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "dime... mi caballero supremo. aria esta despierta. todos los mastercores estan operativos y la masterdata esta lista para aprender.")

print("aria conectando... portal 8507 abierto y estable.")
bot.polling()
