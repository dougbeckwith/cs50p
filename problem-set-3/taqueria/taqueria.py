menu = { 
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

def main():
   calculate_total()


# Calculate the total price of selected menu items
def calculate_total():
    total = 0.00
    while True:
        try:
            item = prompt_for_item()
        except EOFError:
            print("")
            break
    
        try:
            total += menu[item]
        except KeyError:
            continue

        print_total(total)


# Prompt the user to enter a menu item, ensuring it's title-cased    
def prompt_for_item():
    try:
        return input("Item: ").title()
    except  EOFError:
        raise EOFError


# Print the total price with formatting as currency (rounded to 2 decimal places)
def print_total(price):
    print(f"Total: ${price:.2f}")


main()