# Random is variable generator used for selecting random words
# To generate a random number for the game.
import random

# Selecting the range between 1 to 100
Start_range = 1
End_range = 100

# Generates a secret random number between Start and End range
Number_Guess = random.randint(Start_range, End_range)

print(f"Select any number between {Start_range} and {End_range}.")

# Initialize guess variable
guess = None
attempts = 0

# While loop keeps running until the player guess the number
while guess != Number_Guess:
    # Player input
    guess_input = input("Enter the number that you are guessing: ")

# Ensures the player enters a digits
# Checking the input whether it is a valid number
    if not guess_input.isdigit():
        print("Please enter a valid number: ")
        continue
# Converts the valid string input to an integer
    guess = int(guess_input)
    attempts += 1

# Compares the player's guess to make sure low or high or correct
    if guess < Number_Guess:
        print("Too low! Try again.")
    elif guess > Number_Guess:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You guessed the number {Number_Guess} in {attempts} attempts.")

