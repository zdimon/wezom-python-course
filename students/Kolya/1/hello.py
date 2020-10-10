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
'''
import random
while True:
	k = random.randint(1, 10)
	a = int(input('Введите число от 1 до 10: '))
	if a == k:
		break
	else:
		print('Неправильно')