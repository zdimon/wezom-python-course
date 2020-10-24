import json
quiz = open('quiz.json', 'r')
json.load(quiz)
score = 0
for num in quiz:
