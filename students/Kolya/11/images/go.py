import os
a = os.listdir(path=".")
for row in a:
	print("{url: 'images/%s'}," % row)