import sys
import os
import csv


def main():
    # Check command-line arguments and retrieve input and output file paths.
    check_command_line_args()
    input_file = sys.argv[1]
    output_file = sys.argv[2]

    csv_data = read_csv(input_file)

    if csv_data:
        # Clean up the data by splitting the "name" column into "first" and "last."
        reformated_data = reformat_data(csv_data)

        # Write the cleaned data to the output CSV file.
        write_csv(output_file, reformated_data)


def reformat_data(csv_data):
    reformated_data = []
    for row in csv_data:
        last, first = row["name"].split(", ")
        person = {"first": first, "last": last, "house": row["house"]}
        reformated_data.append(person)
    return reformated_data


def write_csv(file_path, csv_data):
    fieldnames = ["first", "last", "house"]
    with open(file_path, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(csv_data)


def read_csv(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            csvreader = csv.DictReader(file)
            data = list(csvreader)
            return data
    except FileNotFoundError:
        sys.exit(f"File not found: {file_path}")


def check_command_line_args():
    arg_length = len(sys.argv)
    if arg_length < 3:
        sys.exit("Too few command-line arguments")
    if arg_length > 3:
        sys.exit("Too many command-line arguments")

    file_path = sys.argv[1]
    if not file_path.endswith(".csv"):
        sys.exit("Not a CSV file")
    if not os.path.exists(file_path):
        sys.exit("File does not exist")


if __name__ == "__main__":
    main()
