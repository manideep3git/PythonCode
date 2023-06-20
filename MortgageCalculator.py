# It's a very basic mortgage calculator 

def mortgage_calculator(principal, interest_rate, years):
    monthly_interest_rate = interest_rate / 100 / 12
    num_payments = years * 12

    # Calculate the monthly mortgage payment
    monthly_payment = (
        principal
        * monthly_interest_rate
        * (1 + monthly_interest_rate) ** num_payments
    ) / ((1 + monthly_interest_rate) ** num_payments - 1)

    # Calculate the total payment over the mortgage term
    total_payment = monthly_payment * num_payments

    # Calculate the total interest paid
    total_interest = total_payment - principal

    # Return the results
    return monthly_payment, total_payment, total_interest


# Example usage
principal = float(input("Enter the principal amount: "))
interest_rate = float(input("Enter the annual interest rate: "))
years = int(input("Enter the number of years: "))

monthly_payment, total_payment, total_interest = mortgage_calculator(
    principal, interest_rate, years
)

print("\nMortgage Calculation Results")
print("----------------------------")
print(f"Principal: ${principal:.2f}")
print(f"Interest Rate: {interest_rate:.2f}%")
print(f"Years: {years}")
print("----------------------------")
print(f"Monthly Payment: ${monthly_payment:.2f}")
print(f"Total Payment: ${total_payment:.2f}")
print(f"Total Interest: ${total_interest:.2f}")
