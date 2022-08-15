import random

how_much= 10
# set the value as 10, as the variable how_much can be found in the question the program has asked
questions = ["ら", "は", "さ", "ち", "ほ", "め", "ん", "ま", "む", "ぬ", "あ", "わ", "た", "こ", "つ"]
for item in range (0, how_much):
    #random
    rand = random.randrange(len(questions))
    random_question = questions[rand]
    print("Answer this question: ", random_question)
    questions.pop(rand)


