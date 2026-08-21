"""
Lecture 4: Dictionary & Sets
Covers: Dictionaries, Nested Dictionaries, Dictionary Methods, Sets, Set Methods, and Practice Problems.
"""

# ==========================================
# 1. DICTIONARY BASICS & NESTED DICTIONARIES
# ==========================================
print("--- 1. Dictionary Basics & Nested Dictionaries ---")

# Creating a basic dictionary
info = {
    "name": "shradha",
    "cgpa": 9.6,
    "marks": [98, 97, 95]
}
print("Original Dictionary:", info)  

# Accessing and modifying values
print("Name:", info["name"])          # Output: shradha
info["name"] = "Rahul"                # Modifying existing key
info["is_adult"] = True               # Adding new key-value pair
print("Updated Dictionary:", info)
print()

# Nested Dictionary
student = {
    "name": "shradha",
    "score": {
        "math": 95,
        "chem": 98,
        "phy": 97
    }
}
print("Nested Student Dict:", student)  
print("Math Marks:", student["score"]["math"])  # Output: 95
print()


# ==========================================
# 2. DICTIONARY METHODS
# ==========================================
print("--- 2. Dictionary Methods ---")

my_dict = {
    "name": "Shradha",
    "score": 95,
    "city": "Delhi"
}

# dict.keys()
print("Keys:", list(my_dict.keys()))  

# dict.values()
print("Values:", list(my_dict.values()))  

# dict.items()
print("Items (Tuples):", list(my_dict.items()))  

# dict.get("key")
print("Get 'name':", my_dict.get("name"))  # Output: Shradha
# Advantage of .get(): Returns None if key doesn't exist instead of throwing an Error

# dict.update()
new_data = {"city": "Mumbai", "age": 22}
my_dict.update(new_data)
print("After update():", my_dict)  
print()


# ==========================================
# 3. SET BASICS & METHODS
# ==========================================
print("--- 3. Set Basics & Methods ---")

# Creating sets (duplicates are automatically removed)
nums = {1, 2, 3, 4}
set2 = {1, 2, 2, 2}
print("Unique Set 2:", set2)  # Output: {1, 2}

# Syntax for empty set
null_set = set()  # {} creates an empty dict, so set() must be used
print("Type of null_set:", type(null_set))
print()

# Set Modification Methods
s = {1, 2}
s.add(3)
s.add(2)  # Duplicate will be ignored
print("After add():", s)  # Output: {1, 2, 3}

s.remove(2)
print("After remove(2):", s)  # Output: {1, 3}

s.pop()  # Removes a random element
print("After pop():", s)  

s.clear()
print("After clear():", s)  # Output: set()
print()

# Set Mathematical Operations: Union & Intersection
set_a = {1, 2, 3}
set_b = {2, 3, 4}

print("Union:", set_a.union(set_b))                # Output: {1, 2, 3, 4}
print("Intersection:", set_a.intersection(set_b))  # Output: {2, 3}
print()


# ==========================================
# 4. PRACTICE PROBLEMS
# ==========================================
print("--- 4. Practice Problems ---")

# Problem 1: Word Meanings Dictionary
word_dict = {
    "table": ["a piece of furniture", "list of facts & figures"],
    "cat": "a small animal"
}
print("Word Dictionary:", word_dict)  
print()

# Problem 2: Classrooms required for subjects
subject_list = ["python", "java", "C++", "python", "javascript", "java", "python", "java", "C++", "C"]
# Using set to extract unique subjects
unique_subjects = set(subject_list)
print("Unique Subjects List:", unique_subjects)
print("Total Classrooms Needed:", len(unique_subjects))  
print()

# Problem 3: Subject Marks Entry
marks_dict = {}

sub1 = input("Enter 1st subject name: ")
mark1 = int(input(f"Enter marks for {sub1}: "))
marks_dict[sub1] = mark1

sub2 = input("Enter 2nd subject name: ")
mark2 = int(input(f"Enter marks for {sub2}: "))
marks_dict[sub2] = mark2

sub3 = input("Enter 3rd subject name: ")
mark3 = int(input(f"Enter marks for {sub3}: "))
marks_dict[sub3] = mark3

print("Marks Dictionary:", marks_dict)  
print()

# Problem 4: Store 9 and 9.0 as separate values in a set
# Solution Method: Store values as different data types or tuples
values_set = {9, "9.0"}
print("Storing 9 and '9.0' as separate values:", values_set)  

# Alternative Method: Using built-in tuple wrappers
alt_set = {("int", 9), ("float", 9.0)}
print("Alternative Method using Tuples:", alt_set)  