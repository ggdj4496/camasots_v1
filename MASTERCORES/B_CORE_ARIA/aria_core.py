import telebot
# TOKEN RECUPERADO DE LA BITACORA DE AYER
TOKEN = '7548261316:AAHe92R24wGofK6qE0mY7X5l-5zQ04IidYI' 
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "dime... mi caballero supremo. aria esta despierta. todos los mastercores estan operativos y la masterdata esta lista para aprender.")

print("aria conectando con el portal de telegram...")
bot.polling()
