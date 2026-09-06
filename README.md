🎮 Python Hangman Game

A fun command-line Hangman game built with Python where the player attempts to guess a randomly selected word one letter at a time before running out of incorrect guesses.

The project was created to practice Python fundamentals, game logic, user input validation, collections, loops, and random selection.

---

✨ Features

- 🎲 Randomly selects a word for each game
- 🔤 Allows the player to guess one letter at a time
- ✅ Detects correct guesses
- ❌ Tracks incorrect guesses
- 🔁 Prevents repeated letter guesses
- ❤️ Displays the number of incorrect guesses remaining
- 🧩 Shows the Hangman drawing based on incorrect guesses
- 🏆 Detects winning and losing conditions
- 🔄 Allows the player to start a new game
- ⚠️ Validates user input

---

🛠️ Technologies Used

- Python 3
- "random" — randomly selects words
- Sets — tracks previously guessed letters
- Lists — stores the word display and incorrect guesses
- Functions — organizes the game logic
- Loops — controls gameplay
- Conditional statements
- String manipulation
- User input and validation

---

📂 Project Structure

python-hangman-game/
<br>
│
<br>
├── hangman.py
<br>
└── README.md
<br>
---

🚀 Getting Started

Prerequisites

Make sure Python 3 is installed.

Check your Python version:

python --version

Clone the Repository

git clone https://github.com/YOUR_USERNAME/python-hangman-game.git

Navigate to the Project

cd python-hangman-game

Run the Game

python hangman.py

---

🎮 How to Play

1. Start the program.
2. The game randomly selects a word.
3. The hidden word is displayed using underscores.
4. Enter one letter at a time.
5. Correct letters are revealed in the word.
6. Incorrect letters reduce the number of guesses remaining.
7. Guess the complete word before running out of attempts.
8. Choose whether to play again after the game ends.

---

🧩 Example Gameplay

🎮 Welcome to Hangman!
The word has 6 letters.

________________________________________

  +---+
  <br>
  |   |
  <br>
      |
  <br>
      |
  <br>
      |
  <br>    
      |
  <br>    
=========
<br>

Word _ _ _ _ _ _
Guess letters None
Wrong letter guessed None
Incorrect guesses left 6

Guess a letter: p

✓ Good guess! 'p' is in the word.

The Hangman drawing changes as incorrect guesses increase.

---

📚 Current Word List

The current version includes several programming-related words, such as:

- Python
- Hangman
- Computer
- JavaScript
- Programmer

The program randomly selects one of these words at the beginning of each game.

---

🧠 Python Concepts Demonstrated

This project demonstrates:

- Variables
- Functions
- Function parameters
- Lists
- Sets
- Strings
- "random.choice()"
- "while" loops
- "for" loops
- "if/elif/else"
- User input
- Input validation
- String methods
- "enumerate()"
- Basic game-state management
- Modular programming

---

🔄 Game Flow

Start Game
    ↓
Randomly Select Word
    ↓
Hide Letters
    ↓
Ask Player for a Letter
    ↓
Validate Input
    ↓
Is Letter in Word?
   ↙              ↘
 Yes              No
  ↓                ↓
Reveal Letter   Reduce Attempts
   ↘              ↙
    Check Game Status
          ↓
   ┌──────┴──────┐
   ↓             ↓
 Win           Lose
   ↓             ↓
Play Again? ←────┘

---

🔮 Future Improvements

Possible improvements for future versions:

- [ ] Add more words
- [ ] Add different difficulty levels
- [ ] Add word categories
- [ ] Randomize words from a larger external word list
- [ ] Add a scoring system
- [ ] Track wins and losses
- [ ] Add a graphical user interface
- [ ] Add sound effects
- [ ] Add multiplayer mode
- [ ] Add automated tests

---

🎯 Learning Objective

The purpose of this project was to strengthen Python programming fundamentals by building an interactive application.

Through this project, I practiced functions, loops, sets, lists, string manipulation, randomization, input validation, and game-state logic.

---
