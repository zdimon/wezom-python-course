from telegram.ext import Updater
from telegram.ext import CommandHandler, CallbackContext, CallbackQueryHandler
from telegram import Bot
import json
from telegram import InlineKeyboardButton, InlineKeyboardMarkup

f = open('question.json', 'r')
jsondata = json.loads(f.read())
f.close()

print('Привет, я спящий бот и я проснулся!')
from utils import get_data
data = get_data()
print(data)
bot = Bot(token=data['ключ'])

def build_menu(buttons,n_cols):
    menu = [buttons[i:i + n_cols] for i in range(0, len(buttons), n_cols)]
    return menu

def press_button(update: Updater, context: CallbackContext):
    print("Pressing button %s" % update.callback_query.data)

def start(update: Updater, context: CallbackContext):
    print("Start command!")
    print(update.message.from_user['username'])
    room_id = update.message.chat_id
    print(jsondata[0]['question'])
    bot.send_message(room_id,jsondata[0]['question'])
    bot.send_photo(chat_id=room_id, photo=open('face.png', 'rb'))

    button_list = []
    button_list.append(InlineKeyboardButton('Test 1',callback_data='one'))
    button_list.append(InlineKeyboardButton('Test 2',callback_data='two'))
    button_list = InlineKeyboardMarkup(build_menu(button_list,n_cols=1))
    bot.send_message(room_id, 'Buttons', reply_markup=button_list)


start_handler = CommandHandler('start', start)

updater = Updater(token=data['ключ'], use_context=True)
updater.dispatcher.add_handler(start_handler)
<<<<<<< HEAD
updater.start_polling() 
=======
updater.dispatcher.add_handler(CallbackQueryHandler(press_button))
updater.start_polling()  
>>>>>>> 2555044369a4c466242d79e763c3a5e97799191b










