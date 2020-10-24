#1346530025:AAHtDsnGKbnpZi3EW6bu8tGyd_YPCE_NyQg
from telegram.ext import Updater
from telegram.ext import CommandHandler, CallbackContext
from telegram import Bot
import json
f = open('question.json', 'r')
txt = f.read()
a = json.loads(txt)
from get_data import get_data
data = get_data()
bot = Bot(token=data['код'])

def start(update: Updater, context: CallbackContext):
    room_id = update.message.chat_id
    bot.send_message(room_id,a[0]['question']%update.message.from_user.username)


start_handler = CommandHandler('start', start)

updater = Updater(token=data['код'], use_context=True)
updater.dispatcher.add_handler(start_handler)
updater.start_polling()  



