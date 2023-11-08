"""
This program validates IPv4 addresses by checking if each component (between the dots)
is a number between 0 and 255. It uses a regular expression pattern to match valid
IPv4 addresses and returns True if the provided IP address is valid, or False if it is
invalid.

Usage:
- Run the program, and it will prompt you to enter an IPv4 address.
- The program will then check the provided address against the defined pattern.
- If the IP address is valid, it will return True; otherwise, it will return False.

Example:
>>> IPv4 Address: 192.168.1.1
True

>>> IPv4 Address: 256.0.0.1
False

>>> IPv4 Address: 01.23.45.67
False
"""

import re


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    # Define a regular expression pattern to match a valid IP address
    ip_pattern = r"^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"

    # Use the regular expression to check if the provided IP address matches the pattern
    if re.match(ip_pattern, ip):
        return True
    else:
        return False


if __name__ == "__main__":
    main()
