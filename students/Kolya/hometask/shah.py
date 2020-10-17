import random
cards = [2,3,4,5,6,7,8,9,10]
coloda = []
vzyal = []
chisla = 0
def it():
	while True:
		i = random.randint(0, 35)
		if i not in vzyal:
			break
			vzyal.append(i)
		else:
			continue
	return i
for row in cards:
	for r in range(4):
		coloda.append(row)
random.shuffle(coloda)
for row in range(2):
	i = random.randint(0, 35)
	print('Ваше число - ' + str(coloda[i]))
	chisla += coloda[i]
	vzyal.append(i)
print('Общий счёт - ' + str(chisla))
while True:
	a = input('Хотите ли взять ещё карту? ')
	if a == 'да':
		i = it()
		print('Ваше число - ' + str(coloda[i]))
		chisla += coloda[i]
		print('Общий счёт - ' + str(chisla))
		if chisla < 22:
			continue
		else:
			print('Вы проиграли :(')
			break
	else:
		fl = coloda[it()]
		sl = coloda[it()]
		chisla2 = fl + sl
		while chisla2 < 22:
			irr = it()
			chisla2 + coloda[irr]
			if chisla2 > 21:
				print('Вы победили :)')
				chisla2 = 0
				break
			else:
				break
		print(chisla2)
		if chisla > chisla2:
			print('Вы победили :)')
			break
		elif chisla < chisla2:
			print('Вы проиграли :(')
			break
		else:
			print('Ничья -_-')
			break



