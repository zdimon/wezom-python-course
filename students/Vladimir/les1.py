'''
print('Какой ваш вес?')
ves = int(input())
print(ves)
if ves <= 30:
    print('Вы худой')
elif ves > 60:
    print('Вы толстый')
else:
    print('Ваш вес нормальный')
'''

import random
while True:
    k = random.randint(1,10)
    a = int(input('Введите число от 1 до 10: '))
    if a == k:
        break
    else:
        print('Неправильно')
        b = input('Хотите ли продолжить? ')
        if b == 'да':
            continue
        else:
            break

