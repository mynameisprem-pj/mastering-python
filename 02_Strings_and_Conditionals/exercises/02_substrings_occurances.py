'''Write a program that takes a text input from the user 
(for example, "I bought $5 worth of items for $10") 
and counts how many times the $ symbol appears in it'''

text = input("Enter a text: ")
print(f"$ count: {text.count("$")}")

