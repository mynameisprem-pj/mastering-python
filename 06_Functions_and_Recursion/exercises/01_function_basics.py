"""
Basic Function Practice Problems
"""

# Problem 1: Function to print length of a list
def print_list_length(lst):
    print("Length of list:", len(lst))  #

# Problem 2: Function to print elements of a list in a single line
def print_list_elements(lst):
    for item in lst:
        print(item, end=" ")  #
    print()

# Problem 3: Function to find factorial of n
def calc_factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i  #
    return fact

# Problem 4: Function to convert USD to INR
def usd_to_inr(usd_val):
    inr_val = usd_val * 83.0  # Assuming 1 USD = 83.0 INR
    return inr_val  #


# --- Testing Functions ---
sample_list = [10, 20, 30, 40, 50]

print("--- Problem 1 ---")
print_list_length(sample_list)

print("\n--- Problem 2 ---")
print_list_elements(sample_list)

print("\n--- Problem 3 ---")
print("Factorial of 5:", calc_factorial(5))

print("\n--- Problem 4 ---")
print("100 USD in INR:", usd_to_inr(100))