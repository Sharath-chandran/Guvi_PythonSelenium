import random

# Set a range for the random number
lower_bound = 1
upper_bound = 100

# Generate a random number
secret_number = random.randint(lower_bound, upper_bound)

print("Welcome to 'Guess the Number'!")
print(f"I'm thinking of a number between {lower_bound} and {upper_bound}.")

# Initialize guess variable
guess = None
attempts = 0

# Loop until the player guesses correctly
while guess != secret_number:
    # Take user input and convert to integer
    guess_input = input("Enter your guess: ")

    # String manipulation: remove whitespace
    guess_input = guess_input.strip()

    # Check if input is a valid number
    if not guess_input.isdigit():
        print("Please enter a valid number.")
        continue

    # Convert to integer
    guess = int(guess_input)
    attempts += 1

    # Use conditions to give feedback
    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts.")

