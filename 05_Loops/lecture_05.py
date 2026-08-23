"""
Lecture 5: Loops in Python
Covers: while loops, break/continue, for loops, for-else, range(), and pass statement.
"""

# ==========================================
# 1. WHILE LOOPS
# ==========================================
print("--- 1. while Loops ---")

# Printing hello 5 times
count = 1
while count <= 5:
    print("hello", count)
    count += 1
print()


# ==========================================
# 2. BREAK & CONTINUE
# ==========================================
print("--- 2. break & continue ---")

# break example: Stop loop when i reaches 3
i = 1
while i <= 5:
    if i == 3:
        break  # Terminate loop
    print("Break loop item:", i)
    i += 1

print()

# continue example: Skip multiples of 2
j = 0
while j < 5:
    j += 1
    if j % 2 == 0:
        continue  # Skip rest of iteration
    print("Odd number via continue:", j)

print()


# ==========================================
# 3. FOR LOOPS & FOR-ELSE
# ==========================================
print("--- 3. for Loops & for-else ---")

# Traversing a list
nums = [1, 2, 3]
for el in nums:
    print("Element:", el)  #

print()

# for-else block
for el in nums:
    print("Item:", el)
else:
    print("Loop completed successfully!")  # Executes after loop finishes

print()


# ==========================================
# 4. RANGE() FUNCTION & PASS
# ==========================================
print("--- 4. range() & pass Statement ---")

# range(stop)
for val in range(3):
    print("range(3):", val)  # 0, 1, 2

# range(start, stop)
for val in range(1, 4):
    print("range(1, 4):", val)  # 1, 2, 3

# range(start, stop, step)
for val in range(1, 6, 2):
    print("range(1, 6, 2):", val)  # 1, 3, 5

print()

# pass statement (placeholder)
for el in range(5):
    pass  # Does nothing, acts as placeholder

print("pass executed without errors.")