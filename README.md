# hangman_game1
A simple Python-based Hangman game where players guess a randomly selected word from a predefined list, with a maximum of 6 incorrect guesses. Built using loops, conditionals, lists, strings, and the random module.
# Python Hangman Game 🎮

## Description
A simple text-based Hangman game developed using Python. The player guesses a randomly selected word from a predefined list of five words, one letter at a time. The player is allowed a maximum of six incorrect guesses to identify the hidden word.

## Features
- Random word selection from a list of five words.
- Letter-by-letter guessing.
- Tracks guessed letters and incorrect attempts.
- Validates user input and prevents repeated guesses.
- Displays win or game-over messages.

## Technologies Used
- Python
- Random module
- Loops and conditional statements
- Strings and lists
- User input/output

## Code Explanation
- `random.choice()` selects a random word from the predefined list.
- `while` loop continues the game until the player wins or reaches six incorrect guesses.
- `for` loop displays guessed letters and underscores for hidden letters.
- `if-else` statements check whether the guessed letter is correct.
- `guessed_letters` stores previously guessed letters.
- `input()` accepts the player's guess, while `print()` displays the game status.
- `all()` checks whether every letter in the word has been guessed.

## How to Run
1. Install Python on your computer.
2. Clone or download this repository.
3. Open the project folder in VS Code or a terminal.
4. Run the following command:

```bash
python hangman.py
```

## Learning Outcome

code : 


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

This project demonstrates the fundamentals of Python programming, including random selection, loops, conditional logic, lists, strings, and input validation.
