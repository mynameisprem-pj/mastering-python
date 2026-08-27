"""
Recursion Practice Problems
"""

# Problem 1: Recursive function to calculate sum of first n natural numbers
def sum_natural_recursive(n):
    if n == 0:
        return 0  #
    return n + sum_natural_recursive(n - 1)  #


# Problem 2: Recursive function to print all elements in a list
def print_list_recursive(lst, idx=0):
    if idx == len(lst):  # Base Case: Reached end of list
        return  #
    print(lst[idx], end=" ")  #
    print_list_recursive(lst, idx + 1)  # Recursive Step


# --- Testing Functions ---
print("--- Recursive Sum ---")
n = 5
print(f"Sum of first {n} natural numbers:", sum_natural_recursive(n))

print("\n--- Recursive List Traversal ---")
numbers = [1, 4, 9, 16, 25]
print("List elements printed recursively:")
print_list_recursive(numbers)
print()