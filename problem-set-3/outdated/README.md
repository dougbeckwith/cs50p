# Date Converter

This Python script is a simple date converter that allows the user to input a date in various formats and then outputs the date in the standardized "YYYY-MM-DD" format. It performs input validation and parsing, ensuring that the entered date is valid and correctly formatted.

## Usage

1. Run the script in a Python environment.

2. Enter a date when prompted.

3. The script will attempt to parse the entered date in either of the following formats:

   - MM/DD/YYYY (e.g., 9/8/1636)
   - Month Day, Year (e.g., September 8, 1636)

4. If the parsing is successful, the script will output the date in "YYYY-MM-DD" format.

## Functions

- `get_date()`: Responsible for collecting and validating the date input from the user. It handles both date formats and checks for correctness.
- `create_date(day, month, year)`: Creates a date dictionary from day, month, and year values.
- `format_date(date)`: Converts the date dictionary into the "YYYY-MM-DD" format.
- `print_date(date)`: Prints the formatted date.

## List of Months

The script uses a list of month names for validation and formatting. The list is defined as follows:

```python
months = [
    "January", "February", "March", "April", "May", "June", "July",
    "August", "September", "October", "November", "December"
]
```

## Example

```python
Date: 9/8/1636
Output: 1636-09-08
```
