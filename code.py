import random

def choose_word():
    word = random.choice(["python", "hangman", "developer", "programming", "challenge", "computer", "science"])
    print(f"Chosen word (for testing): {word}")  # Debugging print
    return word

def display_word(word, guessed_letters):
    displayed = " ".join(letter if letter in guessed_letters else "_" for letter in word)
    print(f"Displayed word: {displayed}")  # Debugging print
    return displayed
