score_right = 0
score_wrong = 0
number = 0
name = input('Введите свое имя: ')
#import pdb
#pdb.set_trace()
# Очищаем файл если он уже существует
answers_p = open(name + '.txt', 'w')
answers_p.close()
file = open('questions.txt', 'r')
answer = open('answers.txt', 'r')
right_answers = answer.readlines()
# import pdb
# pdb.set_trace()
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
print(score_right)
print(score_wrong)
file.close()
