"""
Bitcoin Value Calculator

This script calculates the total value of Bitcoin holdings in USD based on the quantity
of Bitcoin owned by the user and the current price of Bitcoin in USD fetched from an online source.

Usage:
    Run this script with a command-line argument representing the quantity of Bitcoin.
    Example: python bitcoin_calculator.py 2.5

Dependencies:
    - Python 3
    - requests library
"""

import sys
import requests


def main():
    """
    Main function to calculate the total value of Bitcoin holdings in USD.

    This program takes a command-line argument representing the quantity of Bitcoin
    owned by the user and fetches the current price of Bitcoin in USD from an online source.
    It then calculates and prints the total value of the user's Bitcoin holdings.

    Args:
        None

    Returns:
        None
    """
    if len(sys.argv) != 2:
        sys.exit("Missing command-line argument")

    bitcoin_quantity = convert_to_float(sys.argv[1])
    bitcoin_price = get_current_bitcoin_price_usd()

    print_total(bitcoin_quantity, bitcoin_price)


def get_current_bitcoin_price_usd():
    """
    Fetch the current price of Bitcoin in USD.

    This function sends an HTTP GET request to an online source to retrieve the current price of
    Bitcoin in USD. It handles potential issues like network problems, JSON parsing errors,
    and missing data.

    Args:
        None

    Returns:
        float: The current price of Bitcoin in USD.

    Raises:
        SystemExit: If there are issues with the HTTP request, JSON parsing, or if no Bitcoin price
        is found.
    """
    try:
        response = requests.get(
            "https://api.coindesk.com/v1/bpi/currentprice.json", timeout=None
        )
    except requests.RequestException:
        sys.exit("Problem with request")

    try:
        data = response.json()
    except requests.RequestException:
        sys.exit("Problem with JSON")

    if "bpi" in data and "USD" in data["bpi"] and "rate" in data["bpi"]["USD"]:
        price_str = data["bpi"]["USD"]["rate"]
        price_str = price_str.replace(",", "")
    else:
        sys.exit("No bitcoin price found")

    try:
        price = float(price_str)
    except ValueError:
        sys.exit("Problem converting to float")

    return price


def print_total(quantity, total_amount):
    """
    Print the total value of Bitcoin holdings.

    This function takes the quantity of Bitcoin and its current price and calculates the total
    value in USD. It then prints the total value with four decimal places and a currency symbol.

    Args:
        quantity (float): The quantity of Bitcoin.
        total_amount (float): The current price of Bitcoin in USD.

    Returns:
        None
    """
    total_amount = total_amount * quantity
    print(f"${total_amount:,.4f}")


def convert_to_float(arg):
    """
    Convert a command-line argument to a float.

    This function takes a command-line argument, attempts to convert it to a float, and validates
    that it's a positive number.

    Args:
        arg (str): The command-line argument to be converted.

    Returns:
        float: The converted value.

    Raises:
        SystemExit: If the argument is not a valid number or is not positive.
    """
    try:
        num = float(arg)
    except ValueError:
        sys.exit("Command-line argument is not a number")
    else:
        if num <= 0:
            sys.exit("Command-line argument must be greater than 0")
    return num


main()
