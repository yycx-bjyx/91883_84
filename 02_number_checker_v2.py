# Functions
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
                return response
            # output an error if the number is not appropriate.
            else:
                print(error)

        except ValueError:
            print(error_msg)
        # if the amount is appropriate

# main routine


how_much = num_check("How much would you like to test yourself with? ", 0, 10)
