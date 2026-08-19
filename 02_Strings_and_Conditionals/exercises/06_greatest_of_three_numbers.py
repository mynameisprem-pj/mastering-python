'''Take three numbers as input from the user 
(convert them using type casting to int or float). 
Write conditional statements to determine and 
print which of the three numbers is the greatest.'''

num1 = int(input("Enter a number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

if num2 < num1 > num3:
    print(f"Greatest number: {num1}")
elif num1 < num2 > num3:
    print(f"Greatest number: {num2}")
else:
    print(f"Greatest number: {num3}")

