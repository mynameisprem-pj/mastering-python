'''
06_average_of_two_numbers.py

Input two floating-point numbers and print their average.
'''

num_1 = float(input("Enter a number: "))
num_2 = float(input("Enter another number: "))
print(f"Average: {(num_1 + num_2) / 2:.2f}") 

# Here :.2f is used to format a floating-point number to exactly two decimal places
# Example: if the average comes 12.33333345...
# then :.2f formats it 12.34 , only two decimal places