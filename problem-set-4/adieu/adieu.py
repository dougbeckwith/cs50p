import sys

def main():
    names = []
    while True:
        try:
            user_input = input('Name: ')
            names.append(user_input)
        except EOFError:
            print_bid_adieu(names)
            sys.exit()     

def print_bid_adieu(names):
    farewell_message = "Adieu, adieu, to"

    # Check if there are no names to bid farewell to
    if not names:
        return
    
    num_names = len(names)

    if num_names == 1:
        farewell_message += f" {names[0]}"
    elif num_names == 2:
        farewell_message += f" {names[0]} and {names[1]}"
    else:
        farewell_message += " " + ", ".join(names[:-1]) + f", and {names[-1]}"

    print(farewell_message)
    
main()