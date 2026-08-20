"""
Lecture 3: Lists & Tuples
Covers: List indexing/slicing, List methods, Tuple operations, and Practice Problems.
"""

# ==========================================
# 1. LIST BASICS & SLICING
# ==========================================
print("--- 1. List Basics & Slicing ---")

# Creating a list with mixed data types
student = ["Karan", 85, "Delhi"]
print("Original List:", student)  # Output: ['Karan', 85, 'Delhi']

# Mutability: Lists can be changed
student[0] = "Arjun"
print("After Modification:", student)  # Output: ['Arjun', 85, 'Delhi']
print("Length of List:", len(student))  # Output: 3

# List Slicing
marks = [87, 64, 33, 95, 76]
print("Slice [1:4]:", marks[1:4])      # Output: [64, 33, 95]
print("Slice [:4]:", marks[:4])        # Output: [87, 64, 33, 95]
print("Negative Slice [-3:-1]:", marks[-3:-1])  # Output: [33, 95]
print()


# ==========================================
# 2. LIST METHODS
# ==========================================
print("--- 2. List Methods ---")

num_list = [2, 1, 3]

# append() - Adds element to end
num_list.append(4)
print("After append(4):", num_list)  # [2, 1, 3, 4]

# sort() - Ascending order
num_list.sort()
print("After sort():", num_list)  # [1, 2, 3, 4]

# sort(reverse=True) - Descending order
num_list.sort(reverse=True)
print("After sort(reverse=True):", num_list)  # [4, 3, 2, 1]

# reverse() - Reverses list
num_list.reverse()
print("After reverse():", num_list)  # [1, 2, 3, 4]

# insert(idx, el) - Insert at index
num_list.insert(1, 5)
print("After insert(1, 5):", num_list)  # [1, 5, 2, 3, 4]

# remove(el) - Removes first occurrence
demo_list = [2, 1, 3, 1]
demo_list.remove(1)
print("After remove(1):", demo_list)  # [2, 3, 1]

# pop(idx) - Removes element at index
demo_list.pop(0)
print("After pop(0):", demo_list)  # [3, 1]
print()


# ==========================================
# 3. TUPLES & TUPLE METHODS
# ==========================================
print("--- 3. Tuples & Methods ---")

# Tuple syntax
tup = (87, 64, 33, 95, 76)
print("Tuple:", tup)  #

# Single element tuple syntax requirement
single_tup = (1,)  # Notice the trailing comma
print("Single Element Tuple:", single_tup)

# Tuples are immutable: tup[0] = 43 is NOT allowed

# Tuple Methods
tup_demo = (2, 1, 3, 1)
print("Index of '1':", tup_demo.index(1))  # Returns 1 (first occurrence)
print("Count of '1':", tup_demo.count(1))  # Returns 2
print()


# ==========================================
# 4. PRACTICE PROBLEMS
# ==========================================
print("--- 4. Practice Problems ---")

# Problem 1: Favorite Movies List
movies = []
mov1 = input("Enter 1st favorite movie: ")
mov2 = input("Enter 2nd favorite movie: ")
mov3 = input("Enter 3rd favorite movie: ")

movies.append(mov1)
movies.append(mov2)
movies.append(mov3)
print("Favorite Movies List:", movies)
print()

# Problem 2: Palindrome List Check
list1 = [1, 2, 3, 2, 1]
copy_list1 = list1.copy()
copy_list1.reverse()

if list1 == copy_list1:
    print(f"List {list1} is a Palindrome")
else:
    print(f"List {list1} is NOT a Palindrome")
print()

# Problem 3: Count Grade 'A' in Tuple
grades_tuple = ("C", "D", "A", "A", "B", "B", "A")
print("Occurrences of 'A':", grades_tuple.count("A"))
print()

# Problem 4: Store in List and Sort 'A' to 'D'
grades_list = ["C", "D", "A", "A", "B", "B", "A"]
grades_list.sort()
print("Sorted Grades:", grades_list)