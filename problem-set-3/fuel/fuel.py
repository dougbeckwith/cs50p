def main():
    # Get fraction from user in format X/Y
    fraction = get_fraction()
    print_percent(fraction)

def get_fraction():
    while True:
        fraction = input("Fraction: ")

        # Attempt to split the input into X and Y parts using the '/' separator
        try:
            x, y = fraction.split("/")
        except ValueError:
            print("value error")
            continue
        
        # Check if the denominator Y is '0', which is not allowed
        if y == "0":
            print("Y can not be 0")
            continue
       
        # Attempt to convert X and Y to integers
        try:
            x = int(x)
        except ValueError:
            print("X is not an int")
            continue
        try:
            y = int(y)
        except ValueError:
            print("Y is not a int")
            continue
        
        # Check if X is greater than Y, which is not allowed for a proper fraction
        if x > y:
            print("X can not be greater than Y")
            continue

        return {"x":x, "y":y}
        

def print_percent(fraction):
    decimal_value = fraction["x"] / fraction["y"]
    percentage = convert_to_percent(decimal_value)
    match percentage:
        case 0:
            print("E")
        case 1:
            print("E")
        case 100:
            print("F")
        case 99:
            print("F")
        case _:
            print(f"{percentage}%")

def convert_to_percent(decimal):
    # Convert a decimal value to a rounded percentage (e.g., 0.25 to 25%)
    return round(decimal * 100)


main()