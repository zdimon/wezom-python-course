# a = 1

# b = 'blabla'

# # for i in b:
# #     print(i)

# print(b[3])

# d = 'one'
# f = 'two'

# s = d+f



# print(s)

# #b[0] = 'D';

# name = 'Dima'
# name2 = 'Vova'
# name3 = 'Sasha'
# d = 'My name is %s %s %s' % (name, name2, name3)
# print(d)

#import sys

# print(sys.argv)

# for el in sys.argv[1:]:
#     print(el)

# d = [1,2,3,4,5,6]

# f = d[:6]

#f = open('filename','w')
# f.write('  ')
# f.close()
# print(f)
# with open('what', 'w') as f:
#     f.write('blabla')

# import os







#import sys
#import os

#try:
#    os.remove(sys.argv[1])
#except:
#    print('Error')

#print('End programm')
import sys

f = open('test.txt', 'r')
for line in f.readlines():
    line.find(sys.argv[1])
# txt = f.read()

# print(txt)


















