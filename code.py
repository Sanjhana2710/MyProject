import random

def choose_word():
    word = random.choice(["python", "hangman", "developer", "programming", "challenge", "computer", "science"])
    print(f"Chosen word (for testing): {word}")  # Debugging print
    return word
