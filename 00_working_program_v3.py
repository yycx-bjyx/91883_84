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


def instruction():
    print("*** How to Play ***")
    print()
    print("The rules of the game go here")
    print()
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
                print("You would like to test yourself with {} rounds.\n"
                      .format(response))
                return response
                # if the amount is appropriate
            else:
                print(error)
        except ValueError:
            print(error_msg)
            # output an error if the number is not appropriate.


# Main Routine...


learn_jp_before_ques = yes_no("Have you learnt Japanese before? ",
                              "Please learn Japanese before testing yourself. \n")

show_instruction = input("\nHave you played with this quiz before?")

if show_instruction == "yes" or show_instruction == "y":
    show_instruction = "yes"
elif show_instruction == "no" or show_instruction == "n":
    show_instruction = "no"
    print(instruction())
else:
    print("Please enter either 'yes' or 'no'. ")

how_much = num_check("How much would you like to test yourself with? ", 0, 10)

questions = ["ら", "は", "さ", "ち", "ほ", "め", "ん", "ま", "む",
             "ぬ", "あ", "わ", "た", "こ", "つ"]
answers = ["ra", "ha", "sa", "chi", "ho", "me", "n", "ma", "mu",
           "nu", "a", "wa", "ta", "ko", "tsu"]
count = 0
score = 0
user = ""
while count < how_much:
    # generate random number for the index number of the list.
    rand = random.randrange(len(questions))
    random_question = questions[rand]

    # record the input from the user
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
        # give a chance for the user to try answering the question again
        try_again = input("Answer the question: {} ".format(random_question))
        if try_again == answers[rand]:
            print("You got it right this time.\n")
        else:
            print("This is the correct answer: {} ".format(answers[rand]))
        questions.pop(rand)
        answers.pop(rand)

