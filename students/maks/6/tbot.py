from telegram.ext import Updater
from telegram.ext import CommandHandler, CallbackContext
from telegram import Bot



print('Привет, я спящий бот и я проснулся!')
from utils import get_data
data = get_data()
print(data)
bot = Bot(token=data['ключ'])

def start(update: Updater, context: CallbackContext):
    print("Start command!")
    print(update.message.from_user['username'])
    room_id = update.message.chat_id
    print(room_id)
    bot.send_message(room_id,'Hello. How are you?')
    bot.send_photo(chat_id=room_id, photo=open("apple.png", "rb"))


start_handler = CommandHandler('start', start)

updater = Updater(token=data['ключ'], use_context=True)
updater.dispatcher.add_handler(start_handler)
updater.start_polling() 







