# Bulls and Cows — Python Console Game

## Project Overview
This project was developed as part of the Engeto Online Python Academy.
It is a console-based implementation of the classic *Bulls and Cows* guessing game.

The application generates a random 4-digit number with unique digits and guides
the user through the game using validated input, feedback, and basic statistics.

---

## Key Features
- Random generation of a valid 4-digit secret number (no leading zero, unique digits)
- User input validation with clear error messages
- Bulls and cows calculation logic
- Game loop with the option to play multiple rounds
- Basic game statistics:
  - number of games played
  - average time per game
  - average number of guesses
- Graceful program exit handling

---

## Technologies Used
- Python
- Standard Python libraries (`random`, `time`, `sys`)

---

## How It Works
1. The program welcomes the user and explains the game rules.
2. A random secret number is generated.
3. The user enters guesses until the correct number is found.
4. After each guess, the program displays the number of bulls and cows.
5. When the game ends, statistics are shown and the user can choose to play again.

---

## Example Gameplay
```text
Enter a 4-digit number: 1234
1 bull, 2 cows
Enter a 4-digit number: 5678
0 bulls, 1 cow
Correct, you've guessed the right number in 6 guesses!
