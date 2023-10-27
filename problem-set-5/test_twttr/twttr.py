"""
This script takes user input and removes specified characters from the input string.
"""


def main():
    """
    Main function to take user input and print the input string with specified characters 
    removed.
    """

    user_input = input("Input: ")
    print(shorten(user_input))


def shorten(string):
    """
    Remove specified characters from a given string and return the modified string.

    Args:
        string (str): The input string from which characters will be removed.
        chars_to_remove (list of str): A list of characters to remove from the input string.

    Returns:
        str: The input string with specified characters removed.
    """
    result_string = ""
    chars_to_remove = ["a", "e", "i", "o", "u"]

    for char in string:
        if char.lower() not in chars_to_remove:
            result_string += char

    return result_string


if __name__ == "__main__":
    main()
