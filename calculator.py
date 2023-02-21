# define a function for each operation
def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    return x / y

# display a menu of options for the user
print("Select operation.")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")
print("5. Exit")

# loop until the user chooses to exit
while True:
    # ask the user to choose an operation
    choice = input("Enter choice (1/2/3/4/5): ")
    
    # check if the user wants to exit
    if choice == '5':
        break

    # ask the user to input two numbers
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    # perform the selected operation and display the result
    if choice == '1':
        print(num1, "+", num2, "=", add(num1, num2))

    elif choice == '2':
        print(num1, "-", num2, "=", subtract(num1, num2))

    elif choice == '3':
        print(num1, "*", num2, "=", multiply(num1, num2))

    elif choice == '4':
        print(num1, "/", num2, "=", divide(num1, num2))

    else:
        print("Invalid input")

print("Exiting calculator")
