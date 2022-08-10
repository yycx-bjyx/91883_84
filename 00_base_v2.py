# Functions
def yes_no(question, learn_jp_before):
    valid = False
    while not valid:
        # by making a variable for the t / f statement,
        # it is not a lazy coding...
        response = input(question).lower()
        # .lower() at the end of statement input indicates
        # that the variable is being put as a lower case,
        # and is not case-sensitive
        if response == "yes" or response == "y":
            response = "yes"
            return response
        elif response == "no" or response == "n":
            response = "no"
            print(learn_jp_before)
        else:
            print("please answer yes / no")


def instruction():
    print("*** How to Play ***")
    print()
    print("The rules of the game go here")
    print()
    return""


def num_check(question, low, high):
    error = "Please enter an integer between 1 and 10\n"
    error_msg = "This is not an integer!!\n"
    # \n give line break
    valid = False
    while not valid:
        # ask the question
        try:
            response = int(input(question))
            if low < response <= high:
                print("You would like to test yourself with {} rounds.\n".format(response))
                return response
            # output an error if the number is not appropriate.
            else:
                print(error)

        except ValueError:
            print(error_msg)
        # if the amount is appropriate

# Main Routine...


learn_jp_before_ques = yes_no("Have you learnt Japanese before? ",
                              "Please learn Japanese before testing yourself. \n")

show_instruction = input("\nHave you played with this quiz before?")

if show_instruction == "yes" or show_instruction == "y":
    show_instruction = "yes"
    print("program continue")
elif show_instruction == "no" or show_instruction == "n":
    show_instruction = "no"
    print(instruction())
else:
    print("Please enter either 'yes' or 'no'. ")

how_much = num_check("How much would you like to test yourself with? ", 0, 10)
