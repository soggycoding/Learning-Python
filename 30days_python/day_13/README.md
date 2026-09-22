# 📘 Day 13: List Comprehension & Lambda Functions

Welcome to **Day 13**! Today we unlock one of the most celebrated and idiomatic features in Python: **List Comprehensions**, alongside anonymous **Lambda Functions**.

---

## 1. List Comprehension

### What is a List Comprehension?
A list comprehension is a concise, expressive, and optimized syntax to construct a new list from an existing iterable (lists, tuples, ranges, strings).

In traditional loops, you:
1. Initialize an empty accumulator list `lst = []`.
2. Write a `for` loop.
3. Check an `if` condition.
4. Call `.append()` on every iteration.

In a list comprehension, all of that collapses into a single declarative line.

### Syntax Anatomy:
```python
[expression for item in iterable if condition]
```
Let's dissect each component:
- **`for item in iterable`**: Iterates through each element in the source sequence.
- **`if condition`** *(optional)*: Boundary filter. Only items evaluating to `True` reach the expression.
- **`expression`**: What gets evaluated and placed into the new list. Can be mathematical (`x ** 2`), string formatting (`f"#{x:06x}"`), or method calls (`s.upper()`).

### The Performance Advantage (Why List Comprehensions are Faster):
Why do software engineers prefer list comprehensions over traditional `for` loops with `.append()`?
1. **No Attribute Lookup Overhead**: In Python, calling `lst.append(x)` requires looking up the `.append` attribute on the list object on *every single iteration*.
2. **C-Level Loop Execution**: Under the hood (in CPython), a list comprehension is optimized into dedicated bytecode instructions (`LIST_APPEND`), executing in native C loops rather than interpreted Python loop steps.

---

## 2. Variations & Common Patterns

### A. Transformation (Map Pattern)
Transforming each item directly:
```python
# Square numbers from 0 to 5
squares = [x ** 2 for x in range(6)]
# Result: [0, 1, 4, 9, 16, 25]
```

### B. Filtering (Filter Pattern)
Keeping only items that satisfy a predicate:
```python
numbers = [-4, -2, 0, 1, 3, 5]
# Keep only non-positive numbers
non_positives = [x for x in numbers if x <= 0]
# Result: [-4, -2, 0]
```

### C. If-Else Ternary Expression (Transform Both Branches)
> [!IMPORTANT]
> Notice the position of the `if / else`!
> - When **filtering out** items: the `if` goes at the **very end** (no `else` allowed).
> - When **transforming** items based on a condition: the ternary `expression_if_true if cond else expression_if_false` goes at the **beginning**.

```python
# Label numbers as 'even' or 'odd'
parity = ["even" if x % 2 == 0 else "odd" for x in range(5)]
# Result: ['even', 'odd', 'even', 'odd', 'even']
```

### D. Nested Loops & Flattening Multi-Dimensional Lists
You can nest loops inside a list comprehension. The order of `for` clauses in the comprehension matches the nesting order of normal `for` loops!

```python
# Normal nested loops:
# for row in matrix:
#     for item in row:
#         flat.append(item)

matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flattened = [item for row in matrix for item in row]
# Result: [1, 2, 3, 4, 5, 6, 7, 8, 9]
```

---

## 3. Lambda Functions (Anonymous Functions)

### What is a Lambda?
A **lambda function** is a small, anonymous function defined with the `lambda` keyword instead of `def`.
- It can accept any number of positional arguments.
- It can only contain **a single expression**.
- It returns the result of that expression automatically (no `return` keyword allowed!).

### Syntax Anatomy:
```python
lambda arg1, arg2, ... : expression
```

### Basic Examples:
```python
# Adding two numbers
add = lambda a, b: a + b
print(add(3, 5))  # 8

# Squaring a number
square = lambda x: x ** 2
print(square(4))  # 16
```

### Mathematical Applications: Linear Equations
Linear equations take the form:
$$y = mx + b$$
Where:
- $m$ is the **slope**: $\frac{y_2 - y_1}{x_2 - x_1}$
- $b$ is the **y-intercept**: $y - mx$

Using lambdas:
```python
# Slope between two points (x1, y1) and (x2, y2)
calc_slope = lambda x1, y1, x2, y2: (y2 - y1) / (x2 - x1)

# Y-intercept given slope m and a point (x, y)
calc_intercept = lambda m, x, y: y - (m * x)
```

### When to Use Lambdas vs `def`:
- **Use Lambdas**: As quick throwaway callback functions passed into higher-order functions like `sort(key=...)`, `map()`, or `filter()` (which we will master on Day 14).
- **Use `def`**: For any multi-line logic, complex branches, reusable business logic, or functions that require docstrings and type annotations. (PEP 8 explicitly discourages assigning lambdas directly to variables with names like `add = lambda ...` in production code; prefer `def add(...)` for named functions!).

---

## 4. Key Takeaways for Today's Exercises
1. **List Comprehensions** provide clean, high-performance declarative list creation.
2. Filter conditions go at the end: `[expr for item in seq if predicate]`.
3. Ternary transformations go at the start: `[val1 if cond else val2 for item in seq]`.
4. Nested comprehensions preserve left-to-right reading order identical to standard nested loops.
5. **Lambdas** provide concise, single-expression anonymous functions.
