# Demonstration of core Python basics: variables, data types, operators, comments, and input/output.

# ==========================================
# 1. Variables & Data Types
# ==========================================
name = "Shradha"  # String (str)
age = 23          # Integer (int)
price = 25.99     # Floating-point number (float)
is_student = True # Boolean (bool)
empty_val = None  # NoneType

print("--- 1. Data Types & Checking Types ---")
print("Name:", name, "| Type:", type(name))
print("Age:", age, "| Type:", type(age))
print("Price:", price, "| Type:", type(price))
print("Is Student:", is_student, "| Type:", type(is_student))
print("Empty Value:", empty_val, "| Type:", type(empty_val))
print()

# ==========================================
# 2. Operators
# ==========================================
num1 = 10
num2 = 3

print("--- 2. Operators ---")
# Arithmetic Operators
print("Addition (+):", num1 + num2)
print("Subtraction (-):", num1 - num2)
print("Multiplication (*):", num1 * num2)
print("Division (/):", num1 / num2)
print("Modulus (%):", num1 % num2)
print("Exponentiation (**):", num1 ** num2)

# Relational / Comparison Operators
print("\nRelational Operations:")
print("Is num1 > num2?:", num1 > num2)
print("Is num1 == num2?:", num1 == num2)
print("Is num1 != num2?:", num1 != num2)

# Assignment Operators
x = 5
x += 3  # Equivalent to x = x + 3
print("\nAssignment (x += 3):", x)

# Logical Operators
val1 = True
val2 = False
print("\nLogical Operations:")
print("val1 AND val2:", val1 and val2)
print("val1 OR val2:", val1 or val2)
print("NOT val1:", not val1)
print()

# ==========================================
# 3. Type Conversion vs. Type Casting
# ==========================================
print("--- 3. Type Conversion & Casting ---")
# Implicit Type Conversion (Python handles automatically)
a = 1
b = 2.0
result_implicit = a + b  # Converts integer 'a' to float
print("Implicit Conversion (int + float):", result_implicit, "| Type:", type(result_implicit))

# Explicit Type Casting (Manual conversion)
str_num = "2"
casted_num = int(str_num)  # Converting string to integer
result_explicit = a + casted_num
print("Explicit Casting str('2') -> int:", result_explicit)
print()

# ==========================================
# 4. User Input
# ==========================================
print("--- 4. Accepting User Input ---")
# input() returns values as string by default
user_name = input("Enter your name: ")
user_age = int(input("Enter your age: "))    # Type-casted to int
user_gpa = float(input("Enter your GPA: "))   # Type-casted to float

print(f"\nHello {user_name}! Next year you will be {user_age + 1} years old.")
print(f"Your GPA is recorded as: {user_gpa}")

'''
There are two types of comments in python. 
1. Single Line comment
2. Multi Line comment

- This is the multi line comment
'''

# This is a single line comment.