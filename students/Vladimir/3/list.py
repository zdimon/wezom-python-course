'''
a = ['Как вас зовут? ','Какая ваша фамилия? ','Сколько вам лет? ']
answer = []
score = 0
while score != 3:
    for quest in a:
        b = input(quest)
        answer.append(b)
    print(answer)
    score += 1
'''

'''
string = 'Привет ;Как дела? '
a = string.split(';')
answer = []
for item in a:
    b = input(item)
    answer.append(b)
print(answer)
'''

'''
f = open('data.txt','r')
txt = f.read()
print(txt)
'''

'''
f = open('data.txt','r')
txt = f.read()
a = txt.split(';')
answer = []
for item in a:
    b = input(item)
    answer.append(b)
print(answer)
'''

'''
string = []
a = 1
s = '-'
while a != 101:
    string.append(str(a))
    a += 1
s = s.join(string)
print(s)
'''

'''
f = open('name.txt','r')
txt = f.read()
a = txt.split(';')
f = open('name1.txt','w')
for name in a:
    f.write(str(name) + ':')
'''

f = open('name.txt','r')
txt = f.read()
a = txt.split(';')
a = txt.split('\n')
file = []
for name in a:
    b = name.split(';')
    file.append(b)
print(file)
for name_file in file:
    for res in name_file:
        res = open(res + '.txt', 'w')





