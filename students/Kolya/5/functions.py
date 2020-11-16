'''
import requests
from bs4 import BeautifulSoup
txt = requests.get('https://pythonist.ru/')
soup = BeautifulSoup(txt.text, 'html.parser')
a = soup.find_all('h2', {'class':'entry-title'})
for link in a:
	print(link.text)
'''
import json
json.loads()
#json.dumps(obj)
for row in e:
	for row in 
	print(row)