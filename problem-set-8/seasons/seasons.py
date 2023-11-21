import sys
from datetime import date
import re
import inflect


def main():
    birth_date = input("Date of Birth: ")
    try:
        year, month, day = check_birth_date(birth_date)
    except:
        sys.exit("Invalid Date")
    birth_date = date(int(year), int(month), int(day))
    today_date = date.today()
    date_diff = today_date - birth_date

    mins = date_diff.days * 24 * 60
    words = convert_minutes_to_words(mins)
    print(create_ouput(words))


def check_birth_date(birth_date):
    if re.search(r"^\d{4}-\d{2}-\d{2}$", birth_date):
        year, month, day = birth_date.split("-")
        return year, month, day


def convert_minutes_to_words(minutes):
    inflector = inflect.engine()
    return inflector.number_to_words(minutes, andword="")


def create_ouput(words):
    return f"{words.capitalize()} minutes"


if __name__ == "__main__":
    main()
