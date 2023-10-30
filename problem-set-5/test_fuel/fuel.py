import sys


def main():
    # Get a fraction from user input
    fraction = get_fraction()
    try:
        # Attempt to convert the fraction to a percentage
        percentage = convert(fraction)
    except (ValueError, ZeroDivisionError):
        # Handle exceptions for invalid input formats
        sys.exit()

    gauge_value = gauge(percentage)
    print(gauge_value)


def convert(fraction):
    # Check if the fraction is in the format X/Y
    if "/" in fraction:
        x, y = fraction.split("/")
    else:
        # Raise a ValueError if the format is incorrect
        raise ValueError

    # Convert X and Y to integers
    try:
        x = int(x)
    except ValueError as exc:
        raise ValueError from exc

    try:
        y = int(y)
    except ValueError as exc:
        raise ValueError from exc

    # Check if the denominator is zero and raise a ZeroDivisionError if true
    if y == 0:
        raise ZeroDivisionError

    if x > y:
        raise ValueError

    # Calculate the percentage and return it
    decimal = x / y
    percentage = round(decimal * 100)
    return percentage


def gauge(percentage):
    # Determine a gauge value based on the percentage
    match percentage:
        case 0:
            return "E"
        case 1:
            return "E"
        case 100:
            return "F"
        case 99:
            return "F"
        case _:
            return f"{percentage}%"


def get_fraction():
    # Prompt the user to enter a fraction
    fraction = input("Fraction: ")
    return fraction


if __name__ == "__main__":
    main()
