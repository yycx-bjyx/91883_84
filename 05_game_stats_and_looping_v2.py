import random

# set the value as 10, as the variable how_much can be found in the question the program has asked
questions = ["ら", "は", "さ", "ち", "ほ", "め", "ん", "ま", "む", "ぬ", "あ", "わ", "た", "こ", "つ"]
answers = ["ra", "ha", "sa", "chi", "ho", "me", "n", "ma", "mu", "nu", "a", "wa", "ta", "ko", "tsu"]
REPEAT = 15
Total_score = REPEAT*10
count = 0
score = 0
user = ""
exit_way = "xxx"
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

    elif user == exit_way:
            count = REPEAT
            Total_score = count * 10
            print("Your score is: {}".format(score))

    else:
        print("Sorry, You Got This Wrong...\n")
        # try again
        try_again = input("Answer the question: {} ".format(random_question))
        if try_again == answers[rand]:
            print("You got it right this time. You gain 5 points for this!!\n")
            score += 5
            # if the user has got it right on hte second time,
            # they will have 5 points gained towards their total score.
        else:
            print("This is the correct answer: {} \n".format(answers[rand]))
        questions.pop(rand)
        answers.pop(rand)

score_percentage = score/Total_score * 100
print("You got {}% right in the quiz.".format(score_percentage))
if score_percentage > 50:
    print("CONGRATULATIONS!! YOU'VE COMPLETED THE QUIZ FANTASTICALLY!!")

else:
    print("Please work hard for a better score next time!! ")


