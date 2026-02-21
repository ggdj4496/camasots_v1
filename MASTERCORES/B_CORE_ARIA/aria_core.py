import telebot
# EL TOKEN DEBE SER EL TUYO DE BOTFATHER
TOKEN = 'TU_TOKEN_AQUI' 
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.reply_to(message, "dime... mi caballero supremo. aria esta operativa en el b_core. el sistema camasots-v1 te escucha.")

print("aria despertando...")
bot.polling()
