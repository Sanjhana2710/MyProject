import random

def choose_word():
    word = random.choice(["python", "hangman", "developer", "programming", "challenge", "computer", "science"])
    print(f"Chosen word (for testing): {word}")  # Debugging print
    return word

def display_word(word, guessed_letters):
    displayed = " ".join(letter if letter in guessed_letters else "_" for letter in word)
    print(f"Displayed word: {displayed}")  # Debugging print
    return displayed

def hangman():
    word = choose_word()
    guessed_letters = set()
    attempts = 6
    
    print("Welcome to Hangman!")
    
    while attempts > 0:
        print(f"\nWord: {display_word(word, guessed_letters)}")
        print(f"Attempts left: {attempts}")
        guess = input("Guess a letter: ").lower()
        
        if guess in guessed_letters or len(guess) != 1 or not guess.isalpha():
            print("Invalid input or already guessed.")
            continue
        
        guessed_letters.add(guess)
        print(f"Guessed letters so far: {guessed_letters}")  # Debugging print
        
        if guess in word:
            print("Good job! That letter is in the word.")
            if set(word).issubset(guessed_letters):
                print(f"\nCongratulations! You guessed the word: {word}")
                return
        else:
            attempts -= 1
            print("Incorrect guess.")
            
    print(f"\nGame Over! The word was: {word}")
