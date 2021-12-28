# coding: utf-8
import csv
from pathlib import Path

# List of loan costs.
loan_costs = [500, 600, 200, 1000, 450]

# The len() function counts the number of items in the list.
number_of_loans = len(loan_costs)
print(f"There are a total of {number_of_loans} loans.")

# The sum() function adds all the numbers in the list together.
sum_of_loans = sum(loan_costs)
print (f"The total amount spent on loans is ${sum_of_loans:,.2f}")

# This equation determines the average loan price by using previously defined variables.
average_loan_price = sum_of_loans / number_of_loans
print(f"The average loan price is ${average_loan_price:,.2f}")

# Use the loan dictionary to determine the future value and remaining months for the loan, 
# use these values to then determine the present value.
loan = {
    "loan_price": 500,
    "remaining_months": 9,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

# The .get() function is used when trying to pull a specific value from a dictionary. 
future_value = loan.get("future_value")
remaining_months = loan.get("remaining_months")
print(f"The future value is ${future_value:,.2f} and {remaining_months} months are remaining.")

# Write a present value equation with the given discount rate and 
# our previously defined variables for future value and remaining months.
discount_rate = 0.2

present_value_first = future_value / (1 + discount_rate/12) ** remaining_months

print(f"The present value of the loan is ${present_value_first:,.2f}")

# Loan profit is a variable that is an estimation of total profit by using the present value and loan variables.
loan_profit = present_value_first - loan["loan_price"]

# This conditional statement determines if a loan price is worth investment bu comparing present value and loan price.
if present_value_first >= loan["loan_price"]:
    print(f"The loan has a present value ${loan_profit:,.2f} higher than the cost, therefore the loan is worth at least the cost.")
else:
    print(f"The loan is too expensive and not worth the price, you will lose ${-loan_profit:,.2f}")

# Use the given new loan dictionary. 
new_loan = {
    "loan_price": 800,
    "remaining_months": 12,
    "repayment_interval": "bullet",
    "future_value": 1000,
}

# Present value function.
def present_value_calculator(future_value, remaining_months, annual_discount_rate):
    present_value_second = future_value / (1 + discount_rate/12) ** remaining_months
    return present_value_second

# Given discount rate.
annual_discount_rate = 0.2

# Calls the present value function and uses the new loan dictionary data.
new_present_value = present_value_calculator(new_loan["future_value"], new_loan["remaining_months"], annual_discount_rate)

print(f"The present value of the loan is ${new_present_value:,.2f}")

# Given list of dictionaries.
loans = [
    {
        "loan_price": 700,
        "remaining_months": 9,
        "repayment_interval": "monthly",
        "future_value": 1000,
    },
    {
        "loan_price": 500,
        "remaining_months": 13,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 200,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
    {
        "loan_price": 900,
        "remaining_months": 16,
        "repayment_interval": "bullet",
        "future_value": 1000,
    },
]

# Empty list where we will send the inexpensive loans. 
inexpensive_loans = []

# For loop which reads loans then appends all loans under $500 to the inexpensive loans list.
for loan in loans:
    loan_price = loan.get("loan_price") # Got help from Charles's code on this one.

    if loan_price <= 500:
        inexpensive_loans.append(loan)

print(f"List of inexpensive loans: {inexpensive_loans}.")

# Sets the output header.
header = ["loan_price", "remaining_months", "repayment_interval", "future_value"]

# Set the output file path, outputs into the same folder as this python file.
output_path = Path("inexpensive_loans.csv")

# Opens the output file to write, then writes the header before writing the rest. 
with open(output_path, "w") as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(header)
    for row in inexpensive_loans:
        csvwriter.writerow(row.values())
