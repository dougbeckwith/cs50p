"""
This Python script provides a simple utility to calculate a payment amount based on a user's 
greeting.

The main function, `main()`, takes user input for a greeting, calculates the payment amount using 
the `value()` function, and prints the result in the format "$X". The `value()` function evaluates 
the greeting and applies specific payment rules.
"""


def main():
    user_greeting = input("Greeting: ")
    payment_amount = value(user_greeting)
    print(f"${payment_amount}")


def value(greeting):
    """
    Calculate a payment amount based on a given greeting string.

    The payment calculation is as follows:
    - If the greeting starts with "hello," the payment amount is 0.
    - If the greeting starts with "h," the payment amount is 20.
    - For all other cases, the payment amount is 100.

    Args:
        greeting (str): The greeting provided by the user.

    Returns:
        int: The payment amount calculated based on the greeting.
    """
    greeting = greeting.lstrip().lower()
    if len(greeting) >= 5 and greeting[:5] == "hello":
        return 0
    if len(greeting) >= 1 and greeting[:1] == "h":
        return 20
    return 100


if __name__ == "__main__":
    main()
