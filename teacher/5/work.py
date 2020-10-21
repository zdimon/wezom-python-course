# from bs4 import BeautifulSoup

# import requests

# txt = requests.get('https://pythondigest.ru/')

# soup = BeautifulSoup(txt.text, 'html.parser')

# links = soup.find_all('a', {"class": "issue-item-title"})

# for link in links:
#     print(link.text)

# l = [1,2,3,4]
#md = { 'books': [1,2,3], 'users': [{ 'name': 'Dima' }] }

# e = {"key": [1,2,3,4]}
# e['key'][1]

import json

f = open('quiz.json', 'r')
mystr = f.read()
data = json.loads(mystr)
for item in data:
    print(item['question'])




