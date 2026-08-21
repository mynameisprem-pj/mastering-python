# Lecture 4: Dictionary & Sets 🐍

Welcome to **Lecture 4** of the Python learning series! This directory contains code examples, practice exercises, and summary notes covering key-value pair structures (**Dictionaries**) and unique collection structures (**Sets**).

---

## 🧠 Concepts Covered

### 1. Dictionary in Python
* **Definition:** Used to store data values in `key:value` pairs
* **Properties:** Unordered, mutable (changeable), and keys must be unique (no duplicates allowed)
* **Accessing & Modifying:** Elements are accessed using `dict["key"]` and modified or added via `dict["key"] = value`
* **Nested Dictionaries:** Dictionaries stored inside another dictionary (e.g., `student["score"]["math"]`)

### 2. Common Dictionary Methods
* `dict.keys()`: Returns all keys present in the dictionary
* `dict.values()`: Returns all values stored in the dictionary
* `dict.items()`: Returns all `(key, value)` pairs as tuples
* `dict.get("key")`: Safely retrieves the value associated with a key (avoids raising an error if key doesn't exist)
* `dict.update(newDict)`: Inserts/updates specified key-value items into the dictionary

### 3. Sets in Python
* **Definition:** A collection of unordered items where every element must be **unique** and **immutable**
* **Duplicates Handling:** Duplicate items are automatically ignored (e.g., `{1, 2, 2, 2}` becomes `{1, 2}`)
* **Empty Set Syntax:** Must be declared using `set()` because `{}` creates an empty dictionary

### 4. Common Set Methods
* `set.add(el)`: Adds an element to the set
* `set.remove(el)`: Removes the specified element
* `set.clear()`: Empties the set completely
* `set.pop()`: Removes and returns an arbitrary/random value
* `set.union(set2)`: Combines values from both sets and returns a new set
* `set.intersection(set2)`: Returns a new set containing only common elements

---

## 📄 File Structure

* `lecture_04.py` - Single master script demonstrating all dictionary and set concepts and practice solutions.

---

## 🎯 Practice Problems Solved
1. Store specified word meanings in a Python dictionary
2. Calculate the total unique classrooms required given a list of subjects
3. Enter marks for 3 subjects from user input and store them in a dynamically populated empty dictionary
4. Figure out a way to store `9` and `9.0` as distinct separate values inside a set