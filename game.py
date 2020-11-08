# download module randint from library random
from random import randint as r

# select number between 1 and 100
number = r(1, 101)

while True:
    # try to execute the code below
    try:
        # display the message: "Guess the number: ", download number from user as string and convert it to int
        selected_number = int(input("Guess the number: "))

        # check if the given number by the user is smaller than selected number by computer
        # if it's true, display the message "To small!"
        if selected_number < number:
            print("To small!")
        # check if the given number by the user is bigger than selected number by computer
        # if it's true, display the message "To big!"
        elif selected_number > number:
            print("To big!")
        # display a message about your win and finish the game
        else:
            print("You win!")
            break
    # if the program encounters error, display the message "It's not a number!"
    except (ValueError, TypeError):
        print("It's not a number!")
