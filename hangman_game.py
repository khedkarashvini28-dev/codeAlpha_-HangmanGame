# ==========================================
# CodeAlpha Internship Project
# Project Name: Hangman Game
# Developed by: Ashvini Khedkar
# ==========================================

import random

# List of words
words = ["python", "computer", "laptop", "apple", "keyboard"]

# Randomly choose one word
word = random.choice(words)

# Store guessed letters
guessed_letters = []

# Number of incorrect guesses allowed
attempts = 6

print("=" * 50)
print("         WELCOME TO HANGMAN GAME")
print("=" * 50)

while attempts > 0:

    display_word = ""

    # Display guessed letters
    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "

    print("\nWord:", display_word)

    # Check if word is completed
    if "_" not in display_word:
        print("\n🎉 Congratulations! You guessed the word correctly.")
        break

    guess = input("Guess a letter: ").lower()

    # Check if already guessed
    if guess in guessed_letters:
        print("You already guessed that letter.")
        continue

    guessed_letters.append(guess)

    # Check correct or incorrect
    if guess in word:
        print("✅ Correct Guess!")
    else:
        attempts -= 1
        print("❌ Wrong Guess!")
        print("Remaining Attempts:", attempts)

# If player loses
if attempts == 0:
    print("\nGame Over!")
    print("The correct word was:", word)