import os.path
def get_data():
	if not os.path.isfile('secret.txt'):
		name = input('Введите имя бота: ')
		kod = input('Введите код: ')
		f = open('secret.txt', 'w')
		f.write(name + ' ' + kod)
		data = {'имя': name, 'код': kod}
	else:
		f = open('secret.txt', 'r')
		mystr = f.read().split(' ')
		name =  mystr[0]
		kod = mystr[1]
		data = {'имя': name, 'код': kod}
	return data