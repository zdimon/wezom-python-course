#import sys
#import os
#sys.argv


#for i in sys.argv[1:]:
	#print(i)



#with open("this", "w") as o:
#	o.write("floar")

#try:
#	os.remove(sys.argv[1])
#except:
#	print("Error")
#print("All good")



#a = open("test.txt", "r")
#for line in a.readlines():
	#b = line.find(sys.argv[1])
	
	#if b > -1:
		#print(line)
		#p = line.replace("can", "cant")
		#print(p)

	#v = line.find(sys.argv[1])
	#if v > -1:
		#l = line.replace(sys.argv[1], sys.argv[2])
		#print(l)

#txt = a.read()
#print(txt)



import sys

summa_correct = 0
summa_wrong = 0

a = input("Укажите ваше имя: ")
print(a + ", пройдите небольшой опрос")

with open(a + ".txt", "w") as que:
	que1 = input("What is 4+4?: ")
	if que1 == "8":
		summa_correct += 1
	else:
		summa_wrong += 1

	que2 = input("What is 3*3?: ")
	if que2 == "9":
		summa_correct += 1
	else:
		summa_wrong += 1

	que3 = input("What is 7-3?: ")
	if que3 == "4":
		summa_correct += 1
	else:
		summa_wrong += 1

	que.write("Количество правильных ответов: " + str(summa_correct))
	que.write("\nКоличество неправильных ответов: " + str(summa_wrong))

print("Спасибо что прошли опрос!")
