'''
import sys

#sys.argv.pop(0)

for name in sys.argv[1:]:
    print(name)
'''

'''
import sys
import os

for name in sys.argv[1:]:
    try:
        os.remove(name + '.txt')
    except:
        print('Файлы не существуют')
        res = open(name + '.txt', 'w')
'''
# После каждого слова его номер


import sys

#a = str(sys.argv[1])
slov = 0
simv = 0

f = open('test.txt', 'r')
a = f.readlines()
file = []
for line in a:
    for word in line:
        b = line.find(word)
        file.append(b)
        print(file)

    #if line.find(str(sys.argv[1])) != -1:
        #line = line.replace(str(sys.argv[1]), str(sys.argv[2]))
        #print(line)
