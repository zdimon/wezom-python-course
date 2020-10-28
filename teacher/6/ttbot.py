import telebot

from utils import get_data
data = get_data()

bot = telebot.TeleBot(data['ключ'])
# keyboard1 = telebot.types.ReplyKeyboardMarkup()
# keyboard1.row('Привет', 'Пока')

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Привет, ты написал мне /start')

bot.polling()





# @bot.message_handler(content_types=['text'])
# def send_text(message):
#     if message.text.lower() == 'привет':
#         bot.send_message(message.chat.id, 'Привет, мой создатель')
#     elif message.text.lower() == 'пока':
#         bot.send_message(message.chat.id, 'Прощай, создатель')
#     elif message.text.lower() == 'я тебя люблю':
#         bot.send_sticker(message.chat.id, 'CAADAgADZgkAAnlc4gmfCor5YbYYRAI')

# @bot.message_handler(content_types=['sticker'])
# def sticker_id(message):
#     print(message)

