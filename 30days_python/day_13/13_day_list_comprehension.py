# Day 13: List Comprehension & Lambda Functions - Interactive Walkthrough

# ==============================================================================
# SECTION 1: Basic List Comprehensions (Map & Transform)
# ==============================================================================
# Syntax: [expression for item in iterable]

# Example A: Converting string characters into a list
language = 'Python'
chars = [c for c in language]
print("1A. Chars from string:", chars)

# Example B: Generating and transforming numbers
numbers = [i for i in range(11)]
print("1B. Numbers 0 to 10:", numbers)

squares = [i * i for i in range(11)]
print("1B. Squares 0 to 10:", squares)

# Example C: Making tuples inside a comprehension
num_and_square_tuples = [(i, i * i) for i in range(6)]
print("1C. Tuples (i, i^2):", num_and_square_tuples)


# ==============================================================================
# SECTION 2: List Comprehensions with Filtering (Filter Pattern)
# ==============================================================================
# Syntax: [expression for item in iterable if condition]
# The 'if' filter goes at the END! Only elements satisfying the condition are kept.

# Example A: Even numbers
even_numbers = [i for i in range(21) if i % 2 == 0]
print("\n2A. Even numbers 0-20:", even_numbers)

# Example B: Odd numbers with arithmetic transformation
odd_squares = [i * i for i in range(11) if i % 2 != 0]
print("2B. Squares of odd numbers:", odd_squares)

# Example C: Filtering negative and positive numbers
mixed_numbers = [-5, 3, -1, 101, -200, 42, 0]
positive_only = [x for x in mixed_numbers if x > 0]
print("2C. Positives only:", positive_only)


# ==============================================================================
# SECTION 3: Conditional Transformations (Ternary If-Else)
# ==============================================================================
# Syntax: [val_if_true if condition else val_if_false for item in iterable]
# When modifying what gets placed into the list based on a condition,
# the ternary expression goes at the BEGINNING.

labels = ["even" if x % 2 == 0 else "odd" for x in range(6)]
print("\n3. Ternary parity labels:", labels)


# ==============================================================================
# SECTION 4: Nested Loops & Flattening Multi-Dimensional Lists
# ==============================================================================
# Syntax: [expression for outer_item in outer_list for inner_item in outer_item]
# The 'for' clauses follow the EXACT same left-to-right order as nested for loops.

# Example A: Flattening a 2D Matrix
matrix_2d = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
flat_2d = [num for row in matrix_2d for num in row]
print("\n4A. Flattened 2D matrix:", flat_2d)

# Example B: Flattening a 3D Matrix (List of lists of lists)
matrix_3d = [
    [[1, 2]],
    [[3, 4]],
    [[5, 6]]
]
flat_3d = [num for sublist in matrix_3d for row in sublist for num in row]
print("4B. Flattened 3D matrix:", flat_3d)


# ==============================================================================
# SECTION 5: Lambda Functions (Anonymous Functions)
# ==============================================================================
# Syntax: lambda param1, param2, ... : expression
# No 'def' or 'return' statement needed.

# Example A: Basic lambdas
add = lambda a, b: a + b
print("\n5A. Lambda add(5, 7):", add(5, 7))

square = lambda x: x ** 2
print("5A. Lambda square(6):", square(6))

# Example B: Self-invoking (immediately invoked) lambda
sum_direct = (lambda a, b, c: a + b + c)(2, 3, 4)
print("5B. Immediately invoked lambda:", sum_direct)

# Example C: Linear Equations with Lambda
# Linear line: y = m*x + b
# Slope (m) = (y2 - y1) / (x2 - x1)
calc_slope = lambda x1, y1, x2, y2: (y2 - y1) / (x2 - x1)
print("5C. Slope between (1, 2) and (3, 6):", calc_slope(1, 2, 3, 6))

# Y-intercept (b) = y - (m * x)
calc_y_intercept = lambda m, x, y: y - (m * x)
print("5C. Y-intercept with m=2 at point (1, 2):", calc_y_intercept(2, 1, 2))

# Example D: Lambda inside a higher-order generator function
def make_power(n):
    return lambda x: x ** n

cube = make_power(3)
print("5D. Closure lambda cube(3):", cube(3))
