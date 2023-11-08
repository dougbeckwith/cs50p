import re
import sys

# Function to convert a time range in 12-hour format to 24-hour format and print the result
def main():
   
    # Prompt the user for input and call the 'convert' function
    try:
        print(convert(input("Hours: ")))
    except ValueError:
        sys.exit("ValueError")

      


# Function to convert a time range from 12-hour format to 24-hour format
def convert(s):
    # Dictionary for converting 12-hour time to 24-hour time
    twelve_to_twenty_four = {
        "12 AM": "00",
        "1 AM": "01",
        "2 AM": "02",
        "3 AM": "03",
        "4 AM": "04",
        "5 AM": "05",
        "6 AM": "06",
        "7 AM": "07",
        "8 AM": "08",
        "9 AM": "09",
        "10 AM": "10",
        "11 AM": "11",
        "12 PM": "12",
        "1 PM": "13",
        "2 PM": "14",
        "3 PM": "15",
        "4 PM": "16",
        "5 PM": "17",
        "6 PM": "18",
        "7 PM": "19",
        "8 PM": "20",
        "9 PM": "21",
        "10 PM": "22",
        "11 PM": "23",
    }

    # Use a regular expression to match and capture a time range in 12-hour format
    match = re.search(
        r"(1[0-2]|[1-9]):?([0-5][0-9])? (AM|PM) to (1[0-2]|[1-9]):?([0-5][0-9])? (AM|PM)",
        s,
    )

    if match:
        # Convert the start and end times to 24-hour format using the dictionary
        start_24_hour = twelve_to_twenty_four[match.group(1) + " " + match.group(3)]
        end_24_hour = twelve_to_twenty_four[match.group(4) + " " + match.group(6)]

        # Extract and handle the minutes part of the time, default to "00" if not provided
        start_24_min = match.group(2) if match.group(2) is not None else "00"
        end_24_min = match.group(5) if match.group(5) is not None else "00"

        # Format the result in 24-hour format
        twenty_four_hour = (
            f"{start_24_hour}:{start_24_min} to {end_24_hour}:{end_24_min}"
        )

        return twenty_four_hour

    # Raise a 'ValueError' if the input doesn't match the expected format
    raise ValueError


if __name__ == "__main__":
    main()
