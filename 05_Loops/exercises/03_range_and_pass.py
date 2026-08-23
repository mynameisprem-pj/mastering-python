"""
Practice Exercises using range() and loop control.
"""

# Problem 1: Print 1 to 100 using range()
print("--- 1 to 100 using range() ---")
for i in range(1, 101):
    print(i, end=" ")
print("\n")

# Problem 2: Print 100 to 1 using range()
print("--- 100 to 1 using range() ---")
for i in range(100, 0, -1):
    print(i, end=" ")
print("\n")

# Problem 3: Multiplication table of n using range()
n = int(input("Enter number for multiplication table: "))
for i in range(1, 11):
    print(f"{n} x {i} = {n * i}")