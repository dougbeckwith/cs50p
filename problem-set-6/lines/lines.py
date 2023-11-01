import sys
import pathlib
import os


def main():
    """
    Count non-empty and non-comment lines in a Python file and print the count.

    This script reads a Python file specified as a command-line argument,
    counts the lines that are not empty or comments, and prints the count.

    Usage:
    $ python lines.py filename.py

    Args:
        None

    Returns:
        None
    """
    check_command_line_args()

    line_count = 0
    try:
        with open(sys.argv[1], "r", encoding="utf-8") as file:
            lines = file.readlines()

        for line in lines:
            if is_empty_or_comment(line) is False:
                line_count += 1

    except FileNotFoundError:
        print("File not found")

    print(line_count)
    sys.exit(0)


def check_command_line_args():
    arg_length = len(sys.argv)
    if arg_length < 2:
        sys.exit("Too few command-line arguments")
    if arg_length > 2:
        sys.exit("Too many command-line arguments")
    if pathlib.Path(sys.argv[1]).suffix != ".py":
        sys.exit("Not a Python file")
    if os.path.exists(sys.argv[1]) is False:
        sys.exit("File does not exist")


def is_empty_or_comment(line):
    if line.isspace() or line.lstrip().startswith("#"):
        return True
    return False


if __name__ == "__main__":
    main()
