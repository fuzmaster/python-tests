def calculate_months_to_payoff(balance, limit, interest_rate, minimum_payment):
    # Calculate the monthly interest rate from the annual interest rate
    monthly_interest_rate = interest_rate / 12
    
    # Initialize the months variable to 0
    months = 0
    
    # Loop until the balance is paid off
    while balance > 0:
        # Add interest to the balance
        balance += balance * monthly_interest_rate
        
        # Subtract the minimum payment from the balance
        balance -= minimum_payment
        
        # Check if the balance exceeds the card limit
        if balance > limit:
            print("You have exceeded your card limit.")
            break
        
        # Increment the months variable by 1
        months += 1
        
    # Return the number of months it took to pay off the balance
    return months


def main():
    # Prompt the user to enter the debt, card limit, interest rate, and minimum payment
    while True:
        try:
            debt = float(input("Enter your debt: "))
            if debt <= 0:
                raise ValueError
            break
        except ValueError:
            print("Invalid input. Please enter a positive number for your debt.")
    
    while True:
        try:
            limit = float(input("Enter your card limit: "))
            if limit <= 0:
                raise ValueError
            break
        except ValueError:
            print("Invalid input. Please enter a positive number for your card limit.")
    
    while True:
        try:
            interest_rate = float(input("Enter the annual interest rate as a decimal: "))
            if interest_rate <= 0:
                raise ValueError
            break
        except ValueError:
            print("Invalid input. Please enter a positive number for your annual interest rate.")
    
    while True:
        try:
            minimum_payment = float(input("Enter the minimum monthly payment: "))
            if minimum_payment <= 0:
                raise ValueError
            break
        except ValueError:
            print("Invalid input. Please enter a positive number for your minimum monthly payment.")

    # Calculate the number of months it will take to pay off the credit card
    months_to_payoff = calculate_months_to_payoff(debt, limit, interest_rate, minimum_payment)

    # Print the result to the user
    if months_to_payoff == 0:
        print("You have paid off your debt!")
    else:
        print(f"It will take {months_to_payoff} months to pay off your debt.")


if __name__ == '__main__':
    main()
