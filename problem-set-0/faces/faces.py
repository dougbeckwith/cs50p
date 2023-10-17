def main():
    # Prompt the user for text input
    user_input = input("Enter some text: ")

    # Call the 'convert' function to replace emoticons with emojis
    user_input = convert(user_input)

    # Print the modified text with emojis
    print(user_input)

def convert(text:str):
    # Replace ":)" with a smiling face emoji
    text = text.replace(":)", "\U0001F642")

    # Replace ":(" with a sad face emoji
    text = text.replace(":(", "\U0001F641" )
    
    return text


main()
    