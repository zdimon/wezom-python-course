import sys
#import os
#sys.argv


#for i in sys.argv:
	#k = i[0:]
	#print(k)



#with open("this", "w") as o:
#	o.write("floar")

#try:
#	os.remove(sys.argv[1])
#except:
#	print("Error")
#print("All good")



a = open("test.txt", "r")
for line in a.readlines():
	#b = line.find(sys.argv[1])
	
	#if b > -1:
		#print(line)
		#p = line.replace("can", "cant")
		#print(p)

	v = line.find(sys.argv[1])
	if v > -1:
		l = line.replace(sys.argv[1], sys.argv[2])
		print(l)

#txt = a.read()
#print(txt)
