import random

def choose_word():
    word = random.choice(["python", "hangman", "developer", "programming", "challenge", "computer", "science"])
    print(f"Chosen word (for testing): {word}")  
    return word

def display_word(word, guessed_letters):
    displayed = " ".join(letter if letter in guessed_letters else "_" for letter in word)
    print(f"Displayed word: {displayed}")  
    return displayed

def provide_hint(word, guessed_letters):
    hint_letter = next((letter for letter in word if letter not in guessed_letters), None)
    if hint_letter:
        print(f"Hint: The word contains the letter '{hint_letter}'.")

def offer_extra_attempts(attempts):
    choice = input("Would you like 2 extra attempts? (yes/no): ").strip().lower()
    if choice == "yes":
        return attempts + 2
    return attempts

def hangman():
    word = choose_word()
    guessed_letters = set()
    attempts = 6
    
    print("Welcome to Hangman!")
    attempts = offer_extra_attempts(attempts)
    
    while attempts > 0:
        print(f"\nWord: {display_word(word, guessed_letters)}")
        print(f"Attempts left: {attempts}")
        if attempts == 3:
            provide_hint(word, guessed_letters)
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

if _name_ == "_main_":
    hangman()
