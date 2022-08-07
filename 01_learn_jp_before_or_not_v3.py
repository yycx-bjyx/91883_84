# Functions
def yes_no(question, learn_it_before):
    valid = False
    while not valid:
        # by making a variable for the t / f statement, it is not a lazy coding...
        response = input(question).lower()
        # .lower() at the end of statement input indicates that the variable is being put as a lower case, and is not case-sensitive
        if response == "yes" or response == "y":
            response = "yes"
        elif response == "no" or response == "n":
            response = "no"
        else:
            print("please answer yes / no")
# Main Routine...


instructions = yes_no("Have you learnt Japanese before? ", 
                      "Please learn Japanese before testing yourself.\n")

