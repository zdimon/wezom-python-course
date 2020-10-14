a = ['Как вас зовут? ','Какая ваша фамилия? ','Сколько вам лет? ']
answer = []
score = 0
while score != 3:
    for quest in a:
        b = input(quest)
        answer.append(b)
    print(answer)
    score += 1

