# List of month names for validation and formatting
months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

def main():
    date = get_date()
    formated_date = format_date(date)
    print_date(formated_date)

# Function to get and parse a valid date input from the user
def get_date():
    
    while True:
        date_input = input("Date: ")
        is_split = False

        # Attempt to parse the date in MM/DD/YYYY format (e.g., 9/8/1636)
        try:
            month, day, year = date_input.split("/")
            is_split = True
        except ValueError:
            pass
        
        # If the date wasn't successfully split, attempt to parse it in Month Day, Year format (e.g., September 8, 1636)
        if not is_split:  
            try:
                month, day, year = date_input.split() 
            except ValueError:
                continue

            # Remove any commas from the day part (e.g., "8," becomes "8")
            if ',' in day:
                day = day.replace(',',"")
            else: 
                continue

            # Validate and convert the month to a numeric value
            if month in months:
                month = months.index(month) + 1   
            else:
                continue

        # Validate and convert day, month, and year to integers
        try:  
            day = int(day)
            month = int(month)
            year = int(year)
        except ValueError:
            continue
        
        # Additional validation checks for day and month
        if month > 12 or day > 31:
            continue
     
        # If all checks pass, return a date dictionary
        try:
            return create_date(day, month, year)
        except ValueError:
            continue
       

# Function to create a date dictionary from day, month, and year
def create_date(day, month, year):  
    return {
        "day": day,
        "month": month,
        "year": year
    }   


# Function to format the date as YYYY-MM-DD
def format_date(date):
    day = date["day"]
    month = date["month"]
    year = date["year"]

    # Format the parts with leading zeros if needed
    day_str = f"{day:02d}"
    month_str = f"{month:02d}"

    # Concatenate the parts with hyphens
    formatted_date = f"{year}-{month_str}-{day_str}"
    
    return formatted_date
    

def print_date(date):
    print(date)
    

main()