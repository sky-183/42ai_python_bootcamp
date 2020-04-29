# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    guess.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: vflander <marvin@42.fr>                    +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2020/04/29 18:13:47 by vflander          #+#    #+#              #
#    Updated: 2020/04/29 18:13:47 by vflander         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from random import randrange


def guesser():
    """interactive guessing game. It will ask the user to guess a number
    between 1 and 99. The program will tell the user if their input is
    too high or too low. The game ends when the user finds out the
    secret number or types exit.
    """
    intro = (
        "This is an interactive guessing game!\n"
        "You have to enter a number between 1 and 99 to "
        "find out the secret number.\n"
        "Type 'exit' to end the game.\n"
        "Good luck!"
    )
    guess = "What's your guess between 1 and 99?\n"
    dadams_ref = (
        "The answer to the ultimate question of life, "
        "the universe and everything is 42.\n"
    )
    first_try = "Congratulations! You got it on your first try!\n"
    secret_number = randrange(1, 100)
    num_guesses = 0
    print(intro)
    # main loop
    while True:
        user_input = input(guess)
        if user_input.lower() == "exit":
            print("Goodbye!")
            break
        # ignoring floats and negative ints here
        if not user_input.isdigit():
            print("That's not a number.")
            continue
        user_guess = int(user_input)
        if 0 > user_guess < 100:
            print("That's not a valid number.")
            continue
        # got the good input here
        num_guesses += 1
        if user_guess == secret_number:
            if num_guesses == 1:
                print(first_try)
            if secret_number == 42:
                print(dadams_ref)
            print("Congratulations, you ve'got it!")
            if num_guesses != 1:
                print(f"You won in {num_guesses} attempts!")
            break
        elif user_guess > secret_number:
            print("Too high!")
        elif user_guess < secret_number:
            print("Too low!")
        else:
            # for debug
            print("You should not be here, traveller!")


if __name__ == "__main__":
    guesser()
