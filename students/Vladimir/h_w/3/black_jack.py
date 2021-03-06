"""
Дано два списка, с 4-мя мастями и 9 картами.

    faces = [1,2,3,4]
    cards = [2,3,4,5,6,7,8,9,10]

Необходимо создать новый список колоды карт, в которой будет 36 карт по 9 каждой масти.
При этом числа будут повторятся т.е. в колоде будет четыре двойки, четыре тройки и т.д.

В начале игры (запуске программы) пользователю сдается 2 случайные карты (числа).
Подсчитывается кол-во набранных очков, и выводится результат и предложение взять еще карту или отказаться.

Например:

У вас такие карты - 3,5 общее количество очков - 8
Хотите взять еще? д\н

Если пользователь соглашается, ему выдается еще одна карта и процесс повторяется пока будет набрано больше 21 очка.

В этом случае пользователю говорят что он проиграл и предлагают повторить игру или выйти из программы.

В случае если пользователь отказывается брать карту вступает в игру компьютер.

Он берет случайные карты до тех пор пока не наберет от 18 очков (включительно) до 21.

Если количество баллов, набранных компьютером находится между 18 и 21 компьютер прекращает брать карты,
сравнивает свои очки с очками пользователя и определяет победителя или ничью.

Если компьютер набрал больше 21 то он проигрывает и пользователю предлагается продолжить игру или выйти.
"""

import random

faces = [1, 2, 3, 4]
cards = [2, 3, 4, 5, 6, 7, 8, 9, 10]
deck = []

# Создаем колоду
for suit in faces:
    for x in cards:
        deck.append(x)


# Выдаем карты и подсчитывае очки
def game():
    score_p = 0
    score_c = 0
    player = random.sample(deck, 2)
    for point in player:
        score_p += point
    print('У вас такие карты: ', player)
    print('Общее количество очков: ', score_p)
    a = input('Хотите взять еще карту?(д/н) ')
    while a == 'д':
        point = random.choice(deck)
        player.append(point)
        score_p += point
        import pdb; pdb.set_trace()
        print('У вас такие карты: ', player)
        print('Общее количество очков: ', score_p)
        if score_p > 21:
            a = input('Вы проиграли, хотите повторить?(д/н) ')
            if a == 'д':
                game()
            else:
                print('Спасибо за игру!!!')
                exit()
        a = input('Хотите взять еще карту?(д/н) ')
        if a == 'н':
            break
    if a == 'н':
        computer = random.sample(deck, 2)
        for point in computer:
            score_c += point
        while score_c <= 18:
            point = random.choice(deck)
            computer.append(point)
            score_c += point
        if score_c > 21:
            print('Ваши карты: ', player, '\nВаши очки: ', score_p, '\nКарты ИИ: ', computer, '\nОчки ИИ: ', score_c)
            a = input('Вы победили!!! Сыграете еще раз?(д/н) ')
            if a == 'д':
                game()
            else:
                print('Спасибо за игру!!!')
        elif score_p < score_c < 21:
            print('Ваши карты: ', player, '\nВаши очки: ', score_p, '\nКарты ИИ: ', computer, '\nОчки ИИ: ',
                  score_c)
            a = input('Вы проиграли. Желаете сыграть еще раз?(д/н) ')
            if a == 'д':
                game()
            else:
                print('Спасибо за игру!!!')


game()

'''
while a != 'д' or 'н':
    a = input('Укажите "д" или "н": ')
'''

'''
if a != 'д' or 'н':
    while True:
        a = input('Укажите "д" или "н": ')
        if a == 'д' or 'н':
            break
'''
