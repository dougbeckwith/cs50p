"""
A simple addition problem game.

This program allows the user to select a difficulty level (1, 2, or 3) and then presents
10 addition problems based on the chosen level. Users have up to 3 attempts to provide the
correct answer for each problem. The program keeps track of the number of correct answers
and displays the score at the end.

Usage:
Run this script to play the game.
"""

import random
import sys


def main():
    """
    Main function to run an addition problem game.

    The game prompts the user for a difficulty level (1, 2, or 3) and then presents
    10 addition problems based on the chosen level. Users have up to 3 attempts to
    provide the correct answer for each problem. The program keeps track of the
    number of correct answers and displays the score at the end.

    Returns:
        None
    """
    difficulty_level = get_level()  # Get the desired difficulty level.
    correct_answers_count = 0

    # Create and ask user 10 addition problems based on level.
    for _ in range(10):
        attempts = 0
        num1 = generate_integer(difficulty_level)
        num2 = generate_integer(difficulty_level)
        correct_answer = num1 + num2
        # Continue to prompt user for answer for each probem (max of 3 attempts).
        while True:
            answer = input(f"{num1} + {num2} = ")
            attempts += 1
            try:
                answer = int(answer)
            except ValueError:
                pass
            else:
                if answer == correct_answer:
                    correct_answers_count += 1
                    break
                # If the user fails to answer correctly after 3 attempts, print the correct answer and move to the next problem.
                if attempts >= 3:
                    print("EEE")
                    print(f"{num1} + {num2} = {correct_answer}")
                    break

                print("EEE")
                continue

    print(f"Score: {correct_answers_count}")
    sys.exit()


# Function to prompt the user for the difficulty level (1, 2, or 3).
def get_level():
    """
    Prompt the user for the desired difficulty level.

    The function continuously prompts the user until a valid difficulty level
    (1, 2, or 3) is chosen.

    Returns:
        int: The selected difficulty level.
    """
    while True:
        try:
            selected_level = int(input("Level: "))
        except ValueError:
            pass
        else:
            if selected_level < 1 or selected_level > 3:
                continue
            else:
                return selected_level


# Generate random integers based on the selected difficulty level (1, 2, or 3).
def generate_integer(difficulty_level):
    """
    Generate a random integer based on the selected difficulty level.

    Args:
        difficulty_level (int): The chosen difficulty level (1, 2, or 3).

    Returns:
        int: A random integer within the appropriate range for the given difficulty level.
    """
    if difficulty_level == 1:
        return random.randint(0, 9)
    if difficulty_level == 2:
        return random.randint(10, 99)
    return random.randint(100, 999)


if __name__ == "__main__":
    main()
