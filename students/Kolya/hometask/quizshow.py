import json
f = open('quiz.json', 'r')
txt = f.read()
a = json.loads(txt)
name = input('Введите ваше имя: ')
i = 0
for row in a:
	answer = input(row['question'] + ' ')
	for row2 in row['answers']:
		if row2['true'] == 1:
			if row2['text'] == answer:
				i += 1
print('Опрос окончен.')
f = open(name + '.txt', 'w')
f.write('Правильных ответов: ' + str(i))
