import telebot
bot = telebot.TeleBot('1346530025:AAHtDsnGKbnpZi3EW6bu8tGyd_YPCE_NyQg')
@bot.message_handler(commands=['start'])
def start(message):
	bot.send_message(message.chat.id, 'Привет')
bot.polling()


