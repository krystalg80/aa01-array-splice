# import the json module from python3

import json

# open the file and parse the JSON

with open('me-capitals.json', 'r') as f:
    data = json.load(f)

# add total as the length of the cards
total = len(data["cards"])
# initilaize starting score as 0
score = 0

for i in data["cards"]:
    guess = input(i["q"] + " > ")

    if guess == i["a"] :

        score += 1

        print(f"Correct! Current score: {score}/{total}")
    else:
        print("Incorrect! The correct answer was", i["a"])
        print(f"Current score: {score}/{total}")




    