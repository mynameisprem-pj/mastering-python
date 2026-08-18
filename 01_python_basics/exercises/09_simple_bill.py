'''
09_simple_bill.py

Input:
price
quantity

Calculate:
total = price × quantity

Example:
Price: 50
Quantity: 3

Total: 150
'''

print('\n================ Simple Bill ==============')
price = int(input("Price: "))
quantity = int(input("Quantity: "))
total = price * quantity
print(f"Total: {total}")

