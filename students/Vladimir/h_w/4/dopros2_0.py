score_right = 0
score_wrong = 0
number = 0
name = input('Введите свое имя: ')
# Очищаем файл если он уже существует
answers_p = open(name + '.txt', 'w'); answers_p.close()
file = open('questions.txt', 'r')
answer = open('answers.txt', 'r')
right_answers = answer.readlines()
for question in file:
    print(question)
    a = input('Введите ответ: ')
    answers_p = open(name + '.txt', 'a')
    ans = a + '\n'
    answers_p.write(ans)
    answers_p.close()
    if ans == right_answers[number]:
        score_right += 1
    else:
        score_wrong += 1
    number += 1
answers_p = open(name + '.txt', 'a')
answers_p.write('Right answers: ' + str(score_right) + '\nWrong answers: ' + str(score_wrong))
answers_p.close()
file.close()
