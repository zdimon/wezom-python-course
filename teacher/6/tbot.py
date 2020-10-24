print('Привет я спящий бот и я проснулся!')
import os.path

if not os.path.isfile('secret'):
    bot_name = input('Имя бота:')
    secret = input('Cекретный ключ:')

    f = open('secret','w')
    mystr = '%s:%s' % (bot_name,secret)
    f.write(mystr)
    f.close()
else:
    f = open('secret','r')
    mystr = f.read()
    print(mystr) 
