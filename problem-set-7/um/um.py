import re


def main():
    print(count(input("Text: ")))


def count(s):
    # Use regular expressions to find standalone "um"s (case-insensitive)
    return len(re.findall(r'\bum\b', s, re.IGNORECASE))


if __name__ == "__main__":
    main()