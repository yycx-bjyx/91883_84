import random

how_much= 10
one_ques = 1

questions = ["ら", "は", "さ", "ち", "ほ", "め", "ん", "ま", "む", "ぬ", "あ", "わ", "た", "こ", "つ"]

ran_question = random.sample(questions, how_much)
print(ran_question)
