import random
from words import word_list
import sys


def main():
    # Get a random word
    secret_word = get_word()

    # Start the game
    play_game(secret_word)

    # Ask the user if they want to play again
    prompt_play_again()


def prompt_play_again():
    while True:
        # Get user input to play again or exit
        user_input = input("Do you want to play again? (Y/N): ").strip().upper()

        if user_input == "Y":
            # Get a new secret word and start a new game
            new_secret_word = get_word()
            play_game(new_secret_word)
        elif user_input == "N":
            sys.exit()
        else:
            print("Invalid input. Please enter Y or N.")


def play_game(secret_word):
    guessed_letters = []
    attempts_left = 6

    print("Welcome to Hangman!")

    while attempts_left > 0:
        # Display the current state of the word
        print("\n" + "Secret Word: " + display_word(secret_word, guessed_letters))

        # Get a guess from the player
        guess = input("Guess a letter: ").upper()

        # Check if the guess is a single letter
        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.")
            continue

        # Check if the letter has already been guessed
        if guess in guessed_letters:
            print("You've already guessed that letter. Try again.")
            continue

        # Add the letter to the list of guessed letters
        guessed_letters.append(guess)

        # Check if the letter is in the word
        if guess not in secret_word:
            attempts_left -= 1
            print(f"Wrong guess! Attempts left: {attempts_left}")
            print(display_hangman(attempts_left))
        else:
            print(f"Correct guess! {guess} is in the secret word!")
        # Check if the player has guessed all the letters
        if all(letter in guessed_letters for letter in secret_word):
            print("Congratulations! You guessed the word:", secret_word)
            break

    if attempts_left == 0:
        print("Sorry, you ran out of attempts. The correct word was:", secret_word)


def get_word():
    secret_word = random.choice(word_list)
    return secret_word.upper()


def display_word(secret_word, guessed_letters):
    # Create a string to display the current state of the word
    display = ""
    for letter in secret_word:
        if letter in guessed_letters:
            display += letter
        else:
            display += "_"
    return display


def display_hangman(tries):
    stages = [  # final state: head, torso, both arms, and both legs
        """
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |     / \\
                   -
                """,
        # head, torso, both arms, and one leg
        """
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |     / 
                   -
                """,
        # head, torso, and both arms
        """
                   --------
                   |      |
                   |      O
                   |     \|/
                   |      |
                   |      
                   -
                """,
        # head, torso, and one arm
        """
                   --------
                   |      |
                   |      O
                   |     \|
                   |      |
                   |     
                   -
                """,
        # head and torso
        """
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                """,
        # head
        """
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                """,
        # initial empty state
        """
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                """,
    ]
    return stages[tries]


if __name__ == "__main__":
    main()
