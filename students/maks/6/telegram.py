print("Я спящий телеграм бот, и я проснулся")

import os.path
if not os.path.isfile("information"):
	name = input("Введите имя бота: ")
	key = input("Введите ваш ключ: ")

	l = open("information.txt", "w")
	str_1 = ("Имя бота: " + name) ; ("\nВаш секретный ключ: " + key)
	l.write(str_1)
	l.close()

else:
	l = open("information.txt", "r")
	str_1 = l.read()
	print(str_1)