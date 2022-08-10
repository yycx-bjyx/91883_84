# Functions
def error_msg():
    print("this is not an integer!!")
    return ""

# Main routine


error = "please enter an integer between 1 and 10\n"
# \n give line break
response = 0

valid = False
while not valid:
    # ask the question
    try:
        response = int(input("How much would like to play with? "))
        response = int(response)
        if 0 < response <= 10:
            print("You have asked to play with ${}".format(response))
        # output an error if the number is not appropriate.
        else:
            print(error)

    except ValueError:
        print(error_msg())
    # if the amount is appropriate
