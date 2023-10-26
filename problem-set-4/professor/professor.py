import random

math_problems = []


def main():
    level = get_level()

    # Create 10 math problems
    for _ in range(10):
        x = generate_integer(level)
        y = generate_integer(level)
        a = x + y
        math_problems.append({"x": x, "y": y, "a": a})

    
    # Prompt user to answer each math problem and keep track of correct answers with score
    score = 0
    for problem in math_problems:
        tries = 0
        # Continue to prompt user for answer for each probem (max of 3 tries).
        while True:
            answer = input(f"{problem['x']} + {problem['y']} = ")
            tries += 1
            try:
                answer = int(answer)
            except ValueError:
                pass
            else:
                if answer == problem["a"]:
                    score += 1
                    break
                # Print answer to user and move onto next problem
                elif tries >= 3:
                    print("EEE")
                    print(f"{problem['x']} + {problem['y']} = {problem['a']}")
                    break
                else:
                    print("EEE")
                    continue
    print(f"Score: {score}")

# Continues to prompt user for level until 1,2 or 3 is chosen.
def get_level():
    while True:
        try:
            level_choice = int(input("Level: "))
        except ValueError:
            pass
        else:
            if level_choice < 1 or level_choice > 3:
                continue
            else:
                return level_choice


# returns level digits or raises a Value Error if level is not 1,2 or 3
def generate_integer(level):
    if level == 1:
        return random.randrange(0, 9)
    elif level == 2:
        return random.randrange(10, 99)
    else:
        return random.randrange(100, 999)


if __name__ == "__main__":
    main()
