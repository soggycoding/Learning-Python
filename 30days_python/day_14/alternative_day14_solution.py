# Day 14: Higher Order Functions, Closures & Decorators - Alternative Solutions (Pass 2)

# ==============================================================================
# Starter Datasets Provided for Day 14
# ==============================================================================
countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# ==============================================================================
# Level 2 - Exercise 1: Uppercase Countries (Pass 2: Alternative Exploration) — verified 2026-10-07
# ==============================================================================
# Exploration Objectives:
# 1. Implementation Alternatives:
#    - Option A (List Comprehension):
#      Transform each country name to uppercase using standard list comprehension
#      syntax `[... for x in ...]`.
#    - Option B (map() with no `def` helper):
#      Pass built-in `str.upper` directly into `map()` without defining a custom helper.
#
# 2. Mechanistic Analysis & Trade-offs:
#    - Function Call Overhead: In Python, calling a custom user-defined function in a
#      loop incurs bytecode frame overhead. List comprehensions and built-in methods
#      implemented in C skip that extra layer of Python function calls.
#    - Readability: In modern Python, list comprehensions are preferred over `map()`
#      for simple element-wise transformations.
# ==============================================================================

# Target Output: ['ESTONIA', 'FINLAND', 'SWEDEN', 'DENMARK', 'NORWAY', 'ICELAND']
'''
# Option A: List comprehension
country = [x.upper() for x in countries]
print(country)

# Option B: Method reference with map
upper_country = list(map(str.upper, countries))
print(upper_country)
'''


# ==============================================================================
# Level 2 - Exercise 2: Square Numbers (Pass 2: Alternative Exploration) — verified 2026-10-07
# ==============================================================================
# Exploration Objectives:
# 1. Implementation Alternatives:
#    - Option A (List Comprehension):
#      Compute the square of each number using a list comprehension `[... for x in ...]`.
#    - Option B (Inline Lambda with map):
#      Instead of declaring a standalone `def` helper function that is only used once,
#      pass an anonymous inline `lambda` directly into `map()`.
#
# 2. Mechanistic Analysis & Trade-offs:
#    - Single-use Functions: When a helper function is small (1 expression) and only
#      used in one place, declaring it with `def` pollutes the namespace. A `lambda`
#      keeps it localized, but list comprehensions are generally even cleaner and more
#      idiomatic in modern Python.
# ==============================================================================

# Target Output: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
'''
# Option A: List comprehension
squared = [n**2 for n in numbers]
print(squared)

# Option B: Inline lambda with map
squared = list(map(lambda x: x**2, numbers))
print(squared)
'''


# ==============================================================================
# Level 2 - Exercise 3: Uppercase Names (Pass 2: Alternative Exploration) — verified 2026-10-07
# ==============================================================================
# Exploration Objectives:
# 1. Implementation Alternatives:
#    - Option A (List Comprehension):
#      Transform each name to uppercase using a list comprehension.
#    - Option B (map() with no `def` helper):
#      Transform `names` using `map(str.upper, names)`.
#
# 2. Mechanistic Analysis & Trade-offs:
#    - Consistency across String Iterables: Notice how cleanly the patterns from
#      Exercise 1 generalize to any string sequence.
# ==============================================================================

# Target Output: ['ASABENEH', 'LIDIYA', 'ERMIAS', 'ABRAHAM']
'''
# Option A: List comprehension
upper_names = [x.upper() for x in names]
print(upper_names)

# Option B: Method reference with map
upper_names = list(map(str.upper, names))
print(upper_names)
'''
