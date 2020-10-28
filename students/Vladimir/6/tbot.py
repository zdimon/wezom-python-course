from telegram.ext import Updater
from telegram.ext import CommandHandler, CallbackContext
from telegram import Bot
import json

print('Привет я спящий бот и я проснулся!')
from utils import get_data

data = get_data()
print(data)
bot = Bot(token=data['ключ'])


def start(update: Updater, context: CallbackContext):
    print("Start command!")
    print(update.message.from_user['username'])
    room_id = update.message.chat_id
    print(room_id)
    quiz = open('question.json', 'r')
    ask = quiz.read()
    a = json.loads(ask)
    q = a[0]['question']
    bot.send_message(room_id, q % update.message.from_user['username'])
    bot.send_photo(room_id, 'face.png')


start_handler = CommandHandler('start', start)

updater = Updater(token=data['ключ'], use_context=True)
updater.dispatcher.add_handler(start_handler)
updater.start_polling()
