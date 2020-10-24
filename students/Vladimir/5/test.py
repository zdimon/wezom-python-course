'''
def file_search():
    from os import listdir
    from os.path import isfile, join
    onlyfiles = [f for f in listdir('C:/Users/Владелец/wezom-python-course/teacher/5/data') if isfile(join('C:/Users/Владелец/wezom-python-course/teacher/5/data', f))]
    print(onlyfiles)
'''

import requests
from bs4 import BeautifulSoup

txt = requests.get('https://pythonist.ru/')
soup = BeautifulSoup(txt.text, 'html.parser')
links = soup.find_all('div', {'class': 'site-content'})
for link in links:
    print(link.text)
print(txt.url)