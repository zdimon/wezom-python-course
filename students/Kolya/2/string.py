
f = open('data.txt', 'r')
string = f.read()
t = []
s = ';'
i = 1
for row in string.split(':'):
	k = i
	for row2 in row.split('\n'):
		if i == k:
			t.append(str(i) + ' - ' + row2)
			i = i + 1
		else:
			t.append(str(i) + ' - ' + row2)
			i = i + 1
print(t)
#for row in t:
#	f = open(row + '.txt', 'w')
'''
pr = []
s = '-'
for row in range(0, 101):
	pr.append(str(row))
s = s.join(pr)
print(s)

'''