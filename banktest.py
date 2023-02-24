def main():
    # Prompt the user to enter the credit card debt
    while True:
        try:
            debt = float(input("Enter your credit card debt: ")) # Get the user's credit card debt as a float
            if debt <= 0:
                raise ValueError
            break
        except ValueError:
            print("Invalid input. Please enter a positive number for your credit card debt.")

    # Print the credit card debt to the user
    print(f"Your credit card debt is {debt}.")

if __name__ == '__main__':
    main()
