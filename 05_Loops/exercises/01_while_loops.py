"""
Practice Exercises using while loops.
"""

# Problem 1: Print numbers 1 to 100
print("--- Numbers 1 to 100 ---")
num = 1
while num <= 100:
    print(num, end=" ")
    num += 1
print("\n")

# Problem 2: Print numbers 100 to 1
print("--- Numbers 100 to 1 ---")
num = 100
while num >= 1:
    print(num, end=" ")
    num -= 1
print("\n")

# Problem 3: Multiplication table of n
n = int(input("Enter number for multiplication table: "))
i = 1
while i <= 10:
    print(f"{n} x {i} = {n * i}")
    i += 1
print()

# Problem 4: Print list elements using loop
nums_list = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
idx = 0
while idx < len(nums_list):
    print(f"Index {idx}:", nums_list[idx])
    idx += 1
print()

# Problem 5: Search for x in tuple
tup = (1, 4, 9, 16, 25, 36, 49, 64, 81, 100)
x = 36
i = 0
found = False
while i < len(tup):
    if tup[i] == x:
        print(f"Found {x} at index {i}")
        found = True
        break
    i += 1

if not found:
    print(f"{x} not found in tuple")
print()

# Problem 6: Sum of first n numbers
n_sum = int(input("Enter n to calculate sum: "))
total_sum = 0
counter = 1
while counter <= n_sum:
    total_sum += counter
    counter += 1
print(f"Sum of first {n_sum} numbers is: {total_sum}")