import sys
import os
import csv
from tabulate import tabulate

def main():
    # Check command-line arguments and read the CSV file.
    check_command_line_args()
    headers, rows = read_csv(sys.argv[1])

    # Display the CSV data in a tabular format.
    print(tabulate(rows, headers=headers, tablefmt="grid"))


# Function to read the CSV file and return the headers and rows.
def read_csv(file_path):
    try:
        with open(file_path, "r") as file:
            csvreader = csv.reader(file)
            headers = next(csvreader) # Read the header row.
            rows = list(csvreader) # Read all data rows.
            return headers, rows

    except FileNotFoundError:
        print("File not found")
   

# Function to check and validate the command-line arguments.
def check_command_line_args():
    arg_length = len(sys.argv)
    file_path = sys.argv[1]

    if arg_length < 2:
        sys.exit("Too few command-line arguments")
    if arg_length > 2:
        sys.exit("Too many command-line arguments")
    
    if not file_path.endswith(".csv"):
        sys.exit("Not a CSV file")
    if not os.path.exists(file_path):
        sys.exit("File does not exist")


if __name__ == "__main__":
    main()