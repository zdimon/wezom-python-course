f = open('data.txt', 'r')
string = f.read()
t = []
for row in string.split(';'):
	a = input(row)
	t.append(a)
print(' ')
for row in t:
	print(row)