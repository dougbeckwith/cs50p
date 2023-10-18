# Prompt the user for an expression in the format "x operator z" and split it into components
expression = input("Expression: ").split(" ")

# Extract the numbers and the operator from the expression
x = float(expression[0])
operator = expression[1]
z = float(expression[2])

# Calculate and print the result of the expression with one decimal place
if operator == "+":
    print(round((x + z), 1))
elif operator == "-":
    print(round((x - z), 1))
elif operator == "*":
    print(round((x * z), 1))
elif operator == "/":
    print(round((x / z), 1))
