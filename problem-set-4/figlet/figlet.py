from pyfiglet import Figlet
import sys
import random

def main():
    figlet = Figlet()
    fonts = figlet.getFonts()
    num_args = len(sys.argv)

    validate_args(num_args, fonts)
    set_figlet_font(num_args, figlet, fonts)

    user_input = input("Input: ")
    print("Output: \n", figlet.renderText(user_input))


def validate_args(num_args, fonts):
    message = "Invalid usage"
    if  num_args != 1 and num_args != 3:
        sys.exit(message)
    
    if num_args == 3:
        if sys.argv[1] != '-f' and sys.argv[1] != '--font':
            sys.exit(message)
        if sys.argv[2] not in fonts:
            sys.exit(message)


def set_figlet_font(num_args, figlet, fonts):
    if num_args == 3:
        figlet.setFont(font=sys.argv[2])
    else:
        figlet.setFont(font=random.choice(fonts))

main()


