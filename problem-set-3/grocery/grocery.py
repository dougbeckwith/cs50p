def main():
    groceries = create_groceries_dict()
    sorted_groceries = sort_groceries(groceries)
    print_groceries(sorted_groceries)
   
# Keep prompting user for grocery item until user quits ctrl-d
def create_groceries_dict():
    items = {}
    while True:
        try :
            # Prompt the user for a grocery item and convert it to uppercase
            item = input("").upper()

            # Update the dictionary with the grocery item and its quantity
            if item in items:
                items[item] += 1
            else:
                items[item] = 1
        except EOFError:
            return items


def print_groceries(grocery_list):
    # Print the grocery items and their quantities
    for item in grocery_list:
        print(grocery_list[item], item)


def sort_groceries(groceries_dict):
    # Sort the groceries dictionary by item name
    return dict(sorted(groceries_dict.items(), key=lambda item: item[0]))


main()