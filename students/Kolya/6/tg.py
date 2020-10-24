import os.path
if not os.path.isfile('secret.txt'):
	name = input('Введите имя бота: ')
	token = input('Введите код: ')
	f = open('secret.txt', 'w')
	f.write(name + ':' + token)
else:
	f = open('secret.txt', 'r')
	mystr = f.read()
	for row in mystr.split(':'):
		print(row)
