const TelegramBot = require('node-telegram-bot-api');
const token = '7891278144:AAHGf055z_4vO_2A_uP7Ff-D0O5R5h_A1_0';
const bot = new TelegramBot(token, {polling: true});
console.log('ARIA: Conectada. Esperando al Amo Leo...');
bot.onText(/ARIA\?\?/, (msg) => { bot.sendMessage(msg.chat.id, 'dime'); });
