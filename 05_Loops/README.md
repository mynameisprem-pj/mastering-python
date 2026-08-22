# Lecture 5: Loops in Python 🔁

Welcome to **Lecture 5** of the Python learning series! This directory covers iteration techniques using `while` loops, `for` loops, sequence controls (`break`, `continue`, `pass`), and the `range()` function.

---

## 🧠 Concepts Covered

### 1. `while` Loops
* **Syntax:** Repeats a block of code as long as a condition remains `True`.
* **Iterators:** Variables used to control loop execution and count iterations.
* **Infinite Loops:** Occur if the terminating condition is never met.

### 2. Control Statements (`break`, `continue`, `pass`)
* `break`: Immediately terminates the loop execution when encountered.
* `continue`: Skips the rest of the code in the current iteration and jumps to the next one.
* `pass`: A null statement used as a placeholder for future code execution.

### 3. `for` Loops & `for-else`
* **Traversal:** Used for sequential traversal over lists, tuples, strings, etc.
* `for-else`: The `else` block executes when the loop finishes normally (does **not** run if the loop is terminated by a `break`).

### 4. `range()` Function
* Generates a sequence of numbers starting from `0` by default, incrementing by `1` (default), and stopping before a specified number.
* **Syntax:** `range(start?, stop, step?)`

---

## 📁 Directory Layout

* `lecture_05.py` - Core theory and syntax demonstrations.
* `exercises/` - Dedicated folder containing all solved practice problems.
  * `01_while_loops.py` - Counting, tables, searching, and sum using `while` loops.
  * `02_for_loops.py` - Sequential traversal, searching, and factorial using `for` loops.
  * `03_range_and_pass.py` - Iteration with ranges and control flow statements.