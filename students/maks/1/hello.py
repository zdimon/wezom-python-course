#print("Hello world")
#print("Какой ваш вес?")
#ves = int(input())
#if ves <= 30:
 #   print("1")
#elif ves > 60:
 #   print("2")
#else:
 #   print("3")

#import random

#while True:
	#a = random.randint(1,10)
	#b = int(input("Введите число от 1 до 10: "))
	#if b == a:
		#print("Угадал")
		#break
	#else:
		#print("Попробуй ещё раз")

import random

b = int(input("Сколько у вас денег?: "))

run1 = True
run2 = True
while run1:	
	a = random.randint(1,2)
	c = int(input("Какая ваша ставка?: "))
	
	if c > b:
		print("Вы не можете поставить денег больше чем у вас есть")
		continue

	d = int(input("Угадайте число 1 или 2: "))

	if d == a:
		c = c * 1.5
		b = b + c
		print("Вы выиграли! Теперь ваша сумма денег составляет:", + int(b))
	else:
		b = b - c
		print("Вы проиграли. Теперь ваша сумма денег составляет:", + int(b))
	
	if int(b) <= 0:
		print("У вас больше нет денег!")
		break

	while run2:
		e = input("Желаете продолжить? (д/н): ")
		if e == "д":
			break
		elif e == "н":
			f = input("Хотите забрать деньги? (д/н): ")
			if f == "д":
				print("Ваши деньги были успешно перечисленны вам на электронный кошелек")
				run1 = False
				run2 = False
			elif f == "н":
				print("Продолжайте")
				break
		else:
			print("Отвечайте только да или нет")