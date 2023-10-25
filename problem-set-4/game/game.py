"""
Random Number Guessing Game

This module provides a simple random number guessing game. It allows the user to
choose a game level and then guess a random number within that level.
"""

import random
import sys

ERROR_MESSAGE = "The value must be a positive integer in digit format."


def main():
    """
    Start the random number guessing game.

    This function initiates the random number guessing game. It prompts the user to
    select a game level and generates a random number within that level.
    """
    level = prompt_for_level()
    random_number = random.randint(1, level)
    prompt_for_guess(random_number)


def prompt_for_guess(random_number):
    """
    Prompt the user for a guess and provide feedback in the random number guessing game.

    This function repeatedly prompts the user to make a guess in the random number
    guessing game. It handles user input validation, provides feedback on the guess,
    and terminates the game when the correct number is guessed.

    Parameters:
    - `random_number` (int): The random number that the user is trying to guess.
    """
    while True:
        try:
            guess = int(input("Guess: "))
        except ValueError:
            print(ERROR_MESSAGE)
            continue
        else:
            if guess < 1:
                continue
            if guess < random_number:
                print("Too small!")
            elif guess > random_number:
                print("Too large!")
            else:
                print("Just right!")
                sys.exit()
            continue


def prompt_for_level():
    """
    Prompt the user to choose a game level.

    This function prompts the user to choose a game level,
    which determines the range of numbers for the guessing game.

    Returns:
    - `level` (int): The chosen game level.
    """
    while True:
        try:
            level = int(input("Level: "))
        except ValueError:
            print(ERROR_MESSAGE)
            continue
        else:
            if level < 1:
                print(ERROR_MESSAGE)
                continue
        return level


if __name__ == "__main__":
    main()
