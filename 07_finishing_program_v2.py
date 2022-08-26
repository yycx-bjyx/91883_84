# Functions
import random


def yes_no(question, learn_jp_before):
    valid = False
    # avoiding lazy coding by setting boolean as a variable
    # and put in while statement.
    while not valid:
        response = input(question).lower()
        # .lower() at the end of statement input indicates
        # that the variable is being put as a lower case,
        # and is not case-sensitive
        # so if the user inputs a mixed case answer,
        # but it is correct, it will still be correct
        if response == "yes" or response == "y":
            response = "yes"
            return response
        elif response == "no" or response == "n":
            print(learn_jp_before)
        else:
            print("please answer yes / no")


def instruction(instructions):
    print(instructions)
    print()
    print("The rules of the game go here:")
    print()
    print("In this quiz, you will be asked how much rounds you would like to play, "
          "then you will be tested on your Hiragana knowledge. ")
    print()
    print("You are able to exit if you want to during the quiz, by entering 'xxx' to the input spaces. ")
    print()
    print("For the scoring part, you will get 10 marks when you got the question right at the first time, "
          "and you will get 5 marks when you got the question right at the second time. "
          "But if you cannot get the question right on the second, you will not be able to answer it again "
          "and get score from it. ")
    print()
    print("At the end of the quiz, your marks will be shown with the percentage of "
          "your accuracy in answering the questions.")
    print()
    print("Lastly, Good Luck on your quiz!!")
    return""
    # print instruction for the user that has not played
    # this quiz or used this to test themselves before


def num_check(question, low, high):
    error = "Please enter an integer between 1 and 10\n"
    error_msg = "This is not an integer!!\n"
    valid = False
    while not valid:
        # ask the question
        try:
            response = int(input(question))
            if low < response <= high:
                return response
                # if the amount is appropriate
            else:
                print(error)
        except ValueError:
            print(error_msg)
            # output an error if the number is not appropriate.


def statement_generator(statement, decoration):

    sides = decoration * 3

    statement = "{} {} {}".format(sides, statement, sides)
    top_bottom = decoration * len(statement)

    print(top_bottom)
    print(statement)
    print(top_bottom)

    return ""



# Main Routine...

welcome = statement_generator("Welcome to the Japanese Quiz", "*")
print(welcome)
print()


learn_jp_before_ques = yes_no("Have you learnt Japanese before? ",
                              "Please learn Japanese before testing yourself. \n")

show_instruction = input("\nHave you played with this quiz before? ")

if show_instruction == "yes" or show_instruction == "y":
    show_instruction = "yes"

elif show_instruction == "no" or show_instruction == "n":
    show_instruction = "no"
    instructions = statement_generator("How to Play", "*")
    print(instruction(instructions))
    
else:
    print("Please enter either 'yes' or 'no'. ")

how_much = num_check("\nHow much would you like to test yourself with? ", 0, 10)

questions = ["ら", "は", "さ", "ち", "ほ", "め", "ん", "ま", "む",
             "ぬ", "あ", "わ", "た", "こ", "つ"]
answers = ["ra", "ha", "sa", "chi", "ho", "me", "n", "ma", "mu",
           "nu", "a", "wa", "ta", "ko", "tsu"]

count = 0
score = 0
Total_score = how_much*10
correct_question = 0
user = ""
exit_way = "xxx"

while count < how_much:
        # print current round num
        round_num = count + 1
        round_num_decoration = statement_generator("Round {}".format(round_num), "^")
        # add a new variable for printing the statement with the decoration
        print()

        # generate random number for the index number of the list.
        rand = random.randrange(len(questions))
        random_question = questions[rand]

        # record the input from the user
        user = input("Answer the question: {} ".format(random_question)).lower()
        print()
        count += 1
        # keep track of num of questions


        if user == answers[rand]:
            congratulating_msg = statement_generator("CONGRATS!!! TEN POINT ADDED!!", "!")
            print()
            score += 10
            correct_question += 1
            questions.pop(rand)
            answers.pop(rand)

        elif user == exit_way:
            count = how_much
            Total_score = count * 10
            print("Your score is: {}".format(score))

        else:
            wrong_answer = statement_generator("Sorry, You Got This Wrong", ".")
            print()
            # give a chance for the user to try answering the question again
            try_again = input("Answer the question: {} ".format(random_question))
            if try_again == answers[rand]:
                right_answer_sec_time = statement_generator("You got it right this time.", "+")
                print()
                score += 5
                correct_question += 1
            else:
                print("This is the correct answer: {} \n".format(answers[rand]))
            questions.pop(rand)
            answers.pop(rand)


score_percentage = correct_question/how_much * 100
if score_percentage > 50:
    congrat_msg = statement_generator("CONGRATULATIONS!! YOU'VE COMPLETED THE QUIZ FANTASTICALLY!!", "~")
    print()

else:
    low_percentage = statement_generator("Please work hard for a better score next time", "-")

print("You have got {} out of {}, and is {:.1f}% right among all questions!".format(score, Total_score, score_percentage))
