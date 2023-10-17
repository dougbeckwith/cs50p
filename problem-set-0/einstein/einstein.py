# Prompt the user to enter the mass in kilograms to calculate the equivalent energy in joules.
user_input = input("Enter the mass in kilograms to calculate the equivalent energy in joules: ")

# Convert the user's input from a string to an integer.
mass_kg = int(user_input)

# Calculate the energy (E) using the equation E = mc^2, where:
# - E is the energy in joules,
# - m is the mass in kilograms, and
# - c is the speed of light (approximately 300000000 meters per second).
# We square the speed of light to account for the square of the speed in the equation.
energy_joules = mass_kg * (300000000 ** 2)

# Print the calculated energy in joules.
print(energy_joules)
