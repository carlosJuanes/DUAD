
#3. Create a program with a secret number from 1 to 10. The program should not close until the user guesses the number.
#You must research how to generate a different random number each time it runs.

#In this exercise, I had to use AI to find a possible solution, not a direct answer.
#  I requested help to understand step-by-step what the exercise asks for.

#(Research how to generate a different random number each time it runs.)
#  My understanding was that I needed to find a way to generate a random number after the secret number had been guessed

import random

play_again = "yes"
while play_again.lower() == "yes":
    secret_number = random.randint(1, 10)
    guessed_number = int(input(f"Enter a number from 1-10: "))
    while guessed_number != secret_number:
        print("Please try again.")
        guessed_number = int(input(f"Enter a number from 1-10: "))
    print(f"Congratulations! The secret number was {secret_number}.")
    play_again = input(f"Do you want to play again? Type 'yes' to continue: ")
print(f"Game over.")

