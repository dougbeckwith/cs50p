def main():
    # Assume input is uppercased
    plate = input("Plate: ") 
    if is_valid(plate): 
        print("Valid")
    else:
        print("Invalid")

# Check if plate is valid
def is_valid(s):
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
    first_two = s[0:2]

    # Check if the first two characters are alphabetic
    if first_two.isalpha():
        return True
    else:
        return False


def has_valid_length(s):
    length_string = len(s)

    # Check if the length is between 2 and 6 characters (inclusive)
    if length_string < 2 or length_string > 6:
        return False
    return True


def has_valid_numbers(s):
    first_digit_found = False

    for char in s:
        # Check if the character is numeric and marks the start of numbers
        if first_digit_found == False and char == "0":
            return False
        elif first_digit_found == False and char.isnumeric():
            first_digit_found = True
            continue
        
        # Check if characters after the first digit are not numeric
        if first_digit_found == True and not char.isnumeric():
            return False   
        else:
            continue   
    return True


def has_valid_chars(s):
    chars_not_allowed = ['.', '!', ' ']

    # Check if any disallowed characters are present in the input string
    for char in s:
        if char in chars_not_allowed:
            return False
    return True


main()
