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
