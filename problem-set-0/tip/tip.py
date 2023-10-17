def main():
    # Prompt the user for the cost of the meal and store it as a floating-point number.
    dollars = dollars_to_float(input("How much was the meal? (in the format '$##.##'): "))

    # Prompt the user for the tip percentage and store it as a floating-point number.
    percent = percent_to_float(input("What percentage would you like to tip? (in the format '##%'): "))

     # Calculate the tip amount by multiplying the meal cost by the tip percentage.
    tip = dollars * percent

    # Display the calculated tip amount with two decimal places.
    print(f"Leave ${tip:.2f}")


def dollars_to_float(dollars:str):
    # Remove $ from dollars string
    dollars = dollars.replace("$", "")

    # Create float from dollars string
    float_dollars = float(dollars)

    return float_dollars


def percent_to_float(percent:str):
    # Remove % from percent string
    percent = percent.replace("%", "")

    # Create float from percent string
    float_percent = float(percent)

    # Convert the percentage value into a decimal value.
    float_percent = float_percent / 100

    return float_percent


main()