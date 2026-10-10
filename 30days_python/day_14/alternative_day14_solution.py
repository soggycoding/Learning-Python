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


# ==============================================================================
# Level 2 - Exercise 7: Filter Countries Starting with 'E' (Pass 2: Alternative Exploration) — verified 2026-10-10
# ==============================================================================
# Exploration Objectives:
# 1. Implementation Alternatives:
#    - Option A (List Comprehension):
#      Filter elements starting with `'E'` using a list comprehension: `[elem for elem in ... if <condition>]`.
#    - Option B (Case-Insensitive Tuple Matching):
#      Pass a tuple of allowed prefixes to `.startswith(('E', 'e'))` within `filter()` or a comprehension.
#
# 2. Mechanistic Analysis & Trade-offs:
#    - String Prefix Flexibility: `str.startswith()` accepts a tuple of candidates (e.g. `str.startswith(('A', 'B'))`), making multi-character/multi-casing checks fast and idiomatic without boolean concatenation.
# ==============================================================================

# Target Output: ['Estonia']
'''
# Option A
target_letter = 'E', 'e'
country = [x for x in countries if x.startswith(target_letter)]
print(country)

# Option B
country = list(filter(lambda x: x.startswith(("E" , 'e')), countries))
print(country)
'''

# ==============================================================================
# Level 2 - Exercise 8: Chain Two or More List Iterators (Pass 2: Alternative Exploration) — verified 2026-10-10
# ==============================================================================
# Exploration Objectives:
# 1. Implementation Alternatives:
#    - Option A (Generator Expression with built-in sum()):
#      Replace the nested `reduce()` + `map()` + `filter()` pipeline with a single generator expression fed into built-in `sum()`:
#      `sum(transform(elem) for elem in ... if predicate(elem))`
#    - Option B (Comprehension + built-in sum()):
#      Compare the generator pipeline against a list comprehension fed into `sum()`.
#
# 2. Mechanistic Analysis & Trade-offs:
#    - Functional vs Pythonic: In Python, `sum(f(x) for x in seq if cond(x))` is universally preferred over nested `reduce(lambda ..., map(..., filter(...)))` because it eliminates lambda dispatch overhead, avoids deep nesting parentheses, and runs via optimized C loops.
# ==============================================================================

# Target Output: 220
'''
# Option A:
nums = sum(x ** 2 for x in numbers if x % 2 == 0)
print(nums)

# Option B:
nums = sum([x ** 2 for x in numbers if x % 2 == 0])
print(nums)
'''
# ==============================================================================
# Level 2 - Exercise 9: get_string_lists Function (Pass 2: Alternative Exploration) — verified 2026-10-10
# ==============================================================================
# Exploration Objectives:
# 1. Implementation Alternatives:
#    - Option A (List Comprehension inside function):
#      Implement `get_string_lists(lst)` using a concise list comprehension: `[elem for elem in lst if isinstance(elem, str)]`.
#    - Option B (Generator Function with yield):
#      Define a generator function `def get_string_gen(lst):` that `yield`s string elements on demand, then materialize with `list()`.
#
# 2. Mechanistic Analysis & Trade-offs:
#    - Memory footprint: A generator function streams items one-by-one with O(1) auxiliary space until consumed by the caller, which is ideal for massive collections.
# ==============================================================================

# Target Output: ['apple', 'banana', 'cherry']
'''
# Option A
mixed_list = [1, 'apple', 3.14, 'banana', True, 'cherry']
def get_string_lists(lst):
    return [x for x in lst if isinstance(x, str)]
print(get_string_lists(mixed_list))

# Option B
mixed_list = [1, 'apple', 3.14, 'banana', True, 'cherry']
def get_string_gen(lst):
    for x in lst:
        if isinstance(x, str):
            yield x
print(list(get_string_gen(mixed_list)))
'''