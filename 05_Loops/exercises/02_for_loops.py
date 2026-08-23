"""
Practice Exercises using for loops.
"""

# Problem 1: Print list elements
nums_list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
print("--- Traversing list with for loop ---")
for el in nums_list:
    print(el, end=" ")
print("\n")

# Problem 2: Search for x in tuple
tup = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
x = 49
idx = 0
for el in tup:
    if el == x:
        print(f"Found {x} at index {idx}")
        break
    idx += 1
else:
    print("Element not found")
print()

# Problem 3: Factorial of first n numbers
n = int(input("Enter n to calculate factorial: "))
fact = 1
for i in range(1, n + 1):
    fact *= i
print(f"Factorial of {n} is: {fact}")