def main():
    # Prompt user for cameCase word
    camel_case = input("camelCase: ")

    # Convert camel_case string to snake_case string
    snake_case = to_snake_case(camel_case)

    # Print snake_case version
    print(snake_case)


def to_snake_case(camel_case):
    snake_case = ""
    for char in camel_case:
        if char.isupper():
            snake_case = snake_case + "_" + char.lower()
        else:
            snake_case = snake_case + char
    return snake_case

main()