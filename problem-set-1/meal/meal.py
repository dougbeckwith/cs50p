def main():
    # Prompt user for a time
    time = input("What time is it? ")
    # Convert the user input into a numeric time format
    time = convert(time)

    # Check if it's mealtime
    if time >= 7.00 and time <= 8.00:
        print("breakfast time")
    elif time >= 12.00 and time <= 13.00:
        print("lunch time")
    elif time >= 18.00 and time <= 19.00:
        print("dinner time")
    return None

def convert(time:str):
    # Replace the colon with a period to handle time input like "7:30"
    time = time.replace(":", ".")

    # Split the modified time string into hours and minutes
    hours, minutes = map(int, time.split('.'))

    # Calculate the total time in hours with two decimal places
    total_hours = round(hours + minutes / 60, 2)

    return total_hours


if __name__ == "__main__":
    main()