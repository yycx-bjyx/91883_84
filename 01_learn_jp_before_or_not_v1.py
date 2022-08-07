# Ask the user if they have played before

# If they say yes, output 'program continues'

# If they say no, output 'display instructions'

# commit code == drag file to github.com
x = "yes"
y = "no"

x = str(x)
y = str(y)
instructions = y

while instructions.lower() != x:

    while True:
        try:
            instructions = str(input("Have you played this game before"))
            break
        except ValueError:
            print("not a valid answer")

    if instructions.lower() == y:
        print("display instructions")
        break
    elif instructions.lower() == x:
        print("program continue")
    else:
        print("Please enter either 'Yes' or 'No'")
