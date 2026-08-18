'''Create a small program that asks for:

name
age
monthly_income
monthly_expense

Then calculate:

annual_income
annual_expense
monthly_savings
annual_savings

Then calculate:

savings_percentage

Finally print whether the person saves at least 20% of their
monthly income.'''


name = input("Name: ")
age = int(input("Age: "))
monthly_income = int(input("Monthly Income: "))
monthly_expense = int(input("Monthly Expense: "))

annual_income = monthly_income * 12
annual_expense = monthly_expense * 12
monthly_savings = monthly_income - monthly_expense
annual_savings = monthly_savings * 12

savings_percentage = (monthly_savings / monthly_income) * 100

print(f"\n------------ Summary for {name} : Age : {age} ---------------")
print(f"Annual Income: ${annual_income:,.2f}")
print(f"Annual Expense: ${annual_expense:,.2f}")
print(f"Monthly Savings: ${monthly_savings:,.2f}")
print(f"Annual Savings: ${annual_savings:,.2f}")
print(f"Savings Rate: {savings_percentage:.1f}%")

print(f"Saves at least 20% of monthly income: {savings_percentage >= 20}")