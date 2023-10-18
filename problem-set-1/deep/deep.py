# Prompt user for input
answer = input("What is the Answer to the Great Question of Life, the Universe and Everything? ")

# Lower case and remove all leading and trailing whitespace
answer = answer.lower().strip()

# Print "Yes" or "No" based on users answer
match answer:
    case "42" | "forty-two" | "forty two":
        print("Yes")
    case _: 
        print("No")