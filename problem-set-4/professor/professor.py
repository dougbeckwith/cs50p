import random
import sys


def main():
    difficulty_level = get_level() # Get the desired difficulty level.
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
                elif attempts >= 3:
                    print("EEE")
                    print(f"{num1} + {num2} = {correct_answer}")
                    break
                else:
                    print("EEE")
                    continue
    print(f"Score: {correct_answers_count}")
    sys.exit()

# Function to prompt the user for the difficulty level (1, 2, or 3).
def get_level():
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
    if difficulty_level == 1:
        return random.randint(0, 9)
    elif difficulty_level == 2:
        return random.randint(10, 99)
    else:
        return random.randint(100, 999)


if __name__ == "__main__":
    main()
