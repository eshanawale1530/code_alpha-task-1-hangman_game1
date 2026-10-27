
import random

# List of 5 predefined words
words = ["python", "apple", "tiger", "robot", "house"]

# Select a random word
word = random.choice(words)

# Game variables
guessed_letters = []
incorrect_guesses = 0
max_attempts = 6

print("===== WELCOME TO HANGMAN =====")
print("Guess the word one letter at a time!")
print("You have 6 incorrect guesses allowed.")

# Main game loop
while incorrect_guesses < max_attempts:

    # Display the current word progress
    display_word = ""

    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)
    print("Incorrect guesses left:", max_attempts - incorrect_guesses)
    print("Guessed letters:", guessed_letters)

    # Check if the player has won
    if all(letter in guessed_letters for letter in word):
        print("\nCongratulations! You guessed the word:", word)
        break

    # Get user input
    guess = input("Enter a letter: ").lower().strip()

    # Validate input
    if len(guess) != 1 or not guess.isalpha():
        print("Please enter a single letter.")
        continue

    # Check repeated guesses
    if guess in guessed_letters:
        print("You already guessed that letter!")
        continue

    guessed_letters.append(guess)

    # Check the guess
    if guess in word:
        print("Correct guess!")
    else:
        incorrect_guesses += 1
        print("Wrong guess!")

# Check if the player lost
if incorrect_guesses == max_attempts:
    print("\nGame over! The word was:", word)

print("===== THANK YOU FOR PLAYING =====")
