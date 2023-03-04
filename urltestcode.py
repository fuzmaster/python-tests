# Create an empty list to store the names
names = []

# Loop until the user says they are done entering names
while True:
    # Prompt the user to enter a name
    name = input("Enter a name (or 'done' to finish): ")
    # If the user enters 'done', exit the loop
    if name == 'done':
        break
    # Add the name to the names list
    names.append(name)

# Join all the names in the names list with commas and print the resulting string
print(','.join(names))
