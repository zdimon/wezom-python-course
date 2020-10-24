#@Fffffgfsffbot
import telebot
bot = telebot.TeleBot('1288611759:AAEKGMZM53kZTN7jbAYir1a_dGuEXUS0P_A')
@bot.message_handler(commands=['start'])
def start(message):
	bot.send_message(message.chat.id, 'Привет')
bot.polling()



