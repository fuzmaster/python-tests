# Prompt the user to enter the bank name, credit card debt limit, current debt, and APR
bank_info = []

# Prompt the user to enter the bank name
bank_info.append(input("Enter the name of your bank: "))

# Prompt the user to enter the credit card debt limit and current debt
bank_info.append(float(input("Enter credit card debt limit: ")))
bank_info.append(float(input("Enter credit card debt: ")))

# Prompt the user to enter the APR as a decimal with a decimal point
bank_info.append(float(input("Enter the APR (Annual Percentage Rate) as a decimal (e.g., 0.15 for 15%): ")))

# Calculate the difference between the debt limit and current debt
debt_available = bank_info[1] - bank_info[2]

# Output the results to the user
print(f"Your bank name is {bank_info[0]}.")
print(f"Your credit card debt limit is {bank_info[1]:.2f}.")
print(f"Your current credit card debt is {bank_info[2]:.2f}.")
print(f"Your APR is {bank_info[3]:.2%}.")
print(f"You have {debt_available:.2f} of available credit.")
