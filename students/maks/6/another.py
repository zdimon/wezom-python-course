import os.path

def get_data():
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
        arr = mystr.split(';')
        bot_name = arr[0]
        key = arr[1]
    
    данные = {
        'имя': bot_name,
        'ключ': key
    }
    return данные

    