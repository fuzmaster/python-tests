# Prompt the user to enter the bank name, credit card debt limit, current debt, and APR
bank_info = []
bank_info.append(input("Enter the name of your bank: "))
bank_info.append(float(input("Enter credit card debt limit: ")))
bank_info.append(float(input("Enter credit card debt: ")))
bank_info.append(float(input("Enter the APR (Annual Percentage Rate) as a decimal (e.g., 0.15 for 15%): ")))

# Calculate the difference between the debt limit and current debt
debt_available = bank_info[1] - bank_info[2]

# Calculate the monthly interest rate
monthly_rate = bank_info[3] / 12

# Calculate the minimum monthly payment needed to pay off the debt in 12 months
monthly_payment = (bank_info[2] * monthly_rate) / (1 - (1 + monthly_rate)**-12)

# Check if the monthly payment is less than the debt available
if monthly_payment <= debt_available:
    print("You can pay off your debt in 12 months.")
else:
    print(f"To pay off your debt in 12 months, you need to make a monthly payment of {monthly_payment:.2f}.")

# Output the results to the user
print(f"Your bank name is {bank_info[0]}.")
print(f"Your credit card debt limit is {bank_info[1]:.2f}.")
print(f"Your current credit card debt is {bank_info[2]:.2f}.")
print(f"Your APR is {bank_info[3]:.2%}.")
print(f"You have {debt_available:.2f} of available credit.")
