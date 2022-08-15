import random

# set the value as 10, as the variable how_much can be found in the question the program has asked
questions = ["ら", "は", "さ", "ち", "ほ", "め", "ん", "ま", "む", "ぬ", "あ", "わ", "た", "こ", "つ"]
answers = ["ra", "ha", "sa", "chi", "ho", "me", "n", "ma", "mu", "nu", "a", "wa", "ta", "ko", "tsu"]
REPEAT = 5
count = 0
score = 0
user = ""
while count < REPEAT:
    # random
    rand = random.randrange(len(questions))
    random_question = questions[rand]

    # input
    user = input("Answer the question: {} ".format(random_question)).lower()
    count += 1
    # keep track of num of questions


    if user == answers[rand]:
        print("CONGRATS!!! TEN POINT ADDED!!\n")
        score += 10
        questions.pop(rand)
        answers.pop(rand)

    else:
        print("Sorry, You Got This Wrong...\n")
        # try again
        try_again = input("Answer the question: {} ".format(random_question))
        if try_again == answers[rand]:
            print("You got it right this time. You gain 5 points for this!!\n")
            score += 5
        else:
            print("This is the correct answer: {} \n".format(answers[rand]))
        questions.pop(rand)
        answers.pop(rand)

print("CONGRATS!! YOUR SCORE IS {} out of {}!!!!".format(score, REPEAT*10))

