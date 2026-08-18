'''Input:

principal
rate
time

Calculate simple interest:

SI = (P × R × T) / 100

Then calculate total amount:

amount = principal + SI'''

p = float(input("Enter principal: "))
t = float(input("Enter time: "))
r = float(input("Enter rate of interest: "))

si = (p * t * r) / 100
amount = p + si

print(f"Simple Interest: {si}")
print(f"Amount: {amount}")