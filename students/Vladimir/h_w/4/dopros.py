"""
Спросить имя пользователя и сохранить его.

Прочитать файл questions.txt и последовательно задать вопросы пользователю.

Проверить ответы из файла answers.txt

Записать результаты в файл и назвать его именем пользователя.

В результатх указать количество правильных и не правильных ответов.
"""

score_right = 0
score_wrong = 0
name = input('Введите свое имя: ')
# Очищаем файл если он уже существует
answers_p = open(name + '.txt', 'w'); answers_p.close()
file = open('questions.txt', 'r')
# Задаем вопросы и получем ответы, записываем в файл с именем игрока
for quest in file:
    print(quest)
    a = input('Введите ответ: ')
    answers_p = open(name + '.txt', 'a')
    answers_p.write(a + '\n')
file.close()
answers_p.close()

number = 0
file_1 = open(name + '.txt', 'r')
file_2 = open('answers.txt', 'r')
answers_p = file_1.readlines()
right_answers = file_2.readlines()
for ans in right_answers:
    if answers_p[:number] == right_answers[:number]:
        score_right += 1
    else:
        score_wrong += 1
    number += 1
file_1.close(); file_1 = open(name + '.txt', 'a')
file_2.close()
file_1.write('Right answers: ' + str(score_right) + '\nWrong answers: ' + str(score_wrong))







