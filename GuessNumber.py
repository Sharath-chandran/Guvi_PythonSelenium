import random

# Selecting the range between 1 to 100
Lower_Value = 1
Upper_Value = 100

# Generating a random number
Secret_Number = random.randint(Lower_Value, Upper_Value)

print(f"Choose a number between {Lower_Value} and {Upper_Value}.")

# Initialize guess variable
guess = None
attempts = 0

# Loop executes until we guess the number correctly
while guess != Secret_Number:
    # User input
    guess_input = input("Enter the number that you are guessing: ")

    # String manipulation: remove whitespace
    # guess_input = guess_input.strip()

    # Checking the input whether it is a valid number
    if not guess_input.isdigit():
        print("Please enter a valid number.")
        continue

    # Convert to integer
    guess = int(guess_input)
    attempts += 1

    # Use conditions to give feedback
    if guess < Secret_Number:
        print("Too low! Try again.")
    elif guess > Secret_Number:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You guessed the number {Secret_Number} in {attempts} attempts.")

