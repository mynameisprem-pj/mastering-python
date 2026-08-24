"""
Lecture 6: Functions & Recursion
Covers: Function definitions, parameters, return statements, default parameters, and recursion.
"""

# ==========================================
# 1. FUNCTION DEFINITIONS & CALLS
# ==========================================
print("--- 1. Function Basics ---")

# Function to calculate sum of two numbers
def calc_sum(a, b):
    s = a + b
    return s  #

sum_val = calc_sum(2, 3)
print("Sum of 2 and 3:", sum_val)  # Output: 5

# Function with no parameters and no return
def print_hello():
    print("Hello, World!")  #

print_hello()
print()


# ==========================================
# 2. DEFAULT PARAMETERS
# ==========================================
print("--- 2. Default Parameters ---")

# b has a default value of 1
def multiply(a, b=1):
    return a * b  #

print("Multiply with 2 arguments (4, 5):", multiply(4, 5))  # Output: 20
print("Multiply with 1 argument (4):", multiply(4))         # Output: 4 (uses b=1)
print()


# ==========================================
# 3. RECURSION BASICS
# ==========================================
print("--- 3. Recursion Basics ---")

# Function to print numbers from n down to 1 using recursion
def show(n):
    if n == 0:  # Base Case
        return  #
    print(n)
    show(n - 1)  # Recursive Step

print("Printing 5 down to 1 recursively:")
show(5)
print()


# Recursive function to calculate factorial of n
def factorial(n):
    if n == 0 or n == 1:  # Base Case
        return 1  #
    else:
        return n * factorial(n - 1)  # Recursive Step

fact_res = factorial(5)
print("Factorial of 5:", fact_res)  # Output: 120
print()


# Recursive function to calculate sum of first n natural numbers
def calc_natural_sum(n):
    if n == 0:  # Base Case
        return 0  #
    return n + calc_natural_sum(n - 1)  # Recursive Step

print("Sum of first 5 natural numbers:", calc_natural_sum(5))  # Output: 15