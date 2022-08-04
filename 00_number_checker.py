# Functions
def num_check(question, low, high):
    error = "please enter an integer between 1 and 10\n"
    error_msg = "this is not an integer!!"
    # \n give line break
    valid = False
    while not valid:
        # ask the question
        try:
            response = int(input(question))
            if low < response <= high:
                return response
            # output an error if the number is not appropriate.
            else:
                print(error)

        except ValueError:
            print(error_msg)
        # if the amount is appropriate


# main routine
how_much = num_check("how much would you like to test yourself with? ", 0, 10)
