# Random is variable generator used for selecting random words
import random

# Create a List of words for the program
words = ['python', 'javascript', 'java', 'automation', 'pytest', 'guvi', 'selenium']

# Selecting the random word from the list and storing in the original_word
original_word = random.choice(words)

# Randomly chosen word is stored by using list - For splitting the word into letters
# Scramble the word using string manipulation
scrambled = list(original_word)

# shuffle the letters in the list
random.shuffle(scrambled)

# Shuffled letters are joined back to single string using 'join'
scrambled_word = ''.join(scrambled)

# Guess the word from Scrambled letters
print(f"Guess the word from Scrambled letters: {scrambled_word}")

# Initialize variables
# attempts is to track the guesses made by player
attempts = 0
guess = ''

# While loop keeps running until the player find the original word
# .lower() - Ensures the input is case-insensitive
while guess != original_word:
    guess = input("Your guess: ").strip().lower()
    attempts += 1

    if guess == original_word:
        print(f"Correct! You guessed it in {attempts} attempts.")
    else:
        print("Incorrect. Try again!")
