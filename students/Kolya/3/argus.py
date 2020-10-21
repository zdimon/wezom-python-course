
import sys
#a = sys.argv

#for row in range(1, len(a)):
#r = a[1]
#t = a[2]
'''
	#f = open(a[row] + '.txt', 'w')
	#f.close()
	
	#time.sleep(7)
try:
	print('h' + 1)
except:
	print('g')
print('f')
'''
with open('test.txt', 'r') as f:
	slov = 0
	simv = 0
	for row in f.readlines():
		row = row.strip()
		a = row.split(' ')
		row = ''
		i = 0
		for rok in a:
			simv += len(rok)
			slov += 1
			row += str(i) + rok + ' '
			i+=1
		print(row)
	print(slov)
	print(simv)
		#if r in row:
		#if row.find(r) != -1:
			#row = row.replace(r, t)
			#print(row)