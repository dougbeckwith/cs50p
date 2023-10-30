"""
License Plate Validator

This program allows the user to input a license plate string and checks its validity 
against specific criteria. A valid license plate must meet the following conditions:
1. It must start with at least two alphabetic characters.
2. It must be between 2 and 6 characters in length (inclusive).
3. Numbers cannot be used in the middle of a plate, and the first number used cannot be '0'.
4. It must have no periods, spaces, or punctuation marks.

"""


def main():
    """
    This function is the entry point of the program. It prompts the user for a license plate
    input and checks if it is valid. If the plate is valid, it prints "Valid";
    otherwise, it prints "Invalid".
    """
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    """
    Check if a license plate string is valid based on specific criteria.

    Parameters:
        s (str): The license plate string to be checked.

    Returns:
        bool: True if the license plate is valid, False otherwise.
    """
    # Plate must start with at least two letters.
    if not has_valid_start(s):
        return False

    # Plate must be between 2 and 6 chars long (inclusive)
    if not has_valid_length(s):
        return False

    # Plate numbers cannot be used in the middle of a plate. The first number used cannot be a 0.
    if not has_valid_numbers(s):
        return False

    # Plate must have no periods, spaces, or punctuation marks.
    if not has_valid_chars(s):
        return False
    return True


def has_valid_start(s):
    """
    Check if the provided string starts with at least two alphabetic characters.

    Parameters:
        s (str): The string to be checked.

    Returns:
        bool: True if the string starts with at least two alphabetic characters, False otherwise.
    """
    if len(s) < 2:
        return False

    first_two = s[0:2]

    # Check if the first two characters are alphabetic
    if first_two.isalpha():
        return True
    else:
        return False


def has_valid_length(s):
    """
    Check if the length of the provided string is between 2 and 6 characters (inclusive).

    Parameters:
        s (str): The string to be checked.

    Returns:
        bool: True if the string length is within the valid range, False otherwise.
    """
    length_string = len(s)

    if length_string < 2 or length_string > 6:
        return False
    return True


def has_valid_numbers(s):
    """
    Check if the provided string adheres to the rule that plate numbers cannot be used
    in the middle of a plate, and the first number used cannot be a 0.

    Parameters:
        s (str): The string to be checked.

    Returns:
        bool: True if the string follows the number placement rules, False otherwise.
    """
    first_digit_found = False

    for char in s:
        # Check if the character is numeric and marks the start of numbers
        if first_digit_found is False and char == "0":
            return False
        if first_digit_found is False and char.isnumeric():
            first_digit_found = True
            continue

        # Check if characters after the first digit are not numeric
        if first_digit_found is True and not char.isnumeric():
            return False
        continue
    return True


def has_valid_chars(s):
    """
    Check if the provided string contains no periods, spaces, or punctuation marks.

    Parameters:
        s (str): The string to be checked.

    Returns:
        bool: True if the string contains only valid characters, False otherwise.
    """
    chars_not_allowed = [".", "!", " "]

    for char in s:
        if char in chars_not_allowed:
            return False
    return True


if __name__ == "__main__":
    main()
