import random
def get_letter(gussed_letter):
    while True:
        guess=input("Guess a letter: ").lower().strip()
        if len(guess) !=1:
            print("Enter only one letter at a time")
        elif guess in gussed_letter:
            print(f"You already guessed the letter{guess}.please enter a different letter")
        elif not guess.isalpha():
            print("Please enter a letter(a-z)")
        else:
            return guess
def display_gamestatus(display_word,guessed_letter,wrong_gusses,gusses_left,stages):
    print("__"*50)
    print(stages[len(wrong_gusses)])
    print("Word",{" ".join(display_word)})
    print("Gusses letters",{",".join(guessed_letter)if guessed_letter else None})
    print(f"Wrong letter guessed",{",".join(wrong_gusses)if wrong_gusses else None})
    print("Incorrect gusses left",gusses_left)
    print("__"*50)
def play_hangman():
    stages = [
    """
  +---+
  |   |
      |
      |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
      |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
  |   |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========""",
    """
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
========="""
]

    words =["PYTHON","HANGMAN","COMPUTER","JAVACRIPT","PROGRAMER"]
    gussed_letter=set()
    wrong_gusses=[]
    max_try=6
    min_try=0
#print(gussed_letter)
    hidden_word=random.choice(words).lower()
    display_word=["_"]*len(hidden_word)
    print("🎮 Welcome to Hangman!")
    print(f"The word has {len(hidden_word)} letters.")
    while min_try<max_try and "_" in display_word:
        display_gamestatus(display_word,gussed_letter,wrong_gusses,max_try-min_try,stages)
        guess=get_letter(gussed_letter)
        gussed_letter.add(guess)
        if guess in hidden_word:
            print(f"✓ Good guess! '{guess}' is in the word.\U0001F604")
            for i , letter in enumerate(hidden_word):
                if letter==guess:
                    display_word[i]=guess
        else:
             min_try+=1
             print(f"✗ Sorry, '{guess}' is not in the word.\U0001F641")
             wrong_gusses.append(guess)
    if "_" not in display_word:
        print(f"🎉 Congratulations! You guessed the word: {hidden_word}")
        print(f"You had {max_try - min_try} incorrect guesses left.")
    else:
        print(f"💀 Game Over! You've run out of guesses.\U0001F494")
        print(f"The word was: {hidden_word}")
    print("__" * 40)
    
    # Ask for rematch
    while True:
        play_again = input("\nPlay again? (y/n): ").lower().strip()
        if play_again in ['y', 'yes']:
            print("\n" * 2)
            play_hangman()
            break
        elif play_again in ['n', 'no']:
            print("Thanks for playing! Goodbye!")
            break
        else:
            print("Please enter 'y' for yes or 'n' for no.")

if __name__ == "__main__":
    play_hangman()
