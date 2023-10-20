def main():
    # Prompt the user to input a string
    text = input("Input: ")

    # Remove vowels from a given string
    vowels_removed = remove_vowels(text)

    # Print the resulting string with vowels removed
    print(vowels_removed)

# Define a function to remove vowels from a given string.
# Input: str - The input string from which vowels should be removed.
# Return: str - The string with vowels removed.
def remove_vowels(string):
    # Initialize an empty string to store characters without vowels
    new_string = ""

    # Define a list of vowel characters to check against
    vowels = ["a", "e", "i", "o", "u"]
    
    # Iterate through each character in the input string
    for char in string:
        # Check if the lowercase character is not a vowel
        if char.lower() not in vowels: 
           # Append the character to the new string if it's not a vowel   
           new_string += char
    
    return new_string

main()
