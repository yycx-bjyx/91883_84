instructions = ""
# Ask the user if they have played before
while instructions.lower() != "xxx":
    instructions = input("Have you played this game before").lower()
    # .lower() at the end of statement input indicates that the variable is being put as a lower case, and is not case-sensitive
    # If they say yes, output 'program continues'
    if instructions == "yes" or instructions  == "y":
        print("program continues")
    # If they say no, output 'display instructions'
    elif instructions == "no" or instructions == "n":
        print("display instruction")
    # commit code == drag file to github.com
    else:
        print("Please answer Yes / No")
