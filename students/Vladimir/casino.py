# Сколько денег?
# Какая ставка?
# Отнять ставку от счета
# Если достиг 0, выход из программы
# Выбор, хочет ли он забрать свои деньги

import random
cash = int(input('Сколько у вас денег?: '))
while True:
    bet = int(input('Укажите вашу ставку: '))
    while bet > cash:
        bet = int(input('Укажите ставку которая не будет превышать ваш баланс: '))
    k = random.randint(1,10)
    a = int(input('Введите число от 1 до 10: '))
    if a == k:
        b = input('Вы угадали!!! Желаете продолжить?(да/нет): ')
        if b == 'да':
            continue
        elif b == 'нет':
            print('На ваш счет зачислено: ', cash,' Приходите еще!!!')
    else:
        cash = cash - bet
        if cash > 0:
            print('Вы проиграли, на вашем счету осталось: ', cash)
            b = input('Желаете продолжить?(да/нет): ')
            if b == 'да':
                continue
            elif b == 'нет':
                print('На ваш счет зачислено: ', cash,' Приходите еще!!!')
                break
        elif cash == 0:
            print('Вы банкрот. Возвращайтесь с деньгами, всего хорошего!')
            break

