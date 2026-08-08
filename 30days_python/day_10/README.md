# Day 10: Loops

Life is full of routines. In programming, we also perform many repetitive tasks. To handle repetitive tasks efficiently without rewriting code, programming languages use **loops**. 

Python provides two main types of loops:
- **While loop**
- **For loop**

---

## 1. While Loop
A `while` loop repeatedly executes a block of statements as long as a given condition evaluates to `True`. Once the condition becomes `False`, execution stops, and the program continues with the statements following the loop.

### While Loop with `else`
In Python, an optional `else` block can be attached to a `while` loop. The code inside the `else` block executes once when the condition becomes `False` and the loop completes naturally without encountering a `break` statement.

---

## 2. Loop Control Statements: `break` and `continue`

### `break` Statement
The `break` keyword is used to exit or terminate a loop prematurely before its normal completion condition is reached. When encountered, Python immediately breaks out of the loop and resumes execution at the next line after the loop block.

### `continue` Statement
The `continue` keyword is used to skip the rest of the code inside the current iteration of the loop and immediately move on to the next iteration.

---

## 3. For Loop
A `for` loop is used for iterating over a sequence (such as a string, list, tuple, set, or dictionary). It iterates through each item in the collection sequentially from beginning to end.

### Iterating Over Sequences
- **Strings:** Iterates through each character in the string.
- **Lists and Tuples:** Iterates through each item in order.
- **Sets:** Iterates through each element in an unordered collection.
- **Dictionaries:** By default, iterates through the keys of the dictionary. It can also iterate through keys, values, or key-value pairs depending on the method used.

### For Loop with `else`
Just like `while` loops, a `for` loop can also have an optional `else` block. The `else` block executes after all items in the sequence have been processed, provided the loop was not exited early using `break`.

---

## 4. The `range()` Function
The `range()` function is commonly used with `for` loops to generate a sequence of numbers dynamically.

It takes up to three arguments:
1. **Start:** The starting integer of the sequence (inclusive).
2. **Stop:** The ending integer of the sequence (exclusive).
3. **Step:** The difference between each number in the sequence (increment or decrement).

---

## 5. Nested Loops
A nested loop is a loop inside another loop (an inner loop inside an outer loop). For every single iteration of the outer loop, the inner loop executes completely from start to finish.

---

## 6. The `pass` Statement
The `pass` statement acts as a null operation or placeholder. When a loop is required by Python syntax but no code execution is desired yet, `pass` prevents syntax errors and allows code construction without immediate implementation.

