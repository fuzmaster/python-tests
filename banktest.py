# Prompt the user to enter the bank name
bank_name = input("Enter the name of your bank: ")

# Prompt the user to enter the credit card debt limit and current debt
debt_limit = float(input("Enter credit card debt limit: "))
debt_current = float(input("Enter credit card debt: "))

# Prompt the user to enter the APR as a float
apr = float(input("Enter the APR (Annual Percentage Rate) as a decimal: "))

# Calculate the difference between the debt limit and current debt
debt_available = debt_limit - debt_current

# Output the results to the user
print(f"Your bank name is {bank_name}.")
print(f"Your credit card debt limit is {debt_limit:.2f}.")
print(f"Your current credit card debt is {debt_current:.2f}.")
print(f"Your APR is {apr:.2%}.")
print(f"You have {debt_available:.2f} of available credit.")
