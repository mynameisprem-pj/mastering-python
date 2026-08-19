"""
Lecture 2: Strings & Conditional Statements
Covers: Concatenation, Length, Indexing, Slicing, String Functions, and Conditionals.
"""

# ==========================================
# 1. STRING BASICS & OPERATIONS
# ==========================================
print("--- 1. String Basics & Operations ---")

# Concatenation
str1 = "hello"
str2 = "world"
final_str = str1 + " " + str2
print("Concatenation:", final_str)  # Output: hello world

# Length of string
print("Length of string:", len(final_str))  # Output: 11
print()


# ==========================================
# 2. INDEXING & SLICING
# ==========================================
print("--- 2. Indexing & Slicing ---")

# Indexing
name = "Prem_Jha"
print("First character (index 0):", name[0])  # Output: 'P'
# Note: name[0] = 'B' is not allowed because strings are immutable

# Positive Slicing
text = "ApnaCollege"
print("Slice [1:4]:", text[1:4])  # Output: 'pna'
print("Slice [:4]:", text[:4])    # Same as text[0:4] -> 'Apna'
print("Slice [1:]:", text[1:])    # Same as text[1:len(text)] -> 'pnaCollege'

# Negative Slicing
fruit = "Apple"
print("Negative Slice [-3:-1]:", fruit[-3:-1])  # Output: 'pl'
print()


# ==========================================
# 3. COMMON STRING FUNCTIONS
# ==========================================
print("--- 3. Common String Functions ---")

sentence = "I am a coder."

print("Ends with '.':", sentence.endswith("."))       # Returns True
print("Ends with 'er.':", sentence.endswith("er."))   # Returns True
print("Capitalize:", sentence.capitalize())          # Capitalizes 1st char
print("Replace 'coder' with 'developer':", sentence.replace("coder", "developer"))  #
print("Find index of 'am':", sentence.find("am"))    # Returns 1st index of substring
print("Count occurrences of 'a':", sentence.count("a"))  # Counts occurrences
print()


# ==========================================
# 4. CONDITIONAL STATEMENTS
# ==========================================
print("--- 4. Conditional Statements Syntax & Grading ---")

# Marks Grading System
marks = 85

if marks >= 90:
    grade = "A"
elif marks >= 80:
    grade = "B"
elif marks >= 70:
    grade = "C"
else:
    grade = "D"

print(f"Marks: {marks}, Grade: {grade}")



