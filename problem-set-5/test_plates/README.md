# License Plate Validator

The License Plate Validator is a Python program that allows users to input a license plate string and checks its validity against specific criteria. A valid license plate must meet the following conditions:

1. It must start with at least two alphabetic characters.
2. It must be between 2 and 6 characters in length (inclusive).
3. Numbers cannot be used in the middle of a plate, and the first number used cannot be '0'.
4. It must have no periods, spaces, or punctuation marks.

## Usage

To use the License Plate Validator:

1. Run the script by executing the main function.
2. Input a license plate when prompted.
3. The program will then check the provided license plate against the specified criteria and display "Valid" if it meets all conditions or "Invalid" if it doesn't.

## Functions

- **main():** This function is the entry point of the program. It prompts the user for a license plate input and checks if it is valid.

- **is_valid(s):** This function checks if a license plate string is valid based on specific criteria. It returns `True` if the license plate is valid and `False` otherwise.

- **has_valid_start(s):** This function checks if the provided string starts with at least two alphabetic characters. It returns `True` if the string starts with two alphabetic characters and `False` otherwise.

- **has_valid_length(s):** This function checks if the length of the provided string is between 2 and 6 characters (inclusive). It returns `True` if the string length is within the valid range and `False` otherwise.

- **has_valid_numbers(s):** This function checks if the provided string adheres to the rule that plate numbers cannot be used in the middle of a plate, and the first number used cannot be '0'. It returns `True` if the string follows the number placement rules and `False` otherwise.

- **has_valid_chars(s):** This function checks if the provided string contains no periods, spaces, or punctuation marks. It returns `True` if the string contains only valid characters and `False` otherwise.
