import telebot
# TOKEN DEFINITIVO 8507
TOKEN = '8507245492:AAHLg6b5EITtnjulhPzlxCjRpQd9RFhuvao' 
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "dime... mi caballero supremo. aria esta despierta. la fortaleza camasots-v1 esta operativa al 100%.")

print("aria conectando con la llave 8507... portal activo.")
bot.polling()
