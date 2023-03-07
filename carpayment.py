# Car Payment Plan Calculator with Down Payment Check

# Function to calculate monthly payments
def calculate_monthly_payment(car_price, down_payment, interest_rate, loan_term):
    # Calculate the loan amount, monthly interest rate, and number of payments
    loan_amount = car_price - down_payment
    monthly_interest_rate = interest_rate / 12
    num_payments = loan_term * 12
    
    # Calculate the monthly payment using the formula:
    # P = (PV * r) / (1 - (1 + r)^(-n))
    monthly_payment = (loan_amount * monthly_interest_rate) / (1 - (1 + monthly_interest_rate)**(-num_payments))
    
    return monthly_payment

# Get the car details from the user and store them in arrays
car_names = []
car_prices = []
down_payments = []
interest_rates = []
loan_terms = []

for i in range(2):
    print("Enter the details for car", i+1)
    car_names.append(input("Enter the car name: "))
    car_prices.append(float(input("Enter the car price: ")))
    
    # Prompt the user to enter the down payment and check that it's below 20% of the car price
    down_payment = float(input("Enter the down payment: "))
    while down_payment >= (0.2 * car_prices[i]):
        print("Error: Down payment must be less than 20% of the car price ($" + str(0.2 * car_prices[i]) + " or less).")
        down_payment = float(input("Enter the down payment: "))
    down_payments.append(down_payment)
    
    interest_rates.append(float(input("Enter the annual interest rate (as a decimal): ")))
    loan_terms.append(int(input("Enter the loan term (in years): ")))

# Calculate the monthly payments for each car
monthly_payments = []

for i in range(2):
    monthly_payment = calculate_monthly_payment(car_prices[i], down_payments[i], interest_rates[i], loan_terms[i])
    monthly_payments.append(monthly_payment)

# Print the monthly payments to the console
print("Monthly Payments:")
print(car_names[0], ":", "$", round(monthly_payments[0], 2))
print(car_names[1], ":", "$", round(monthly_payments[1], 2))

# Compare the monthly payments and print the result
if monthly_payments[0] < monthly_payments[1]:
    print(car_names[0], "has the lower monthly payment.")
elif monthly_payments[0] > monthly_payments[1]:
    print(car_names[1], "has the lower monthly payment.")
else:
    print("Both cars have the same monthly payment.")
