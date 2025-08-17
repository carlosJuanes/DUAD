#12. Create an algorithm that has a secret number from 1 to 10 and asks the user to guess that number.
#The algorithm should not terminate until the user guesses the number.

secret_number=7

guessed_number= int(input("please enter a number from 1 - 10 = "))
while guessed_number!=secret_number:
    print("INCORRECT!!! please try again")
    guessed_number= int(input("please enter a number from 1 - 10 = "))
print(f"CONGRATULATION!!! the secret number was  {secret_number}")