import os.path
name = input('Введите имя бота: ')
if not os.path.isfile(name + '.txt'):
    key = input('Введите свой ключ: ')
    f = open(name + '.txt', 'w')
    f.write(name + ':' + key)
    f.close()
else:
    f = open(name + '.txt', 'r')
    info = f.read()
    print(info)
    name = info.split(':')[0]
    key = info.split(':')[1]

