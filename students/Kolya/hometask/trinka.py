# -*- coding: utf8 -*-
#@Fffffgfsffbot
import telebot
from telebot import types
import random
from PIL import Image, ImageDraw, ImageFont
carts = {'cherv': [6, 7, 8, 9, 10, 11],
'bubna': [6, 7, 8, 9, 10, 11],
'pika': [6, 7, 8, 9, 10, 11],
'xresta': [6, 7, 8, 9, 10, 11]}
global text
text = '<b>Трынька</b>\n\n'
global balance
balance = 20
global a
a = 1
bot = telebot.TeleBot('1288611759:AAEKGMZM53kZTN7jbAYir1a_dGuEXUS0P_A')
def daykartu():
	masti = ['cherv', 'bubna', 'pika', 'xresta']
	mastiu = {'cherv': [0, 0],
				'bubna': [0, 0],
				'pika': [0, 0],
				'xresta': [0, 0]}
	xix = 0
	tuzi = 0
	mastiu2 = mastiu
	for row in range(3):
		mast = masti[random.randint(0, 3)]
		nominal = carts[mast][random.randint(0, 5)]
		while nominal == 'н':
			nominal = carts[mast][random.randint(0, 5)]
		if nominal == 6:
			xix += 1
		carts[mast][random.randint(0, 5)] = 'н'
		mastiu[mast][0] += 1
		mastiu[mast][1] += nominal
	if xix == 3:
		mastiu = mastiu2
		mastiu[mast][1] = 34
	return mastiu
#@bot.message_handler(commands=['start'])
def show(num, message):
	markup = types.InlineKeyboardMarkup(row_width=3)
	but = types.InlineKeyboardButton(text= 'Упасть', callback_data = 'stop')
	but2 = types.InlineKeyboardButton(text= 'Вскрыться', callback_data = 'go')
	but3 = types.InlineKeyboardButton(text= 'Поставить ещё', callback_data = 'more')
	markup.add(but, but2, but3)
	global text
	text = '<b>Трынька</b>\n\n'
	text += 'Всего очков - %s\n' % (num)
	bot.send_message(message.chat.id, text, reply_markup = markup, parse_mode = 'HTML')
@bot.callback_query_handler(lambda first: first.data == 'go')
def go(call):
	masti = ['cherv', 'bubna', 'pika', 'xresta']
	mastib = daykartu()
	mbwin = False
	for row in masti:
		if mastib[row][0] >= 2:
			mbwin = True
			row2 = row
	if mbwin == True:
		global text
		global a
		text += 'Всего очков бота - %s' % (mastib[row2][1])
		if num > mastib[row2][1]:
			global balance
			bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id, text = text, parse_mode = 'HTML')
			balance += a
			bot.send_message(call.message.chat.id, 'Вы победили')
		elif num < mastib[row2][1]:
			bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id, text = text, parse_mode = 'HTML')
			balance -= a
			bot.send_message(call.message.chat.id, 'Вы проиграли')
		else:
			bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id, text = text, parse_mode = 'HTML')
			bot.send_message(call.message.chat.id, 'Ничья')
	else:
		bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id, text = text + '\nВсего очков бота - 0', parse_mode = 'HTML')
		bot.send_message(call.message.chat.id, 'Вы победили')
	a = 1
	text = '<b>Трынька</b>\n\n'
	start(call.message)
@bot.callback_query_handler(lambda two: two.data == 'stop')
def stop(call):
	global text
	global balance
	bot.edit_message_text(chat_id = call.message.chat.id, message_id = call.message.message_id, text = text + 'Вы упали', parse_mode = 'HTML')
	balance -= a
	text = '<b>Трынька</b>\n\n'
	start(call.message)
@bot.message_handler(commands=['start'])
def start(message):
	#while balance > 0:

	global balance
	bot.send_message(message.chat.id, 'Ваш баланс - %s' % str(balance))
	#while balance > 0:
	global a
	
	bot.send_message(message.chat.id, 'Ваша ставка - %s' % str(a))
	if balance - int(a) > 0:
		masti = ['cherv', 'bubna', 'pika', 'xresta']
		mastiu = daykartu()
		mbwin = False
		for row in masti:
			if mastiu[row][0] >= 2:
				mbwin = True
				row2 = row
		if mbwin == True:
			global num
			num = mastiu[row2][1]
			show(num, message)
		else:

			bot.send_message(message.chat.id, 'Вы проиграли')

			balance -= a
			start(message)
	else:
		bot.send_message(message.chat.id, 'Недостаточно денег.')
		start(message)
@bot.callback_query_handler(lambda three: three.data == 'more')
def more(call):
	global a
	a += 1
	bot.send_message(call.message.chat.id, 'Ваша ставка - %s' % str(a))
	show(num, call.message)
bot.polling()