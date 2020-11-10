import json

q1 = { 
  "category": 
    "Actors & Actresses", 
  "questions": 
    [
      {
        "answer": "Chuck Norris", 
        "question": "Which actor traveled with the circus at the age of 15 and was a tamer?"
      }
    ]
}
  
q2 = { 
  "category":
    "Art / Culture",
  "questions":
    [
      {
        "answer": "Verona", 
        "question": "In which city did Romeo and Julia live?"
      }
    ]
}

q3 = { 
  "category":
    "Australia",
  "questions":
    [
      {
        "answer": "Opera", 
        "question": "What is the most famous building in Sydney?"
      }
    ]
}

q4 = { 
  "category":
    "Biology",
  "questions":
    [
      {
        "answer": "Yes, a snail has 135 rows of teeth", 
        "question": "Do snails have teeth?"
      }
    ]
}

q5 = { 
  "category":
    "Dinosaurs",
  "questions":
    [
      {
        "answer": "Torosaurus", 
        "question": "To which dinosaur does the largest skull belong?"
      }
    ]
}

q6 = { 
  "category":
    "Economy",
  "questions":
    [
      {
        "answer": "Drachme", 
        "question": "What was the currency of Greece before the introduction of the EURO?"
      }
    ]
}

q7 = { 
  "category":
    "Film / TV",
  "questions":
    [
      {
        "answer": "Antonio Banderas", 
        "question": "Who played Che Guevara in the movie \"Evita\"?"
      }
    ]
}

q8 = { 
  "category":
    "Food and drink",
  "questions":
    [
      {
        "answer": "Vitamin C", 
        "question": "Which vitamin is the only one that you will not find in an egg?"
      }
    ]
}

q9 = { 
  "category":
    "Fruits & Vegetables",
  "questions":
    [
      {
        "answer": "52 meters", 
        "question": "How long was the longest apple peel, recorded in the Guinness Book of Records?"
      }
    ]
}

q10 = { 
  "category":
    "General",
  "questions":
    [
      {
        "answer": "Dardanelles", 
        "question": "For which narrow sea strait is Hellespont the ancient name?"
      }
    ]
}

q11 = { 
  "category":
    "Geography",
  "questions":
    [
      {
        "answer": "The Mediterranean Sea and the Red Seas", 
        "question": "Which two seas are joined by the Suez Canal?"
      }
    ]
}

q12 = { 
  "category":
    "History",
  "questions":
    [
      {
        "answer": "Russia", 
        "question": "Which country sent its navy around the world to fight the Japanese in 1904?"
      }
    ]
}

q13 = { 
  "category":
    "Informatics",
  "questions":
    [
      {
        "answer": "File Transfer Protocol", 
        "question": "What does \"FTP\" stand for in the computer and internet world?"
      }
    ]
}

q14 = { 
  "category":
    "Language",
  "questions":
    [
      {
        "answer": "Montreal (Canada)", 
        "question": "Which is the world s second largest French-speaking city?"
      }
    ]
}

q15 = { 
  "category":
    "Literature",
  "questions":
    [
      {
        "answer": "Rudyard Kipling", 
        "question": "Who wrote Jungle Book?"
      }
    ]
}

q16 = { 
  "category":
    "Music",
  "questions":
    [
      {
        "answer": "Megan Thee Stallion", 
        "question": "Who is Tina Snow?"
      }
    ]
}

q17 = { 
  "category":
    "Nature",
  "questions":
    [
      {
        "answer": "Elephant", 
        "question": "Which mammal cannot jump?"
      }
    ]
}

q18 = { 
  "category":
    "Politics",
  "questions":
    [
      {
        "answer": "The White House", 
        "question": "In which house does the American president live?"
      }
    ]
}

q19 = { 
  "category":
    "Science",
  "questions":
    [
      {
        "answer": "Blue or purple", 
        "question": "What is the color of giraffe tongue?"
      }
    ]
}

q20 = { 
  "category":
    "Sports",
  "questions":
    [
      {
        "answer": "Seven times", 
        "question": "How many times has Michael Schumacher been a Formula 1 champion?"
      }
    ]
}

all_questions = [q1, q2, q3, q4, q5, q6, q7, q8, q9, q10, q11, q12, q13, q14, q15, q16, q17, q18, q19, q20]

with open("quest.json", "w") as l:
  questions = json.dump(all_questions, l)

#with open("quest.json", "r") as k:
  #json_data = json.load(k)

#for item in json_data:
  #print("Category: " + str(item["category"]))
