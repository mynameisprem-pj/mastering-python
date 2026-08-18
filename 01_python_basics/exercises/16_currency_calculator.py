'''Ask the user for:

amount
conversion_rate

Calculate:

converted_amount = amount × conversion_rate'''

amount = float(input("Enter amount: "))
coversion_rate = float(input("Enter conversion rate: "))

converted_amount = amount * coversion_rate

print(f"Converted Amount: {converted_amount}")
