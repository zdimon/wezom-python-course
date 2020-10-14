b = []
i = False
for row in range(64):
	if row % 8 == 0:
		if i == True:
			i = False
		else:
			i = True
	if i == True:
		b.append('б')
		i = False
	else:
		b.append('ч')
		i = True
	
k = 0
for rrr in range(8):
	pr = ''
	for row in range(k, k + 8):
		pr = pr + '|' + b[row]
	print(pr)
	k = k + 8
