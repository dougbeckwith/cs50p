import emoji

def main():
    user_input = input("Input: ")

    # Use emoji to replace emoji aliases in the user's input with actual emoji characters.
    print(emoji.emojize(user_input, language='alias'))

main()