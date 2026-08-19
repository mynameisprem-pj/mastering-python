'''
Write a program to ask the user for their full name using input() 
and display:The total character count (length) of the entered name.  
The name in all capitalized format using .capitalize(). '''

name = input("Enter your full name: ")
print(f"Length of the Name: {len(name)}")
print(f"Name in capitalized format: {name.capitalize()}")