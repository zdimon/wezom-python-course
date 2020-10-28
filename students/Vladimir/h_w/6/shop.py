import json
import telebot


f = open('mouse.json', 'r')
f1 = open('keyboard.json', 'r')
f2 = open('headphones.json', 'r')
data = f.read()
data1 = f1.read()
data2 = f2.read()
mouse = json.loads(data)
razer_m = mouse[0]
steelseries_m = mouse[1]
bloody_m = mouse[2]
a4tech_m = mouse[3]
keyboard = json.loads(data1)
aula_k = keyboard[0]
logitech_k = keyboard[1]
hyperx_k = keyboard[2]
msi_k = keyboard[3]
headphones = json.loads(data2)
razer_h = headphones[0]
sven_h = headphones[1]
huperx_h = headphones[2]
jbl_h = headphones[3]
f.close()
f1.close()
f2.close()






bot = telebot.TeleBot('1269980207:AAEty6BwPGh9u3osCIukji9_MSQz43m9h1w')
keyboard = telebot.types.ReplyKeyboardMarkup(True)
keyboard.row('Нет', 'Да')
order = telebot.types.InlineKeyboardButton(text='Добавить в корзину')


@bot.message_handler(commands=['start'])
def start_message(message):
    markup = telebot.types.InlineKeyboardMarkup()
    markup.add(telebot.types.InlineKeyboardButton(text='Мышь', callback_data=1))
    markup.add(telebot.types.InlineKeyboardButton(text='Клавиатуру', callback_data=2))
    markup.add(telebot.types.InlineKeyboardButton(text='Наушники', callback_data=3))
    bot.send_message(message.chat.id, text="Здравствуйте! Добро пожаловать в наш магазин!\nЧто вы желаете приобрести?",
                     reply_markup=markup)

@bot.callback_query_handler(func=lambda call: True)
def query_handler(call):

    bot.answer_callback_query(callback_query_id=call.id, text='Модели что есть в наличии')
    if call.data == '1':
        bot.send_photo(call.message.chat.id, open(razer_m['Photo'], 'rb'))
        bot.send_message(call.message.chat.id, 'Цена: ' + razer_m['Cost'], reply_markup=order)
        bot.send_photo(call.message.chat.id, open(steelseries_m['Photo'], 'rb'))
        bot.send_message(call.message.chat.id, 'Цена: ' + steelseries_m['Cost'], reply_markup=order)
        bot.send_photo(call.message.chat.id, open(bloody_m['Photo'], 'rb'))
        bot.send_message(call.message.chat.id, 'Цена: ' + bloody_m['Cost'], reply_markup=order)
        bot.send_photo(call.message.chat.id, open(a4tech_m['Photo'], 'rb'))
        bot.send_message(call.message.chat.id, 'Цена: ' + a4tech_m['Cost'], reply_markup=order)
    elif call.data == '2':
        print()
    elif call.data == '3':
        print()

    bot.edit_message_reply_markup(call.message.chat.id, call.message.message_id)




bot.polling()
