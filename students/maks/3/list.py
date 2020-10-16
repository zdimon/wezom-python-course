#string = "Привет;Как дела?"
#a = string.split(";")

#for item in a:
#	b = input(item + ": ")
#answer = []
#answer.append(b)
#print(answer)


#h = open("turtle.txt","r")
#roll = h.read()
#print(roll)


#low = []
#for i in range(1,101):
#	low.append(i)

#s = "-"
#l = s.join(str(x) for x in low)
#print(l)


import random

faces = [1,2,3,4]
cards = [2,3,4,5,6,7,8,9,10]

run1 = True

deck = cards * 4
random.shuffle(deck)

x = deck.pop()
y = deck.pop()

print("Ваши карты: " + str(x) + ", " + str(y))
summa_p = x + y
print("Общее количество очков: " + str(summa_p))
summa_d = 0

while run1:
	take = input("Хотите взять ещё? (д/н): ")
	if take == "д":
		z = deck.pop()
		print("Вам попалась карта: " + str(z))
		summa_p += z
		print("Теперь у вас " + str(summa_p) + " очков")
			
		if summa_p > 21:
			print("Вы проиграли. Количество ваших очков должно быть меньше чем 21")
			exit(0)
			#again = input("Хотите заново начать игру? (д/н): ")

				#if again == "д":

	elif take == "н":
		print("Ждите, пока дилер возьмёт карты")
		while summa_d <= 18:
			c = deck.pop()
			summa_d += c
			print("Дилер взял карту: " + str(c))
			print("Теперь у него: " + str(summa_d) + " очков")
			run1 = False

			if summa_d > 21:
				print("Вы выиграли! Дилер набрал больше чем 21 очко!")
				exit(0)

	else:
		print("Отвечайте только да или нет")

if summa_d > summa_p:
	print("Дилер выиграл. У него больше очков чем у вас.")
elif summa_d < summa_p:
	print("Вы выиграли! У вас больше очков чем у Дилера!")
else:
	print("Ничья. Никто не выиграл.")