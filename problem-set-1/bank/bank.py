# Prompt user for greeting and convert to lowercase with leading whitespace removed.
greeting = input("Greeting: ").lstrip().lower()

# If the greeting starts with "hello," print "$0."
if greeting[0:5] == "hello":
    print("$0")
# Else check if the first character of the input is "h"
elif greeting[0:1] == "h":
    print("$20")
 # If the input doesn't match any of the conditions above, print "$100."
else:
    print("$100")
