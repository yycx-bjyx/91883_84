import random

how_much= 10

questions = ["ら", "は", "さ", "ち", "ほ", "め", "ん", "ま", "む","ぬ"]

for item in range(0, how_much):
    ran_questions = random.sample(questions)
    print(ran_questions)
