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


# ==============================================================================
# Level 2 - Exercise 4: Filter Countries Containing 'land' (Pass 2: Alternative Exploration) — verified 2026-10-08
# ==============================================================================
# Exploration Objectives:
# 1. Implementation Alternatives:
#    - Option A (List Comprehension with Filtering):
#      Filter items using a list comprehension: `[elem for elem in ... if <condition>]`.
#    - Option B (Inline Lambda with filter()):
#      Instead of defining a standalone `def` helper function, pass an anonymous inline lambda directly to `filter()`.
#
# 2. Mechanistic Analysis & Trade-offs:
#    - Readability vs Functional style: List comprehensions are generally considered more Pythonic and concise than `filter()` with a lambda.
#    - Execution Overhead: `filter()` with a Python lambda invokes a function frame for every element, whereas list comprehensions execute optimized C-level loop bytecode.
# ==============================================================================

# Target Output: ['Finland', 'Iceland']
'''
# Option A: List comprehension
country_six = [country for country in countries if "land" in country]
print(country_six)

# Option B: Inline lambda with filter
country_six = list(filter(lambda x: "land" in x, countries))
print(country_six)
'''


# ==============================================================================
# Level 2 - Exercise 5: Filter Countries with Exactly Six Characters (Pass 2: Alternative Exploration) — verified 2026-10-08
# ==============================================================================
# Exploration Objectives:
# 1. Implementation Alternatives:
#    - Option A (List Comprehension):
#      Filter elements by exact length using a list comprehension: `[elem for elem in ... if len(elem) == ...]`.
#    - Option B (Inline Lambda with filter()):
#      Use `filter()` paired with an inline lambda checking the length.
#
# 2. Mechanistic Analysis & Trade-offs:
#    - In-place predicate logic: Avoid namespace pollution by omitting single-use named functions for simple length checks.
# ==============================================================================

# Target Output: ['Sweden', 'Norway']
'''
# Option A: List comprehension
country_w_six = [country for country in countries if len(country) == 6]
print(country_w_six)

# Option B: Inline lambda with filter
country_w_six = list(filter(lambda x: len(x) == 6, countries))
print(country_w_six)
'''


# ==============================================================================
# Level 2 - Exercise 6: Filter Countries with Six or More Letters (Pass 2: Alternative Exploration) — verified 2026-10-08
# ==============================================================================
# Exploration Objectives:
# 1. Implementation Alternatives:
#    - Option A (List Comprehension):
#      Filter elements using `>=` length comparison inside a list comprehension.
#    - Option B (Inline Lambda with filter()):
#      Use `filter()` paired with an inline lambda with `>=`.
#
# 2. Mechanistic Analysis & Trade-offs:
#    - Comparison operators in functional pipelines: Observe the syntactic parity between exact match (`==`) and inequality (`>=`) across both paradigms.
# ==============================================================================

# Target Output: ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
'''
# Option A: List comprehension
country_w_six_or_more = [country for country in countries if len(country) >= 6]
print(country_w_six_or_more)

# Option B: Inline lambda with filter
country_w_six_or_more = list(filter(lambda x: len(x) >= 6, countries))
print(country_w_six_or_more)
'''