"""
main.py: druhý projekt do Engeto Online Python Akademie

author: Svitlana Demianiuk
email: sveta.grigorenko.1997@gmail.com
"""

import time
import random
import sys  # Pro bezpečné ukončení programu

# Přivítání hráče
def welcome():
    print("Hi there!")
    print("-" * 47)
    print("I've generated a random 4 digit number for you")
    print("Let's play a bulls and cows game.")
    print("Type 'exit' anytime to quit.")
    print("-" * 47)

# Vygeneruje náhodné čtyřmístné číslo s unikátními číslicemi, nezačíná nulou
def generate_secret_number():
    digits = list("123456789")
    first_digit = random.choice(digits)
    remaining_digits = list(set("0123456789") - set(first_digit))
    rest = random.sample(remaining_digits, 3)
    return first_digit + ''.join(rest)

# Získá vstup od uživatele a zkontroluje jeho platnost
def get_user_guess():
    while True:
        guess = input("Enter a 4-digit number (or type 'exit' to quit): ")
        if guess.lower() == "exit":
            return None
        if len(guess) != 4:
            print("The number must have exactly 4 digits.")
        elif not guess.isdigit():
            print("The input must be a number.")
        elif guess[0] == "0":
            print("The number must not start with zero.")
        elif len(set(guess)) != 4:
            print("All digits must be unique.")
        else:
            return guess

# Spočítá bulls a cows podle zadání
def count_bulls_and_cows(secret, guess):
    bulls = sum(s == g for s, g in zip(secret, guess))
    cows = len(set(secret) & set(guess)) - bulls
    return bulls, cows

# Hlavní logika programu
if __name__ == "__main__":
    welcome()

    total_games = 0
    total_time = 0
    total_guesses = 0

    while True:  # Smyčka pro více her
        secret = generate_secret_number()
        print("Secret number:", secret)  # Dočasně zobrazíme pro testování

        guesses = 0
        start_time = time.time()

        while True:  # Smyčka pro jednu hru
            guess = get_user_guess()

            if guess is None:
                print("You exited the game.")
                print("Thanks for playing! Goodbye 👋")
                sys.exit()  # Ukončí celý program

            guesses += 1
            bulls, cows = count_bulls_and_cows(secret, guess)

            bull_word = "bull" if bulls == 1 else "bulls"
            cow_word = "cow" if cows == 1 else "cows"

            if bulls == 4:
                print(f"Correct, you've guessed the right number in {guesses} guesses!")
                break
            else:
                print(f"{bulls} {bull_word}, {cows} {cow_word}")

        # Statistiky po skončení hry
        end_time = time.time()
        duration = end_time - start_time

        total_games += 1
        total_time += duration
        total_guesses += guesses

        avg_time = total_time / total_games
        avg_guesses = total_guesses / total_games

        print("\nThat's amazing!")
        print("--- Game stats ---")
        print(f"Games played: {total_games}")
        print(f"Average time: {avg_time:.2f} seconds")
        print(f"Average guesses: {avg_guesses:.2f}")
        print("-" * 47)

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for playing! Goodbye 👋")
            break
  