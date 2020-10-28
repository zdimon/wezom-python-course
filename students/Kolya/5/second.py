from os import listdir
from os.path import isfile, join
def kol():
	onlyfiles = [f for f in listdir('C:/Users/kolya/wezom-python-course/students/Kolya/5/data') if isfile(join('C:/Users/kolya/wezom-python-course/students/Kolya/5/data', f))]
	return onlyfiles