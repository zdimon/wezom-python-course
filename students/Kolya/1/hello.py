'''
print('Start')
print('Какой ваш вес?')
a = int(input())
if a <= 30:
	print('Вы худой')
elif a > 60:
	print('Вы полный')
elif a > 30 and a <= 60: 
	print('Вы нормального веса')





import random
o = 10
print('Ваш баланс - ' + str(o))
c = int(input('Какова ваша ставка? '))
if c < o:
	while True:
		k = random.randint(1, 10)
		print('Подсказка: число ' + str(k))
		a = int(input('Введите число от 1 до 10: '))

		if a == k:
			print('Вы угадали')
			o = o * 2
			print('Ваш счёт - ' + str(o))
			b = input('Хотите ли продолжить? ' )
			if b == 'да':
					continue
			else:
				print('Вам выплатят ' + str(o))
				break
		else:
			print('Неправильно')
			b = input('Хотите ли продолжить? ' )
			o = o - c
			if b == 'да':
				if o > 0:
					continue
				else:
					print('Вы банкрот :(')
					break
			else:
				break
else:
	print('Недостаточно средств')
<<<<<<< HEAD
'''
=======
>>>>>>> 206a11545729e623dcaba4ea745946fb5f295f27
